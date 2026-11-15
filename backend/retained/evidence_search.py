"""Rank reviewed safety evidence using an existing frozen semantic retriever.

No training, numerical parameter fitting or generated scientific claims occur.
Semantic similarity orders source relevance; it never represents safety.
"""
from __future__ import annotations

import copy
import json
import math
import re
from pathlib import Path
from urllib.request import HTTPRedirectHandler, Request, build_opener
from urllib.parse import urlsplit

PILLARS = {"prevention", "detection", "suppression"}
INTENTS = {
    "prevention": ("flammability", "flame spread", "material selection", "fabric", "cotton", "pmma", "sibal", "ignition", "ventilation"),
    "detection": ("detect", "smoke", "aerosol", "particle", "alarm", "dust", "silicone", "kapton", "teflon", "sampling", "sensor"),
    "suppression": ("suppress", "extinguish", "extinction", "co2", "carbon dioxide", "helium", "droplet", "methanol", "heptane", "dilution"),
}


def read_json(path):
    def reject(value):
        raise ValueError("Non-finite JSON value")
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), parse_constant=reject)


def words(value):
    return set(re.findall(r"[a-z0-9]+", value.lower()))


def validate_chains(payload):
    if not isinstance(payload, dict) or payload.get("schema_version") != "fire-safety-chains-v1":
        raise ValueError("Unexpected evidence-chain envelope")
    chains = payload.get("chains")
    if not isinstance(chains, list):
        raise ValueError("Missing evidence chains")
    seen = set()
    for chain in chains:
        if not isinstance(chain, dict) or not isinstance(chain.get("id"), str) or not chain["id"] or chain["id"] in seen:
            raise ValueError("Invalid or duplicate evidence-chain identity")
        seen.add(chain["id"])
        if chain.get("pillar") not in PILLARS or not all(isinstance(chain.get(k), str) and chain[k].strip() for k in ("title", "short_answer", "material")):
            raise ValueError("Incomplete evidence-chain description")
        for key in ("keywords", "canonical_document_ids", "scenario_tags"):
            if not isinstance(chain.get(key), list) or any(not isinstance(x, str) for x in chain[key]):
                raise ValueError("Invalid evidence-chain terms")
        for key in ("conditions", "literature", "data", "next_options"):
            if not isinstance(chain.get(key), list):
                raise ValueError("Incomplete evidence-chain source fields")
        for row in chain["conditions"] + chain["data"]:
            if not isinstance(row, dict):
                raise ValueError("Source fields must be objects")
            value = row.get("value")
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value)):
                raise ValueError("Source numeric values must be finite numbers or null")
            if not isinstance(row.get("display_value"), str) or not isinstance(row.get("label"), str):
                raise ValueError("Missing literal source display value")
        for option in chain["next_options"]:
            if not isinstance(option, dict) or not all(isinstance(option.get(k), str) and option[k].strip() for k in ("label", "query_terms")):
                raise ValueError("Invalid follow-up search option")
        for key in ("experiment", "model", "safety_insight"):
            if not isinstance(chain.get(key), dict):
                raise ValueError("Missing experiment, model or insight scope")
    return payload


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, file, code, message, headers, new_url):
        raise ValueError("The loopback semantic service redirected the request")


class FrozenRetriever:
    def __init__(self, url="http://127.0.0.1:8784/api/search", timeout=15):
        parsed = urlsplit(url)
        if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost"} or parsed.username or parsed.password or parsed.path != "/api/search":
            raise ValueError("Use the configured loopback semantic-search service")
        self.url, self.timeout = url, timeout

    def __call__(self, query, document_ids):
        if not document_ids:
            raise ValueError("No reviewed canonical source bindings")
        body = json.dumps({"query": query, "method": "bge", "top_k": min(50, len(document_ids)),
                           "filters": {"document_ids": document_ids}}).encode("utf-8")
        request = Request(self.url, data=body, headers={"Content-Type": "application/json"}, method="POST")
        with build_opener(NoRedirect()).open(request, timeout=self.timeout) as response:
            result = json.load(response)
        if not isinstance(result, dict) or not isinstance(result.get("model"), dict):
            raise ValueError("Malformed semantic response")
        model = result["model"]
        if model.get("effective_method") != "bge" or model.get("trained") is not False:
            raise ValueError("The frozen BGE retrieval method was not established")
        return result


