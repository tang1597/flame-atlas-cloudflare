"""Qualitative navigation bridge; no files, models or experiments are joined."""
from copy import deepcopy
import re
from urllib.parse import urlencode, urlsplit


VERSION = "1.0.0"
CASE_ID = re.compile(r"R0[1-7](?:-[A-Za-z0-9_.-]+)?\Z")
CI_VIEW_MAP = {
    "CI01": ("R01",), "CI02": ("R01", "R02"),
    "CI03": ("R03", "R01"), "CI04": ("R02", "R05"),
    "CI05": ("gas_guidance", "R03"), "CI06": ("R02", "R06"),
    "CI07": ("R07", "R01"), "CI08": ("spice_search", "R01"),
}


def _records(items, name):
    if not isinstance(items, list):
        raise ValueError(f"Atlas {name} registry must be a list")
    result = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or item["id"] in result:
            raise ValueError(f"Atlas {name} identities are missing or duplicated")
        result[item["id"]] = item
    return result


def _study_ids(value):
    if not isinstance(value, list) or any(not isinstance(i, str) for i in value):
        raise ValueError("Study identities must be explicitly supplied strings")
    return list(dict.fromkeys(value))


def _official_catalog_url(value, study_id):
    if not isinstance(value, str) or any(ord(c) < 32 for c in value):
        return None
    try:
        url = urlsplit(value)
        if (url.scheme == "https" and url.hostname == "psi.nasa.gov"
                and not url.username and not url.password
                and url.path.rstrip("/") == "/physci/repo/data/investigations/" + study_id):
            return value
    except ValueError:
        pass
    return None


def attach_evidence_links(atlas_payload, strategy_payload):
    """Return a deep copy with main's explicit CI-to-existing-view navigation.

    Source-study intersection describes navigation coverage only. It cannot
    identify a matched experiment, reproduce the CI calculation, qualify a
    product or establish full source coverage. Original CI identities/classes
    and graph relationships remain unchanged.
    """
    if (not isinstance(atlas_payload, dict)
            or atlas_payload.get("schema_version") != "habitat-fire-atlas-api/1.0"
            or atlas_payload.get("status") != "reviewed_qualitative_navigation_mapping"):
        raise ValueError("A reviewed public habitat-atlas payload is required")
    public = deepcopy(atlas_payload)
    datasets = _records(public.get("datasets"), "dataset")
    sources = _records(public.get("sources"), "source")
    insights = _records(public.get("insights"), "insight")
    reviewed_strategies = (isinstance(strategy_payload, dict)
        and strategy_payload.get("schema_version") == "fire-strategy-catalog/1.0"
        and strategy_payload.get("status") == "reviewed_for_research"
        and strategy_payload.get("preview") is not True)
    cases = _records(strategy_payload.get("cases"), "strategy") if reviewed_strategies else {}
    canonical = {}
    for prefix in {item for targets in CI_VIEW_MAP.values() for item in targets if item.startswith("R")}:
        matches = [case for cid, case in cases.items()
                   if CASE_ID.fullmatch(cid) and (cid == prefix or cid.startswith(prefix + "-"))]
        # An ambiguous/stale family never silently chooses the first case.
        if len(matches) == 1:
            canonical[prefix] = matches[0]
    for iid, insight in insights.items():
        if iid not in CI_VIEW_MAP:
            continue
        source_ids = _study_ids(insight.get("source_psi_ids"))
        original_refs = _study_ids(insight.get("source_ids", []))
        insight["source_ids"] = original_refs + [sid for sid in source_ids
            if sid in sources and sid not in original_refs]
        links = deepcopy(insight.get("deep_links", []))
        if not isinstance(links, list):
            raise ValueError("Insight deep links must be a list")
        existing_urls = {link.get("url") for link in links if isinstance(link, dict)}
        intersections, comparison_only, missing, official_ids = {}, [], [], []
        def append(link):
            if link["url"] not in existing_urls:
                links.append(link)
                existing_urls.add(link["url"])
        for target in CI_VIEW_MAP[iid]:
            if target == "gas_guidance":
                append({"label": "Gas-isolation guidance context", "url": "/gas-case.html",
                    "kind": "guidance_context", "source_study_intersection": [],
                    "scope_note": "Official-guidance and related-mechanism context only; not BRE gas-leak, flashback or shutdown-performance validation."})
                continue
            if target == "spice_search":
                append({"label": "Search reviewed SPICE literature", "url": "/index.html?" + urlencode({"q": "SPICE"}),
                    "kind": "literature_search", "source_study_intersection": [],
                    "scope_note": "Literature navigation only; search results do not establish source completeness, a physical match or validation."})
                continue
            case = canonical.get(target)
            if case is None:
                missing.append(target)
                continue
            studies = _study_ids(case.get("investigations", []))
            overlap = [sid for sid in source_ids if sid in studies]
            intersections[case["id"]] = overlap
            if not overlap:
                comparison_only.append(case["id"])
            append({"label": "Review related evidence — " + target,
                "url": "/strategies.html?" + urlencode({"case": case["id"]}),
                "kind": "reviewed_case", "case_id": case["id"],
                "source_study_intersection": overlap,
                "scope_note": ("Related reviewed view sharing the listed study identities; selected records do not establish full CI source coverage or a matched joint experiment."
                    if overlap else "Related comparative view only; its declared studies do not intersect this insight's source studies. It is not a direct source for this CI.")})
        for sid in source_ids:
            dataset = datasets.get(sid)
            url = _official_catalog_url(dataset.get("nasa_url"), sid) if dataset else None
            if url:
                official_ids.append(sid)
                append({"label": "NASA " + sid + " catalog", "url": url,
                    "kind": "official_psi_catalog", "study_id": sid,
                    "scope_note": "Official study identity/catalog page; not an exact paper, trial or quantitative reproduction locator."})
        represented = {sid for overlap in intersections.values() for sid in overlap}
        insight["deep_links"] = links
        insight["source_coverage"] = {
            "role": "qualitative_navigation_only", "full_source_coverage": "not_established",
            "local_view_study_intersections": intersections,
            "ci_sources_without_local_study_match": [sid for sid in source_ids if sid not in represented],
            "related_comparative_case_ids": comparison_only,
            "official_catalog_link_ids": official_ids, "unavailable_requested_views": missing,
            "reviewed_strategy_payload_available": bool(reviewed_strategies),
            "scope_note": "Navigation availability does not merge experiments, reproduce the complete cross-source analysis, identify a joint effect or validate a product/target habitat.",
        }
    public["evidence_navigation"] = {"version": VERSION,
        "role": "Main-authored qualitative links to existing views and official catalog identities.",
        "full_source_coverage": "not_established", "experiments_merged": False}
    return public
