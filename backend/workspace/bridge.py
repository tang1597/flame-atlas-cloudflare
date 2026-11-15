"""Read-only links between ranked papers, reviewed findings and chart identities.

No network, model inference, coefficient estimation or file reads occur here.
The offline builder supplies every source/PSI relationship explicitly. Ranking
can be preserved from an upstream response, or use the transparent lexical rule
over one combined corpus when the frozen retriever is unavailable.
"""
from __future__ import annotations

from copy import deepcopy
import math
import re
from urllib.parse import unquote, urlsplit

ALIASES = {
    "打火機": "lighter propane butane gas flame stability", "丙烷": "propane C3H8",
    "丁烷": "butane C4H10", "丙丁烷": "propane butane", "甲醇": "methanol CH3OH",
    "庚烷": "heptane C7H16", "十二烷": "dodecane C12H26", "液滴": "droplet",
    "低氧": "oxygen extinction", "熄滅": "extinction", "基地": "habitat lunar base",
    "微重力": "microgravity", "可控": "flame stability control", "噴口": "burner nozzle",
    "壓力": "pressure", "流量": "flow rate",
}
STOPWORDS = {"the", "in", "a", "paper", "papers", "find", "research", "about", "is", "can"}
RELATIONSHIPS = {"direct_source", "related_work", "related_psi"}
PRIVATE = {"path", "local_path", "localPdf", "localPath", "weights", "credentials", "raw_rows"}
MACHINE_PATH = re.compile(r"(?<![A-Za-z0-9:])[A-Za-z]:[\\/][^\s\"<>]*|file://[^\s\"<>]*", re.I)


def tokens(value):
    return set(re.findall(r"[a-z0-9]+", str(value).lower()))


def public_url(value):
    if not isinstance(value, str) or any(ord(c) < 32 for c in value):
        return None
    try:
        parsed = urlsplit(value)
        return value if parsed.scheme in {"http", "https"} and parsed.hostname and not parsed.username and not parsed.password else None
    except ValueError:
        return None


def source_link(value):
    if isinstance(value, str) and re.fullmatch(r"/sources/[A-Za-z0-9_-]{1,120}\.pdf(?:#page=[1-9][0-9]*)?", value):
        return value
    return public_url(value)


def normalize_doi(value):
    if not isinstance(value, str):
        return None
    value = unquote(value.strip()).lower()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else None


def clean(value):
    if isinstance(value, dict):
        return {key: clean(child) for key, child in value.items()
                if key not in PRIVATE and not str(key).endswith(("_path", "_weights"))}
    if isinstance(value, list):
        return [clean(child) for child in value]
    if isinstance(value, str):
        return MACHINE_PATH.sub("[offline source path withheld]", value)
    return deepcopy(value)


