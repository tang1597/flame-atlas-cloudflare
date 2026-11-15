"""Read-only adapter for an explicitly configured, reviewed strategy catalog.

No catalog, model, source PDF or network connection is opened at import time.
The input may contain offline provenance paths; only the public field allowlist
is returned. This adapter checks display/provenance structure, not the truth of
a paper's findings or the safety of an intervention.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


VERSION = "1.1.0"
ID = re.compile(r"[A-Za-z0-9_.-]{1,160}\Z")
MANIFEST_ID = re.compile(r"[A-Za-z0-9_-]{1,120}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
EVIDENCE_KINDS = frozenset({
    "observation", "author_conclusion", "physical_inference",
    "product_hypothesis", "official_guidance", "model_inference",
})
MEASUREMENTS = frozenset({"direct", "source_reduced", "source_reported"})
RUBRIC_CRITERIA = frozenset({
    "raw_data", "source_traceability", "NASA_intervention_evidence",
    "earth_comparison", "fire_relevance",
})
EDITORIAL_FIELDS = frozenset({"score_breakdown", "scoring_method", "main_selection"})
TOP_FIELDS = (
    "schema_version", "status", "selected_case_id", "ranking_method",
    "selection", "title", "title_en", "summary", "summary_en", "limits",
    "science_gate", "scope", "data_status", "updated_at", "language",
    "main_selection", "scoring_method",
)
CASE_FIELDS = (
    "id", "title_en", "title_zh", "rank", "rank_reasons", "summary_en",
    "pillar", "strategy", "product_concept", "investigations",
    "earth_comparison", "supported_claims", "unsupported_claims",
    "next_validation", "limits", "keywords", "tags", "conditions",
    "display_safety_status", "safety_status_basis", "selection_reason",
    "related_concepts", "evidence_score", "score_max", "score_breakdown", "ranking_basis",
    "source_case_ids", "gas_case_url",
    "summary_zh", "short_summary", "fire_question", "fire_question_en", "fire_question_zh",
    "key_terms", "authored_key_terms", "search_terms",
)
REQUIRED_CASE = (
    "id", "title_en", "title_zh", "rank", "rank_reasons", "pillar",
    "strategy", "product_concept", "investigations", "evidence",
    "literature", "earth_comparison", "supported_claims",
    "unsupported_claims", "next_validation",
)
SOURCE_FIELDS = (
    "id", "manifest_id", "title", "authors", "year", "authority", "kind",
    "role", "url", "doi", "edition", "sha256", "pdf_page",
    "source_locator", "access", "scope", "limits", "direct_page_links",
    "fulltext_status", "version_id", "ntrs_id",
)
EVIDENCE_FIELDS = (
    "id", "kind", "statement", "source_ids", "source_locator",
    "measurement_kind", "value", "unit", "investigation_id", "trial_id",
    "physical_generation_id", "record_id", "fraction", "label", "conditions",
    "denominator", "uncertainty", "observation_form", "independent_events",
    "limits", "x_value", "x_unit", "measurement_kind_detail",
)
LITERATURE_FIELDS = (
    "id", "source_id", "title", "url", "doi", "edition", "source_locator",
    "paraphrase", "short_quote", "quote_role", "limits",
)
CHART_FIELDS = (
    "kind", "title", "data_status", "x_type", "x_label", "x_unit",
    "x_definition", "y_label", "y_unit", "y_definition", "caption", "limits",
)
PRIVATE_KEYS = frozenset({
    "path", "paths", "local_pdf", "local_pdf_url", "raw", "raw_data",
    "raw_records", "raw_rows", "weights", "model_weights", "training_data",
    "fitted_model", "source_payload", "private", "credentials",
    "local_file", "raw_file", "raw_files", "source_file", "filepath",
})
PATH_TEXT = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s\"<>]*"
    r"|\\\\[^\s\\]+\\[^\s\"<>]*"
    r"|file://[^\s\"<>]*"
    r"|(?<![A-Za-z0-9:])/(?:Users|home|mnt|tmp|workspace|private|var)/[^\s\"<>]*",
    re.IGNORECASE,
)
STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "how", "i", "in", "is", "it", "of", "on", "or", "the", "to",
    "what", "when", "with", "this", "that", "these", "those", "we", "its", "our",
    "should", "could", "would", "can", "do", "does", "did", "was", "were", "has",
    "have", "had", "will", "not", "no", "yes", "if", "then", "than", "but", "yet",
    "also", "only", "all", "any", "each", "one", "two", "same", "different",
    "which", "where", "why", "who", "inside", "normally", "decide", "early", "part",
    "nasa", "iss", "space", "spacecraft", "cabin", "crew", "habitat", "lunar",
    "moon", "mars", "martian", "earth", "ground", "flight", "terrestrial", "microgravity",
    "fire", "flame", "flames", "combustion", "safety", "safe", "unsafe", "hazard",
    "hazards", "evidence", "source", "sources", "data", "record", "records", "research",
    "study", "studies", "experiment", "experiments", "test", "tests", "tested", "testing",
    "result", "results", "reported", "used", "using", "use", "support", "supports",
    "show", "shown", "design", "planning", "evaluate", "evaluation", "verify", "verification",
    "validation", "validated", "unvalidated", "known", "unknown", "relevant", "specified",
    "complete", "completely", "measured", "measurement", "measurements", "material", "materials",
    "property", "properties", "condition", "conditions", "environment", "environments",
    "bounded", "separate", "distinct", "additional", "related", "provide", "provides", "psi", "ii", "iii",
    "help", "based", "actual", "local", "new", "readout", "setting", "settings",
    "火焰", "消防", "火災", "安全", "太空", "地面", "證據", "資料", "研究", "測試",
    "宇宙", "載人", "環境", "如何", "怎麼", "什麼", "可能", "可以", "是否", "能否",
    "應該", "還能", "使用", "代表", "支持", "設計", "這些", "這個", "提供", "模型",
    "來源", "進行", "系統", "完全", "完整", "危害", "結果", "材料", "驗證",
})
CJK_RUNS = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+")
WORD_FORMS = {
    "detector": "detect", "detectors": "detect", "detection": "detect",
    "particles": "particle", "sensors": "sensor", "instruments": "instrument",
    "sampling": "sample", "samples": "sample", "fractions": "fraction",
    "droplets": "droplet", "mixtures": "mixture", "fields": "field",
    "outcomes": "outcome", "responses": "response", "sizes": "size",
    "ageing": "aging",
}
MATCH_FIELDS = (
    "title_en", "title_zh", "title", "summary_en", "summary_zh", "short_summary",
    "fire_question", "fire_question_en", "fire_question_zh", "keywords", "tags",
    "key_terms", "authored_key_terms", "search_terms", "investigations",
)
SCOPE_PATTERNS = (
    # Adapted from the existing evidence_search.py explicit scope exclusion;
    # no retriever/model import is necessary for this fixed lexical boundary.
    re.compile(r"\brocket[\s-]+(?:engine|motor|propellant|fuel|nozzle)\b", re.I),
    re.compile(r"\bpropellant[\s-]+(?:fire|tank|suppression|dose|combustion)\b", re.I),
    re.compile(r"\b(?:retropropulsion|reverse[\s-]+thrust)\b", re.I),
    re.compile(r"火箭(?:引擎|發動機|发动机|推進劑|推进剂|燃料|噴嘴|喷嘴)"),
    re.compile(r"(?:推進劑|推进剂)(?:火災|火灾|燃燒|燃烧|滅火|灭火|劑量|剂量|儲箱|储箱|贮箱)"),
    re.compile(r"(?:反向|逆向)(?:助推|推進|推进)"),
)


class CatalogUnavailable(ValueError):
    """Missing or invalid reviewed input; suitable for a public HTTP 503."""


class CaseNotFound(KeyError):
    """A requested case is absent; suitable for HTTP 404."""


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _identifier(value):
    return isinstance(value, str) and bool(ID.fullmatch(value))


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def _positive_integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _public_url(value):
    if not isinstance(value, str) or any(ord(char) < 32 for char in value):
        return None
    try:
        url = urlsplit(value)
        if url.scheme in {"http", "https"} and url.hostname and not url.username and not url.password:
            return value
    except ValueError:
        pass
    return None


def _private_key(key):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(key)).lower().replace("-", "_")
    return (name in PRIVATE_KEYS or name.startswith("private_")
            or name.endswith(("_path", "_paths", "_weights")))


def _sanitize(value):
    """Drop offline-only keys recursively without discarding a valid catalog."""
    if isinstance(value, dict):
        return {key: (_public_url(child) if str(key).lower() in {
            "url", "href", "official_url", "source_url", "direct_url",
        } else _sanitize(child)) for key, child in value.items() if not _private_key(key)}
    if isinstance(value, list):
        return [_sanitize(child) for child in value]
    if isinstance(value, str):
        if value.lstrip().lower().startswith(("javascript:", "data:", "file:")):
            return None
        if not _public_url(value) and re.search(
                r"(?:^|\s)(?:\.{1,2}[\\/]|[\w.-]+[\\/])[^\s]*"
                r"\.(?:csv|tsv|xlsx?|parquet|pkl|pickle|pt|pth|bin|safetensors)(?:$|\s)", value,
                re.IGNORECASE):
            return "[private file reference withheld]"
        return PATH_TEXT.sub("[private file reference withheld]", value)
    if value is None or isinstance(value, (bool, int, float)):
        return value if not isinstance(value, float) or math.isfinite(value) else None
    return None


def _editorial_metadata(value):
    """Keep the named raw_data rubric criterion, not an experimental payload.

    The same word also names private datasets elsewhere. Only a rubric text,
    score/null, or bounded score object is accepted in this metadata context.
    Numeric editorial weights are metadata; executable/model weights are not.
    """
    if isinstance(value, list):
        return [_editorial_metadata(child) for child in value]
    if not isinstance(value, dict):
        return _sanitize(value)
    public = {}
    for key, child in value.items():
        if key == "raw_data":
            score = child.get("score") if isinstance(child, dict) else child
            rubric_labels = (isinstance(child, dict) and bool(child)
                             and set(child).issubset({"0", "1", "2", "3"})
                             and all(isinstance(label, str) for label in child.values()))
            if (isinstance(child, str) or child is None
                    or rubric_labels or (_finite(score) and 0 <= score <= 3)):
                public[key] = _editorial_metadata(child)
        elif key == "weights":
            if (isinstance(child, dict) and set(child).issubset(RUBRIC_CRITERIA)
                    and all(_finite(item) and item >= 0 for item in child.values())):
                public[key] = deepcopy(child)
        elif not _private_key(key):
            public[key] = _editorial_metadata(child)
    return public


def _project(value, fields):
    return {key: (_editorial_metadata(deepcopy(value[key])) if key in EDITORIAL_FIELDS
                  else _sanitize(deepcopy(value[key]))) for key in fields if key in value}


def _refs(value, known, label):
    if not isinstance(value, list) or any(not isinstance(item, str) or item not in known for item in value):
        raise CatalogUnavailable(f"Invalid {label} source references")


def _locator_present(value):
    if isinstance(value, str):
        return _nonempty(value)
    if not isinstance(value, dict):
        return False
    return any(value.get(key) not in (None, "", []) for key in (
        "pdf_page", "section", "sheet", "row", "cells", "figure", "table", "equation",
    ))


def _related_refs(value, source_ids, evidence_ids):
    """Validate explicit references without treating unknown/null as an ID.

    Origin source_case_ids belong to the supplied editorial source-card registry,
    not necessarily the final ranked-family IDs. They are kept as origin labels.
    """
    if isinstance(value, list):
        for child in value:
            _related_refs(child, source_ids, evidence_ids)
    elif isinstance(value, dict):
        for key, child in value.items():
            if key == "source_ids" and child is not None:
                _refs(child, source_ids, "related-concept")
            elif key == "source_id" and child is not None:
                if not isinstance(child, str) or child not in source_ids:
                    raise CatalogUnavailable("Related concept references an unknown source")
            elif key in {"evidence_id", "evidence_ids"} and child is not None:
                refs = [child] if key == "evidence_id" else child
                if (not isinstance(refs, list)
                        or any(not isinstance(ref, str) or ref not in evidence_ids for ref in refs)):
                    raise CatalogUnavailable("Related concept references unknown evidence")
            elif key == "source_case_ids" and child is not None:
                if not isinstance(child, list) or any(not _nonempty(ref) for ref in child):
                    raise CatalogUnavailable("Origin source-case identities must be text labels")
            _related_refs(child, source_ids, evidence_ids)


def _nested_evidence_ids(value):
    found = set()
    if isinstance(value, list):
        for child in value:
            found.update(_nested_evidence_ids(child))
    elif isinstance(value, dict):
        entries = value.get("evidence", [])
        if isinstance(entries, list):
            found.update(item["id"] for item in entries
                         if isinstance(item, dict) and _identifier(item.get("id")))
        for child in value.values():
            found.update(_nested_evidence_ids(child))
    return found


def _validate(document, review_mode=False):
    if not isinstance(document, dict) or document.get("schema_version") != "fire-strategy-catalog/1.0":
        raise CatalogUnavailable("Unsupported strategy catalog schema")
    status = document.get("status")
    if status != "reviewed_for_research" and not (review_mode is True and status == "pending_main_review"):
        raise CatalogUnavailable("A reviewed catalog or explicitly enabled pending-review preview is required; examples are unavailable")
    if not _nonempty(document.get("ranking_method")):
        raise CatalogUnavailable("Main-authored ranking method is required")
    sources = document.get("sources")
    cases = document.get("cases")
    if not isinstance(sources, list) or not isinstance(cases, list) or not cases:
        raise CatalogUnavailable("Strategy cases and source lists are required")
    source_ids = set()
    for source in sources:
        if not isinstance(source, dict) or not _identifier(source.get("id")) or source["id"] in source_ids:
            raise CatalogUnavailable("Invalid or duplicate source identity")
        if not _nonempty(source.get("title")) or not _nonempty(source.get("edition")):
            raise CatalogUnavailable("Source title and edition are required")
        digest = source.get("sha256")
        if digest is not None and (not isinstance(digest, str) or not SHA256.fullmatch(digest)):
            raise CatalogUnavailable("Invalid source SHA metadata")
        page = source.get("pdf_page")
        if page is not None and not _positive_integer(page):
            raise CatalogUnavailable("Source PDF page must be a positive integer or null")
        source_ids.add(source["id"])
    case_ids = set()
    for case in cases:
        if not isinstance(case, dict) or any(field not in case for field in REQUIRED_CASE):
            raise CatalogUnavailable("Incomplete strategy case")
        if not _identifier(case["id"]) or case["id"] in case_ids:
            raise CatalogUnavailable("Invalid or duplicate case identity")
        if not _positive_integer(case["rank"]):
            raise CatalogUnavailable("Case priority must be a positive main-authored integer")
        if any(not isinstance(case.get(field), str) for field in ("title_en", "title_zh", "strategy", "product_concept")):
            raise CatalogUnavailable("Case titles, strategy and product concept must be text")
        if any(not isinstance(case.get(field), list) for field in (
            "rank_reasons", "investigations", "evidence", "literature", "supported_claims",
            "unsupported_claims", "next_validation",
        )):
            raise CatalogUnavailable("Invalid strategy case list fields")
        if not isinstance(case["earth_comparison"], dict):
            raise CatalogUnavailable("Earth comparison must retain its typed scope")
        _refs(case["earth_comparison"].get("source_ids", []), source_ids, "Earth comparison")
        evidence_ids = set()
        for item in case["evidence"]:
            if (not isinstance(item, dict) or not _identifier(item.get("id"))
                    or item["id"] in evidence_ids or item.get("kind") not in EVIDENCE_KINDS
                    or not _nonempty(item.get("statement"))):
                raise CatalogUnavailable("Invalid evidence identity, role or statement")
            _refs(item.get("source_ids"), source_ids, "evidence")
            evidence_ids.add(item["id"])
        for item in case["literature"]:
            if not isinstance(item, dict) or item.get("source_id") not in source_ids:
                raise CatalogUnavailable("Literature must resolve to an exact source identity")
        for claim in case["supported_claims"]:
            if isinstance(claim, dict):
                if claim.get("kind") not in EVIDENCE_KINDS:
                    raise CatalogUnavailable("Supported claim must preserve its evidence role")
                _refs(claim.get("source_ids", []), source_ids, "claim")
        if "source_case_ids" in case:
            refs = case["source_case_ids"]
            if not isinstance(refs, list) or any(not _nonempty(ref) for ref in refs):
                raise CatalogUnavailable("Origin source-case identities must be text labels")
        related = case.get("related_concepts", [])
        if not isinstance(related, list):
            raise CatalogUnavailable("Related concepts must remain a list")
        _related_refs(related, source_ids, evidence_ids | _nested_evidence_ids(related))
        case_ids.add(case["id"])
    if document.get("selected_case_id") not in case_ids:
        raise CatalogUnavailable("Main-selected case is missing from the catalog")
    return document


def _manifest_entries(manifest):
    if not isinstance(manifest, dict):
        return {}
    entries = manifest.get("sources", manifest)
    return entries if isinstance(entries, dict) else {}


def _source_projection(source, entries, port):
    public = _project(source, SOURCE_FIELDS)
    public["url"] = _public_url(source.get("url"))
    public["local_pdf_url"] = None
    manifest_id = source.get("manifest_id") or source["id"]
    entry = entries.get(manifest_id) if isinstance(manifest_id, str) else None
    digest = source.get("sha256")
    if (isinstance(manifest_id, str) and MANIFEST_ID.fullmatch(manifest_id)
            and isinstance(digest, str) and SHA256.fullmatch(digest)
            and isinstance(entry, dict) and entry.get("sha256") == digest
            and isinstance(entry.get("path"), (str, Path))
            and Path(entry["path"]).suffix.lower() == ".pdf"):
        page = source.get("pdf_page")
        fragment = f"#page={page}" if _positive_integer(page) else ""
        public["local_pdf_url"] = f"http://127.0.0.1:{port}/sources/{manifest_id}.pdf{fragment}"
    return public


def _chart_projection(case):
    """Fail closed for a chart, preserving the case and sourced observations."""
    raw = case.get("chart")
    if raw is None:
        return None, "not_supplied", "No observed-data chart was supplied."
    if not isinstance(raw, dict):
        return None, "unavailable", "Observed-data chart has an unsupported shape."
    if raw.get("kind") not in {"observed_points", "observed_series"}:
        return None, "unavailable", "Only supplied observations can be plotted."
    if raw.get("connect_points") is True:
        return None, "unavailable", "Connected or interpolated curves are not enabled."
    required_text = ("title", "x_label", "x_definition", "y_label", "y_definition", "y_unit")
    if any(not _nonempty(raw.get(field)) for field in required_text):
        return None, "unavailable", "Source-defined chart axes and units are incomplete."
    x_type = raw.get("x_type")
    if x_type not in {"linear", "ordinal", "categorical"} or "x_unit" not in raw:
        return None, "unavailable", "An explicit axis type and unit declaration are required."
    if x_type == "ordinal" and raw["x_unit"] is not None:
        return None, "unavailable", "Ordinal event order cannot be assigned elapsed-time units."
    series = raw.get("series")
    if not isinstance(series, list) or not series:
        return None, "unavailable", "No source observations were supplied for plotting."
    evidence = {item["id"]: item for item in case["evidence"]}
    result = _project(raw, CHART_FIELDS)
    result.update({"connect_points": False, "render_mode": "markers", "series": []})
    series_ids = set()
    for item in series:
        if (not isinstance(item, dict) or not _identifier(item.get("id"))
                or item["id"] in series_ids or not _nonempty(item.get("label"))
                or not _nonempty(item.get("investigation_id"))
                or not _nonempty(item.get("trial_id"))
                or not isinstance(item.get("points"), list) or not item["points"]):
            return None, "unavailable", "Each series needs a distinct source trial and supplied points."
        plotted = _project(item, (
            "id", "label", "investigation_id", "trial_id", "physical_generation_id",
            "measurement_kind", "conditions", "limits", "independent_events",
        ))
        plotted["points"] = []
        for point in item["points"]:
            if not isinstance(point, dict):
                return None, "unavailable", "An observed point is incomplete."
            x, y = point.get("x"), point.get("y")
            if not (_nonempty(x) if x_type == "categorical" else _finite(x)) or not _finite(y):
                return None, "unavailable", "Unknown or non-finite coordinates cannot be plotted or replaced by zero."
            obs = evidence.get(point.get("evidence_id"))
            if (not isinstance(obs, dict) or obs.get("kind") != "observation"
                    or obs.get("measurement_kind") not in MEASUREMENTS
                    or not obs.get("source_ids") or not _locator_present(obs.get("source_locator"))):
                return None, "unavailable", "A chart point must reference a located observation in this case."
            if obs.get("observation_form") in {"aggregate", "literature_aggregate", "pooled_summary"}:
                return None, "unavailable", "An aggregate summary cannot supply individual scatter points."
            if (not _finite(obs.get("value")) or y != obs["value"] or obs.get("unit") != raw["y_unit"]):
                return None, "unavailable", "Point values and units must match their referenced observations."
            same_trial = obs.get("trial_id") == item["trial_id"]
            generation = item.get("physical_generation_id")
            same_generation = _nonempty(generation) and obs.get("physical_generation_id") == generation
            if obs.get("investigation_id") != item["investigation_id"] or not (same_trial or same_generation):
                return None, "unavailable", "Independent trials cannot be combined into one observed series."
            plotted["points"].append(_project(point, ("x", "y", "evidence_id", "label")))
        result["series"].append(plotted)
        series_ids.add(item["id"])
    return result, "available", "Supplied observations only; no fitted or interpolated values."


def _case_projection(case):
    public = _project(case, CASE_FIELDS)
    if "gas_case_url" in public:
        link = case["gas_case_url"]
        # A supplied source-only case link may be an official URL or a clean
        # root-relative dashboard route; never a filesystem or script URL.
        relative = (isinstance(link, str) and link.startswith("/") and not link.startswith("//")
                    and not any(ord(char) < 32 for char in link)
                    and "\\" not in unquote(link)
                    and not any(part in {".", ".."} for part in unquote(urlsplit(link).path).split("/"))
                    and _sanitize(link) == link)
        public["gas_case_url"] = link if relative else _public_url(link)
    public["evidence"] = [_project(item, EVIDENCE_FIELDS) for item in case["evidence"]]
    public["literature"] = [_project(item, LITERATURE_FIELDS) for item in case["literature"]]
    for item in public["literature"]:
        if "url" in item:
            item["url"] = _public_url(item["url"])
    chart, state, reason = _chart_projection(case)
    public["chart"] = chart
    public["chart_status"] = {"state": state, "reason": reason}
    public["observation_table"] = [deepcopy(item) for item in public["evidence"]
                                   if item["kind"] == "observation"]
    return public


def _tokens(text):
    lowered = text.casefold()
    words = {WORD_FORMS.get(word, word) for word in re.findall(r"[^\W_]+", lowered, re.UNICODE)
             if word not in STOPWORDS and len(word) > 1 and any(char.isalpha() for char in word)}
    # Fixed overlapping Han bigrams handle unsegmented authored Chinese text.
    # No translation, learned tokenizer, synonyms, semantic score or reranking.
    for run in CJK_RUNS.findall(lowered):
        words.update(run[index:index + 2] for index in range(len(run) - 1)
                     if run[index:index + 2] not in STOPWORDS)
    return words - STOPWORDS


def _text_values(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _text_values(item)
    elif isinstance(value, dict):
        for key in ("label", "name", "title", "title_en", "title_zh", "term", "id"):
            if key in value:
                yield from _text_values(value[key])


def _case_topics(case):
    texts = []
    for field in MATCH_FIELDS:
        texts.extend(_text_values(case.get(field)))
    for concept in case.get("related_concepts", []):
        if isinstance(concept, dict):
            for field in MATCH_FIELDS:
                texts.extend(_text_values(concept.get(field)))
    return [text.replace("[private file reference withheld]", "") for text in texts]


def _authored_anchors(texts):
    anchors = set()
    for text in texts:
        # Study/material names already authored in the eligible case fields.
        # Ordinary title-case words are not inferred to be scientific aliases.
        for value in re.findall(r"(?<![A-Za-z0-9])([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)*)(?![A-Za-z0-9])", text):
            if value.casefold() not in STOPWORDS and value not in {"II", "III", "IV"}:
                anchors.add(value)
        # SAME is also an ordinary English word; use it as an anchor only when
        # the question preserves uppercase spelling or explicitly says SAME-R.
        if re.search(r"(?<![A-Za-z0-9])SAME(?![A-Za-z0-9])", text):
            anchors.add("SAME")
    return anchors


def _has_anchor(query, anchor):
    pattern = r"(?<![A-Za-z0-9])" + re.escape(anchor).replace(r"\-", r"[\s-]+") + r"(?![A-Za-z0-9])"
    return bool(re.search(pattern, query, 0 if anchor == "SAME" else re.I))


def _negated_scope_mention(query, start):
    prefix = re.split(r"[.;!?，；。！？\n]", query[:start])[-1][-110:]
    qualifiers = r"(?:(?:a|an|the|any|about|for|of|or|nor)\s+)*"
    if re.search(r"\b(?:not|no|excluding|exclude|without)\s+" + qualifiers + r"$", prefix, re.I):
        return True
    if re.search(r"\bnot\s+(?:asking|researching|discussing|studying|related)\s+(?:about|to)\s+" + qualifiers + r"$", prefix, re.I):
        return True
    if re.search(r"\b(?:not|no|excluding|without)\s+(?:(?:about|a|an|the)\s+)*rocket[\s-]+(?:engine|motor|propellant)\s+(?:or|nor|and)\s*$", prefix, re.I):
        return True
    if re.search(r"(?:不是|並非|并非|不涉及|不討論|不讨论|排除)火箭(?:引擎|發動機|发动机)(?:或|和|與|与)\s*$", prefix):
        return True
    return bool(re.search(r"(?:不是|並非|并非|不涉及|不討論|不讨论|不研究|不含|排除|非)(?:關於|关于)?\s*$", prefix))


def _outside_scope_terms(query):
    terms = []
    for pattern in SCOPE_PATTERNS:
        for match in pattern.finditer(query):
            if not _negated_scope_mention(query, match.start()) and match.group() not in terms:
                terms.append(match.group())
    return terms


def _match_cases(cases, query):
    if not query:
        return ([case["id"] for case in cases], {}, "catalog_browse", {
            "status": "not_classified", "message": "Browse the supplied research priorities. No question-specific applicability decision has been made.",
        })
    excluded = _outside_scope_terms(query)
    if excluded:
        return ([], {}, "outside_scope", {
            "status": "out_of_scope",
            "message": "Rocket-engine and propellant fire suppression are outside these reviewed crew-environment cases. The catalog cannot establish an engine agent, dose or operating procedure.",
            "matched_exclusion_terms": excluded,
        })
    topics = {case["id"]: _case_topics(case) for case in cases}
    anchors = {cid: sorted(term for term in _authored_anchors(texts) if _has_anchor(query, term))
               for cid, texts in topics.items()}
    if any(anchors.values()):
        matched = {cid: terms for cid, terms in anchors.items() if terms}
        basis = "explicit_authored_anchor"
    else:
        question_tokens = _tokens(query)
        matched = {cid: sorted(question_tokens.intersection(_tokens(" ".join(texts))))
                   for cid, texts in topics.items()}
        matched = {cid: terms for cid, terms in matched.items() if terms}
        basis = "case_specific_topic_terms" if matched else "no_authored_topic_match"
    ids = [case["id"] for case in cases if case["id"] in matched]
    scope = ({"status": "in_scope", "message": "The question matches authored topics in the reviewed crew-fire research. Physical applicability, product effectiveness and safety remain unestablished."}
             if ids else {"status": "not_classified", "message": "No case-specific authored topic match was found. Clarify the material, instrument, study or fire mechanism; no safety conclusion follows from an empty result."})
    return ids, matched, basis, scope


class StrategyCatalog:
    """An offline path is mandatory; there is no example or guessed fallback."""

    def __init__(self, catalog_path, review_mode=False):
        if not isinstance(review_mode, bool):
            raise ValueError("Review mode must be an explicit boolean")
        self.catalog_path = Path(catalog_path) if catalog_path else None
        self.review_mode = review_mode

    def _load(self):
        if self.catalog_path is None:
            raise CatalogUnavailable("Reviewed strategy catalog is not configured")
        try:
            payload = self.catalog_path.read_bytes()
            def reject_constant(_value):
                raise ValueError("Non-finite JSON number")
            document = json.loads(payload.decode("utf-8-sig"), parse_constant=reject_constant)
        except (OSError, UnicodeError, ValueError) as exc:
            raise CatalogUnavailable("Reviewed strategy catalog is unavailable or invalid") from exc
        return _validate(document, self.review_mode), hashlib.sha256(payload).hexdigest()

    def catalog(self, manifest, port, q=None):
        if not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535:
            raise ValueError("A valid loopback server port is required")
        if q is not None and not isinstance(q, str):
            raise ValueError("Query must be text")
        document, digest = self._load()
        public = _project(document, TOP_FIELDS)
        public["version"] = VERSION
        public["catalog_sha256"] = digest
        public["preview"] = self.review_mode
        public["review_mode"] = self.review_mode
        public["preview_notice"] = (
            "QA preview only; main review is pending. No release or safety approval is implied."
            if document["status"] == "pending_main_review" else
            "QA preview mode; source status is unchanged." if self.review_mode else None
        )
        entries = _manifest_entries(manifest)
        public["sources"] = [_source_projection(item, entries, port) for item in document["sources"]]
        # Stable sort preserves authored order for equal ranks; no renumbering.
        public["cases"] = [_case_projection(item) for item in sorted(document["cases"], key=lambda item: item["rank"])]
        query = _sanitize(q.strip()) if q else ""
        matching, terms, basis, scope = _match_cases(public["cases"], query)
        public.update({"query": query, "matching_case_ids": matching,
                       "match_method": "case_specific_authored_terms", "match_basis": basis,
                       "matched_authored_terms": terms, "query_scope": scope,
                       "match_tokenization": "Eligible authored titles, short summaries, fire questions and key terms only; fixed word forms and overlapping Han bigrams, generic words excluded. Explicit authored study/material anchors take precedence. No learned ranking.",
                       "match_role": "Research-topic navigation only; main-authored rank and selected flagship are unchanged. Topic matching is not physical applicability or safety approval."})
        return public

    def detail(self, case_id, manifest, port):
        document = self.catalog(manifest, port)
        for case in document["cases"]:
            if case["id"] == case_id:
                return {key: value for key, value in document.items() if key != "cases"} | {"case": case}
        raise CaseNotFound("Strategy case not found")


def catalog(catalog_path, manifest, port, q=None, *, review_mode=False):
    """Convenience entry point for a server with an explicit catalog option."""
    return StrategyCatalog(catalog_path, review_mode=review_mode).catalog(manifest, port, q)