def search(payload, chains, retriever):
    if not isinstance(payload, dict):
        raise ValueError("Supply a query object")
    query = payload.get("query")
    if not isinstance(query, str) or not query.strip() or len(query) > 2000:
        raise ValueError("Enter a research question of 1-2000 characters")
    filters = payload.get("filters") or {}
    if not isinstance(filters, dict) or set(filters) - {"pillar", "material", "gravity"}:
        raise ValueError("Use the documented pillar, material and gravity filters")
    for key, value in filters.items():
        if value is not None and (not isinstance(value, str) or len(value) > 120):
            raise ValueError("Invalid search filter")
    pillar = filters.get("pillar") or None
    if pillar and pillar not in PILLARS:
        raise ValueError("Unknown safety pillar")
    material = (filters.get("material") or "").strip().lower()
    gravity = (filters.get("gravity") or "").strip().lower()
    effective = query.strip()
    candidates = [c for c in chains if not pillar or c["pillar"] == pillar]
    if material:
        candidates = [c for c in candidates if material in " ".join([c["material"]] + c["keywords"]).lower()]
    if gravity:
        candidates = [c for c in candidates if gravity in " ".join([r["display_value"] for r in c["conditions"] if "gravity" in r.get("label", "").lower()]).lower()]
    lower = effective.lower()
    standards_relevant = any(x in lower for x in ("controlled", "uncontrolled", "standard", "requirement", "containment", "iss fire", "authorized", "approved"))
    out_of_scope = bool(re.search(r"rocket\s+(?:engine|propellant)|propellant\s+(?:fire|tank)|reverse\s+thrust|retropropulsion", lower))
    warnings = ["This prototype ranks three reviewed safety evidence chains; it does not establish coverage of every PSI study.",
                "Semantic relevance is not a safety score, probability, certification or physical match."]
    if out_of_scope:
        warnings.append("Rocket-engine and propellant fire safety is outside these reviewed crew-environment evidence chains.")
        candidates = []
    elif any(x in lower for x in ("lunar", "moon", "martian", "mars", "partial gravity")):
        warnings.append("These examples do not provide measured lunar/Martian partial-gravity combustion conditions; inspect the source gravity and transfer limits.")
    ids = sorted({identifier for chain in candidates for identifier in chain["canonical_document_ids"]})
    semantic_rows, mode, semantic_status, model_name = [], "lexical_fallback", "unavailable", None
    source_retrieval_status, source_answer_eligible = None, False
    if candidates and ids:
        try:
            semantic = retriever(effective, ids)
            if not isinstance(semantic, dict) or not isinstance(semantic.get("results"), list):
                raise ValueError("Malformed semantic results")
            for row in semantic["results"]:
                if not isinstance(row, dict) or not isinstance(row.get("document", {}), dict):
                    raise ValueError("Malformed semantic source")
                identifier = row.get("id") or row.get("document", {}).get("id")
                score = row.get("score")
                if identifier in ids and isinstance(score, (int, float)) and not isinstance(score, bool) and math.isfinite(score):
                    doc = row.get("document") or {}
                    semantic_rows.append({"id": identifier, "title": doc.get("title", identifier), "score": score,
                                          "url": doc.get("doiUrl") or doc.get("sourceUrl")})
            if not semantic_rows:
                raise ValueError("No bound semantic source results")
            mode, semantic_status, model_name = "pretrained_bge_plus_source_conditions", "available", "Frozen pretrained BGE passage retrieval"
            source_retrieval_status = semantic.get("retrieval_status")
            source_answer_eligible = semantic.get("automatic_insight_eligible") is True
            if not source_answer_eligible:
                warnings.append("The upstream retriever has not established automatic answer eligibility. These are source-navigation candidates and pre-reviewed interpretations, not a newly generated answer to the query.")
        except (OSError, ValueError, TypeError, TimeoutError):
            semantic_rows = []
            warnings.append("The local pretrained semantic retriever is unavailable for these bindings. The displayed order uses explicit source terms; no SI ranking is claimed for this request.")
    elif candidates:
        warnings.append("Canonical literature bindings are unavailable; explicit source-term ordering is shown.")
    query_words = words(effective)
    ranked = []
    for chain in candidates:
        matches = [term for term in INTENTS[chain["pillar"]] if term in lower]
        matched_terms = [term for term in chain["keywords"] if words(term) & query_words]
        sources = [r for r in semantic_rows if r["id"] in chain["canonical_document_ids"]]
        best = max((r["score"] for r in sources), default=None)
        reasons = ["Safety question: " + chain["pillar"] + ("; explicit terms: " + ", ".join(matches) if matches else "; inspect the source scope for relevance.")]
        if matched_terms:
            reasons.append("Source-topic overlap: " + ", ".join(matched_terms[:5]))
        if best is not None:
            reasons.append("Frozen BGE retrieved a canonical literature source bound to this reviewed chain.")
        else:
            reasons.append("No bound semantic score is available for this chain; its placement is a source-term fallback.")
        reasons += ["Material / formulation: " + chain["material"],
                    "Documented experiment in this exemplar chain: " + chain["experiment"].get("name", "not supplied"),
                    "Evidence / applicability: " + chain["safety_insight"].get("evidence_level", "not supplied")]
        lexical = len(matches) + len(matched_terms)
        ranked.append({"chain": copy.deepcopy(chain), "score": best if best is not None else (lexical if mode == "lexical_fallback" else None),
                       "rank_reasons": reasons, "semantic_sources": sources,
                       "_sort": (bool(matches), best if best is not None else -1, lexical) if semantic_status == "available" else (bool(matches), lexical, 0)})
    ranked.sort(key=lambda result: result["_sort"], reverse=True)
    options, used = [], set()
    for result in ranked:
        result.pop("_sort")
        for option in result["chain"]["next_options"]:
            key = (option.get("label"), option.get("query_terms"))
            if key not in used:
                used.add(key)
                options.append(copy.deepcopy(option))
    return {"schema_version": "fire-safety-search-v1", "query": effective, "filters": filters,
            "search_mode": mode, "semantic_status": semantic_status, "semantic_model": model_name,
            "source_retrieval_status": source_retrieval_status, "source_answer_eligible": source_answer_eligible,
            "ranking_method": "Explicit safety-pillar terms prioritize the question; bound BGE source relevance orders candidates, with source-topic fallback. Physical conditions and evidence limits are shown separately, not converted into a safety probability.",
            "ranked_results": ranked, "suggested_options": options[:12], "standards_relevant": standards_relevant,
            "scope": "outside_reviewed_scope" if out_of_scope else "three_reviewed_exemplar_chains",
            "warnings": warnings, "training_performed": False, "numerical_model_executed": False}