class ReviewedEvidenceBridge:
    def __init__(self, catalog):
        if not isinstance(catalog, dict) or catalog.get("schema_version") != "scene-evidence-bridge-v1":
            raise ValueError("A reviewed scene-evidence catalog is required")
        self.catalog = deepcopy(catalog)
        self.documents = self._registry(catalog.get("documents"), "document")
        self.charts = self._registry(catalog.get("charts"), "chart")
        for chart in self.charts.values():
            if not isinstance(chart.get("points"), list) or not chart.get("evidence_status"):
                raise ValueError("Chart points and evidence status must be explicit")
            for point in chart["points"]:
                if not isinstance(point, dict) or not point.get("source_locator") or not any(k in point for k in ("observed", "predicted")):
                    raise ValueError("A plotted point requires typed source values and a locator")
                for key in ("x", "observed", "predicted"):
                    if key in point and (isinstance(point[key], bool) or not isinstance(point[key], (int, float)) or not math.isfinite(point[key])):
                        raise ValueError("Plot coordinates must be finite source numbers")
        self.findings = self._registry(catalog.get("findings", []), "finding")
        for finding in self.findings.values():
            for insight in finding.get("fire_insights", []):
                if not isinstance(insight, dict) or any(not isinstance(insight.get(k), str) or not insight[k].strip()
                        for k in ("pillar", "claim", "status", "source_locator")):
                    raise ValueError("Standalone fire insights require a pillar, claim, status and source locator")
        self.bindings = {identifier: [] for identifier in self.documents}
        for binding in catalog.get("bindings", []):
            if binding.get("document_id") not in self.documents or binding.get("relationship") not in RELATIONSHIPS:
                raise ValueError("Unknown paper or unreviewed relationship in binding")
            if not binding.get("source_locator") or not binding.get("reason"):
                raise ValueError("An explicit binding locator and reason are required")
            chart_ids = binding.get("chart_ids", [])
            finding_ids = binding.get("finding_ids", [])
            if any(i not in self.charts for i in chart_ids) or any(i not in self.findings for i in finding_ids):
                raise ValueError("Unresolved chart/finding binding")
            self.bindings[binding["document_id"]].append(deepcopy(binding))

    @staticmethod
    def _registry(rows, label):
        if not isinstance(rows, list):
            raise ValueError(f"Explicit {label} registry required")
        registry = {}
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"] or row["id"] in registry:
                raise ValueError(f"Invalid or duplicate {label} identity")
            registry[row["id"]] = deepcopy(row)
        return registry

    def rank_documents(self, query, allowed_study_ids=None, limit=12):
        """Same lexical rule as the baseline, over one augmented paper corpus.

        Adding reviewed sources cannot reorder the unchanged baseline documents
        relative to each other. Zero-overlap documents are never a fallback.
        The scene limits eligible studies; it does not add score tokens.
        """
        if not isinstance(query, str) or not query.strip() or len(query) > 2000:
            raise ValueError("Supply a research query of 1–2000 characters")
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100:
            raise ValueError("Use a document limit from 1 to 100")
        if allowed_study_ids is not None and (not isinstance(allowed_study_ids, (list, tuple, set))
                or any(not isinstance(i, str) for i in allowed_study_ids)):
            raise ValueError("Allowed study IDs must be an explicit list or None")
        allowed = set(allowed_study_ids) if allowed_study_ids is not None else None
        expanded = query.strip() + " " + " ".join(value for key, value in ALIASES.items() if key in query)
        terms = tokens(expanded) - STOPWORDS
        scored = []
        for identifier, document in self.documents.items():
            if document.get("kind") == "study_metadata":
                continue
            studies = document.get("studyIds") or document.get("study_ids") or []
            if allowed is not None and not allowed.intersection(studies):
                continue
            # Offline source hydration must not silently change established
            # retrieval scores. The builder snapshots the pre-hydration fields.
            ranking_text = document.get("ranking_metadata_text")
            haystack = tokens(ranking_text if isinstance(ranking_text, str) else
                              " ".join(str(document.get(k, "")) for k in ("title", "abstract", "searchKeyphrases", "topics")))
            matched = sorted(terms & haystack)
            if matched:
                scored.append((len(matched), identifier, matched, document))
            else:
                # Reviewed aliases only recover otherwise absent matches. They
                # never change the relative order of original positive hits.
                aliases = sorted(terms & tokens(" ".join(document.get("reviewed_search_terms", []))))
                if aliases:
                    scored.append((0.5, identifier, aliases, document))
        scored.sort(key=lambda row: (-row[0], row[1]))
        rows = []
        for rank, (score, _, matched, document) in enumerate(scored[:limit], 1):
            row = deepcopy(document)
            row.update(rank=rank, score=score, matched_terms=matched)
            rows.append(row)
        return {"documents": rows, "query": query.strip(), "search_mode": "explicit_lexical_augmented_corpus",
                "ranking_method": "Original metadata token overlap; descending match count, then document ID. Reviewed source aliases recover zero-overlap hits below original positive hits. Study landing pages remain in scene navigation. Scene context only filters explicit study links.",
                "eligible_corpus_size": len(self.documents), "no_unrelated_fallback": True,
                "training_performed": False, "live_generation": False}

    @staticmethod
    def _ranked_rows(response):
        if not isinstance(response, dict):
            raise ValueError("A ranked response object is required")
        for key in ("documents", "studies", "results"):
            if isinstance(response.get(key), list):
                rows = []
                for item in response[key]:
                    if not isinstance(item, dict):
                        raise ValueError("Ranked rows must be objects")
                    document = item.get("document") if isinstance(item.get("document"), dict) else item
                    identifier = item.get("id") or document.get("id")
                    if not isinstance(identifier, str) or not identifier:
                        raise ValueError("Ranked document identity is missing")
                    rows.append((identifier, document, item.get("score")))
                return rows
        raise ValueError("No ranked documents/studies/results list was supplied")

    def get_chart(self, identifier):
        if identifier not in self.charts:
            raise KeyError(identifier)
        return clean(self.charts[identifier])

    def chart_metadata(self, identifier):
        chart = self.get_chart(identifier)
        fields = ("id", "title", "family", "quantity", "x_label", "y_label", "description", "model_type",
                  "evidence_status", "evidence_label", "limitations", "r2", "formal_acceptance_score", "sources")
        return {key: chart[key] for key in fields if key in chart}

    def enrich(self, response, *, context=None):
        """Keep every returned paper in its actual order; attach typed evidence."""
        context = clean(context or {})
        ordered = self._ranked_rows(response)
        result_documents, selected_chart_ids, selected_chart_set = [], [], set()
        for ordinal, (identifier, ranked, score) in enumerate(ordered, 1):
            canonical = self.documents.get(identifier, {})
            # A reused ID with a conflicting explicit DOI cannot inherit evidence.
            ranked_doi = normalize_doi(ranked.get("doi") or ranked.get("doiUrl") or ranked.get("source_url"))
            stored_doi = normalize_doi(canonical.get("doi") or canonical.get("doiUrl"))
            conflict = bool(ranked_doi and stored_doi and ranked_doi != stored_doi)
            if conflict:
                canonical = {}
            bindings = [] if conflict else sorted(self.bindings.get(identifier, []),
                key=lambda b: ({"direct_source": 0, "related_work": 1, "related_psi": 2}[b["relationship"]], b.get("priority", 100)))
            evidence, insights, chart_ids, chart_bindings = [], [], [], []
            used_finding_ids, used_evidence, used_insights = set(), set(), set()
            for binding in bindings:
                relation = binding["relationship"]
                for fid in binding.get("finding_ids", []):
                    if fid in used_finding_ids:
                        continue
                    used_finding_ids.add(fid)
                    finding = deepcopy(self.findings[fid])
                    finding.update(relationship=relation, binding_reason=binding["reason"])
                    evidence_key = (finding.get("text"), relation, finding.get("source_id"))
                    if evidence_key not in used_evidence:
                        used_evidence.add(evidence_key)
                        evidence.append(clean(finding))
                    for insight in finding.get("fire_insights", []):
                        key = (insight.get("pillar"), insight.get("claim"), relation)
                        if key not in used_insights:
                            used_insights.add(key)
                            insights.append({**clean(insight), "finding_id": fid, "relationship": relation})
                for cid in binding.get("chart_ids", []):
                    if cid not in chart_ids:
                        chart_ids.append(cid)
                        chart_bindings.append({"chart_id": cid, "relationship": relation, "reason": binding["reason"],
                                               "source_locator": binding["source_locator"]})
                    if cid not in selected_chart_set:
                        selected_chart_set.add(cid); selected_chart_ids.append(cid)
                    for insight in self.charts[cid].get("fire_insights", []):
                        key = (insight.get("pillar"), insight.get("claim"), relation)
                        if key not in used_insights:
                            used_insights.add(key)
                            insights.append({**clean(insight), "chart_id": cid, "relationship": relation})
            exact = [e for e in evidence if e["relationship"] == "direct_source"]
            related = [e for e in evidence if e["relationship"] != "direct_source"]
            abstract = ranked.get("abstract") if isinstance(ranked.get("abstract"), str) else canonical.get("abstract")
            physical = [e for e in exact if e.get("summary_role") == "reviewed_physical_outcome"]
            source_brief = canonical.get("reviewed_summary")
            if isinstance(source_brief, dict) and source_brief.get("text") and source_brief.get("source_locator") and source_brief.get("relationship") in RELATIONSHIPS:
                summary = source_brief["text"]
                summary_method = source_brief.get("method", "reviewed_source_insights")
            elif physical:
                summary = physical[0].get("text")
                summary_method = "reviewed_physical_outcome"
            elif isinstance(abstract, str) and abstract.strip():
                summary = " ".join(re.split(r"(?<=[.!?])\s+", abstract.strip())[-2:])
                summary_method = "abstract_extract"
            elif exact:
                summary = exact[0].get("text") or exact[0].get("title")
                summary_method = "reviewed_note"
            elif related:
                summary = "Related source evidence, not a result attributed to this paper: " + str(related[0].get("text") or related[0].get("title"))
                summary_method = "related_reviewed_note"
            else:
                summary = "No reviewed quantitative finding is explicitly bound to this source. Open its abstract and inspect the study conditions."
                summary_method = "not_available"
            studies = deepcopy(ranked.get("study_ids") or ranked.get("studyIds") or canonical.get("studyIds") or [])
            nasa_links = ranked.get("nasaDataLinks") or canonical.get("nasaDataLinks") or []
            data_url = next((public_url(v) for v in nasa_links if public_url(v)), None)
            if not data_url:
                known_study = next((s for s in studies if re.fullmatch(r"PSI-[0-9]+", s)), None)
                if known_study:
                    data_url = "https://psi.nasa.gov/physci/repo/data/investigations/" + known_study
            source_url = source_link(ranked.get("source_url")) or source_link(ranked.get("doiUrl")) or source_link(ranked.get("sourceUrl")) or source_link(canonical.get("doiUrl")) or source_link(canonical.get("sourceUrl")) or source_link(canonical.get("fulltext_url"))
            doc = {"id": identifier, "title": ranked.get("title") or canonical.get("title") or identifier,
                   "doi": ranked_doi or stored_doi, "source_url": source_url,
                   "abstract": abstract if isinstance(abstract, str) and abstract.strip() else None,
                   "abstract_status": canonical.get("abstractStatus") or ranked.get("abstract_status"),
                   "abstract_role": canonical.get("abstractRole"), "rank": ordinal,
                   "study_ids": studies, "year": ranked.get("year") or canonical.get("year"), "kind": canonical.get("kind") or ranked.get("kind"),
                   "matched_terms": deepcopy(ranked.get("matched_terms") or []), "data_url": data_url,
                   "match_reason": "; ".join(dict.fromkeys(b["reason"] for b in bindings)) if bindings else ("Conflicting paper identity; enrichment withheld." if conflict else "No explicit reviewed source binding."),
                   "summary": summary, "summary_method": summary_method, "evidence": evidence, "insights": insights, "chart_ids": chart_ids,
                   "chart_bindings": chart_bindings, "binding_status": "identity_conflict" if conflict else "mapped" if bindings else "unmapped",
                   "metadata_origin": canonical.get("metadata_origin", "existing_literature_corpus"),
                   "ranking_score": score, "ranking_score_is_safety": False,
                   "fulltext_url": source_link(canonical.get("fulltext_url")),
                   "chart_links": [{"chart_id": c["chart_id"], "relationship": c["relationship"]} for c in chart_bindings]}
            if isinstance(source_brief, dict) and not conflict:
                doc["summary_provenance"] = clean(source_brief)
            diagram = canonical.get("diagram")
            if isinstance(diagram, dict) and diagram.get("kind") in {"solid", "smoke", "droplet", "jet", "sphere", "disk"} and diagram.get("source_locator"):
                doc["diagram"] = clean(diagram)
            result_documents.append(clean(doc))
        lines = []
        seen = set()
        for doc in result_documents:
            if doc["evidence"] and doc["summary"] not in seen:
                seen.add(doc["summary"]); lines.append(doc["summary"])
            if len(lines) == 3:
                break
        limits = ["Reviewed-source navigation does not establish the safety of the selected habitat, material or device.",
                  "The selected scene does not apply measured pressure, oxygen, gravity or operating presets."]
        if context.get("habitat") in {"lunar_base", "mars_base"} or context.get("habitat") == "pressurized_rover":
            limits.append("These source links do not establish validated partial-gravity predictions.")
        return {"schema_version": "scene-evidence-search-v1", "documents": result_documents,
                "charts": [self.chart_metadata(cid) for cid in selected_chart_ids],
                "summary": {"method": "reviewed_notes_selection", "label": "Reviewed evidence summary", "generated": False,
                            "text": " ".join(lines) if lines else "No explicitly reviewed evidence is bound to the returned sources.", "limits": limits},
                "context": context, "query": response.get("query") or context.get("query"),
                "search_mode": response.get("search_mode") or "upstream_ranked_response",
                "provenance": {"ranking_preserved": True, "returned_order": [i for i, _, _ in ordered],
                               "mapping_method": "Explicit document/source and reviewed study IDs; no title-similarity binding.",
                               "live_generation": False, "training_performed": False, "numerical_model_executed": False},
                "safety": {"status": "Unknown", "engineering_approved": False}}


def enrich(response, catalog, *, context=None):
    return ReviewedEvidenceBridge(catalog).enrich(response, context=context)
