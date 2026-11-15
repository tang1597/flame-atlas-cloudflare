"""Read-only habitat/fire evidence navigation over explicitly reviewed inputs.

No input, PDF, model or network is accessed at import time. Relationship labels
and CI joins are authored data, never inferred from search words or habitats.
Only qualitative public fields and source-identity metadata are projected.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


VERSION = "1.0.0"
RELATIONSHIPS = frozenset({"direct", "analogue", "related", "hypothesis", "unknown"})
CI_IDS = frozenset(f"CI{i:02d}" for i in range(1, 9))
IDENTIFIER = re.compile(r"[A-Za-z0-9_.-]{1,160}\Z")
MANIFEST_ID = re.compile(r"[A-Za-z0-9_-]{1,120}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
TOP_FIELDS = ("title", "summary", "description", "defaults", "limits", "scope", "fire_types_are_mutually_exclusive")
HABITAT_FIELDS = (
    "id", "title", "label", "context", "description", "interior_context",
    "gravity_context", "gravity_evidence", "world_contexts", "limits", "unknowns",
    "source_ids", "fire_type_ids", "insight_ids", "relation_ids", "deep_links",
)
FIRE_FIELDS = ("id", "title", "label", "description", "context", "limits", "source_ids", "deep_links")
DATASET_FIELDS = (
    "id", "title", "name", "summary", "description", "study_ids", "investigation_ids",
    "architecture", "scope", "source_ids", "insight_ids", "deep_links", "limits",
    "unknowns", "readiness", "evidence_roles",
)
RELATION_FIELDS = (
    "id", "habitat_id", "fire_type_id", "dataset_id", "relationship", "statement",
    "insight_ids", "source_ids", "limits", "unknowns", "world_id", "context",
    "source_locator", "evidence_roles", "deep_links",
)
INSIGHT_FIELDS = (
    "id", "title", "summary", "class", "classification", "decision", "hypothesis",
    "one_discriminating_test", "validation_needed", "logical_limit", "limits",
    "dataset_ids", "investigation_ids", "source_ids", "deep_links",
)
RAW_INSIGHT_FIELDS = ("id", "title", "class", "decision", "hypothesis", "one_discriminating_test", "logical_limit")
SOURCE_FIELDS = (
    "id", "manifest_id", "title", "authors", "year", "authority", "kind", "role",
    "url", "doi", "edition", "sha256", "pdf_page", "source_locator", "section",
    "direct_page_links", "scope", "limits", "access", "fulltext_status",
)
PRIVATE_KEYS = frozenset({
    "path", "paths", "file", "files", "local_pdf", "local_pdf_url", "raw", "raw_data",
    "raw_records", "raw_rows", "raw_comments", "weights", "model_weights", "training_data",
    "source_payload", "private", "credentials", "numeric_catalog", "numeric_data",
    "observed_values", "measurements", "calculation", "metrology_calculation",
    "numerical_presets", "presets", "parameters", "points", "series",
})
PATH_TEXT = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s\"<>]*|\\\\[^\s\\]+\\[^\s\"<>]*"
    r"|file://[^\s\"<>]*|(?<![A-Za-z0-9:])/(?:Users|home|mnt|tmp|workspace|private|var)/[^\s\"<>]*",
    re.IGNORECASE,
)


class AtlasUnavailable(ValueError):
    """Missing, stale or unreviewed input; suitable for a public HTTP 503."""


def _id(value):
    return isinstance(value, str) and bool(IDENTIFIER.fullmatch(value))


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _page(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _url(value, relative=False):
    if not isinstance(value, str) or any(ord(char) < 32 for char in value):
        return None
    try:
        parsed = urlsplit(value)
        if parsed.scheme in {"http", "https"} and parsed.hostname and not parsed.username and not parsed.password:
            return value
        if (relative and value.startswith("/") and not value.startswith("//") and not parsed.scheme
                and "\\" not in unquote(value)
                and not any(part in {".", ".."} for part in unquote(parsed.path).split("/"))
                and not PATH_TEXT.search(value)):
            return value
    except ValueError:
        pass
    return None


def _private(key):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(key)).lower().replace("-", "_")
    return name in PRIVATE_KEYS or name.startswith("private_") or name.endswith(("_path", "_paths", "_weights"))


def _clean(value):
    if isinstance(value, dict):
        return {key: (_url(child, relative=True) if str(key).lower() in {"url", "href", "source_url", "official_url"}
                      else _clean(child)) for key, child in value.items() if not _private(key)}
    if isinstance(value, list):
        return [_clean(child) for child in value]
    if isinstance(value, str):
        if value.lstrip().lower().startswith(("javascript:", "data:", "file:")):
            return None
        if not _url(value) and re.search(
                r"(?:^|\s)(?:\.{1,2}[\\/]|[\w.-]+[\\/])[^\s]*\.(?:csv|tsv|xlsx?|parquet|pkl|pt|pth|bin|safetensors)(?:$|\s)",
                value, re.I):
            return "[private file reference withheld]"
        return PATH_TEXT.sub("[private file reference withheld]", value)
    return deepcopy(value)


def _project(value, fields):
    return {key: _clean(value[key]) for key in fields if key in value}


def _links(value):
    if not isinstance(value, list):
        raise AtlasUnavailable("Public links must be an explicit list")
    result = []
    for link in value:
        if not isinstance(link, dict):
            raise AtlasUnavailable("Invalid public link metadata")
        public = _project(link, ("label", "title", "kind", "target_id", "source_id", "source_ids",
                                 "pdf_page", "physical_pdf_page", "section"))
        public["url"] = _url(link.get("url"), relative=True)
        result.append(public)
    return result


def _read(path):
    if path is None:
        raise AtlasUnavailable("Habitat atlas inputs are not configured")
    try:
        payload = Path(path).read_bytes()
        def reject_constant(_value):
            raise ValueError("Non-finite JSON number")
        value = json.loads(payload.decode("utf-8-sig"), parse_constant=reject_constant)
        if not isinstance(value, dict):
            raise ValueError("Expected a JSON object")
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        raise AtlasUnavailable("Reviewed habitat atlas input is unavailable or invalid") from exc
    return value, hashlib.sha256(payload).hexdigest()


def _registry(items, name, key="id"):
    if not isinstance(items, list):
        raise AtlasUnavailable(f"{name} must be an explicit registry list")
    result = {}
    for item in items:
        if not isinstance(item, dict) or not _id(item.get(key)) or item[key] in result:
            raise AtlasUnavailable(f"Invalid or duplicate {name} identity")
        result[item[key]] = item
    return result


def _refs(refs, known, label):
    if not isinstance(refs, list) or any(not isinstance(ref, str) or ref not in known for ref in refs):
        raise AtlasUnavailable(f"Unresolved {label} references")


def _optional_refs(value, sources, insights, datasets=None):
    if isinstance(value, list):
        for child in value:
            _optional_refs(child, sources, insights, datasets)
    elif isinstance(value, dict):
        for key, child in value.items():
            if key == "source_ids":
                _refs(child, sources, "source")
            elif key == "source_id" and child is not None:
                _refs([child], sources, "source")
            elif key == "insight_ids":
                _refs(child, insights, "insight")
            elif key == "dataset_ids" and datasets is not None:
                _refs(child, datasets, "dataset")
            _optional_refs(child, sources, insights, datasets)


def _source(source, manifest, port):
    public = _project(source, SOURCE_FIELDS)
    public["title"] = _clean(source.get("title"))
    public["edition"] = _clean(source.get("edition"))
    public["url"] = _url(source.get("url") or source.get("public_url"))
    public["direct_page_links"] = _links(source.get("direct_page_links", []))
    public["local_pdf_url"] = None
    sid = source.get("manifest_id") or source["id"]
    digest = source.get("sha256")
    entry = manifest.get(sid) if isinstance(sid, str) else None
    if (isinstance(sid, str) and MANIFEST_ID.fullmatch(sid)
            and isinstance(digest, str) and SHA256.fullmatch(digest)
            and isinstance(entry, dict) and entry.get("sha256") == digest
            and isinstance(entry.get("path"), (str, Path)) and Path(entry["path"]).suffix.lower() == ".pdf"):
        fragment = f"#page={source['pdf_page']}" if _page(source.get("pdf_page")) else ""
        public["local_pdf_url"] = f"http://127.0.0.1:{port}/sources/{sid}.pdf{fragment}"
    return public


class HabitatAtlas:
    def __init__(self, mapping_path, insight_path, qa_contract_path):
        self.mapping_path = Path(mapping_path) if mapping_path else None
        self.insight_path = Path(insight_path) if insight_path else None
        self.qa_contract_path = Path(qa_contract_path) if qa_contract_path else None

    def catalog(self, manifest, port):
        if not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535:
            raise ValueError("A valid loopback server port is required")
        mapping, mapping_sha = _read(self.mapping_path)
        insight_map, insight_sha = _read(self.insight_path)
        qa, qa_sha = _read(self.qa_contract_path)
        if (mapping.get("schema_version") != "habitat-fire-atlas-mapping/1.0"
                or insight_map.get("schema_version") != "cross-dataset-fire-insight-map-v1"
                or qa.get("schema_version") != "habitat-fire-mapping-qa/1.0"
                or mapping.get("status") != "reviewed_qualitative_navigation_mapping"
                or qa.get("status") != "pass"
                or qa.get("review_status") != "reviewed_for_qualitative_habitat_fire_navigation"):
            raise AtlasUnavailable("A reviewed habitat mapping and QA contract are required")
        if (qa.get("mapping_sha256") != mapping_sha
                or qa.get("reviewed_insight_map_sha256") != insight_sha):
            raise AtlasUnavailable("Habitat mapping or insight-map review binding is missing or stale")
        policy = mapping.get("public_payload_policy", {})
        if not isinstance(policy, dict) or any(policy.get(key) is not False for key in (
                "exact_numeric_measurements", "numeric_safe_presets", "local_machine_paths",
                "raw_trial_rows", "safety_approval_generated")):
            raise AtlasUnavailable("The qualitative-only public-data policy must be explicit")
        habitats = _registry(mapping.get("habitats"), "habitat")
        fire_types = _registry(mapping.get("fire_types"), "fire type")
        datasets = _registry(mapping.get("datasets"), "dataset", "psi_id")
        sources = _registry(mapping.get("source_refs"), "source")
        supplied_insights = _registry(mapping.get("insights", []), "supplied insight", "insight_id")
        original_insights = _registry(insight_map.get("insights"), "original insight")
        limitations = _registry(mapping.get("limitations"), "limitation")
        gaps = _registry(mapping.get("gaps"), "gap")
        tags = _registry(mapping.get("state_tags"), "state tag")
        if not CI_IDS.issubset(original_insights) or set(supplied_insights) != CI_IDS:
            raise AtlasUnavailable("The explicit CI01-CI08 source identities are required")
        if not habitats or not fire_types or not datasets:
            raise AtlasUnavailable("Reviewed habitat, fire-type and dataset registries are required")
        for source in sources.values():
            digest = source.get("sha256")
            if digest is not None and (not isinstance(digest, str) or not SHA256.fullmatch(digest)):
                raise AtlasUnavailable("Source SHA metadata is invalid")
            if source.get("pdf_page") is not None and not _page(source["pdf_page"]):
                raise AtlasUnavailable("Source physical PDF page must be a positive integer or unknown")
        def check_ids(item):
            for field, registry in (("source_ref_ids", sources), ("limit_ids", limitations),
                                    ("gap_ids", gaps), ("state_tag_ids", tags)):
                if field in item:
                    _refs(item[field], registry, field)
            _optional_refs(item, sources, CI_IDS, datasets)
        def limit_text(ids):
            return [_clean(limitations[i].get("text_en")) for i in ids]
        for item in [*datasets.values(), *fire_types.values(), *supplied_insights.values()]:
            check_ids(item)
        for iid, supplied in supplied_insights.items():
            original = original_insights[iid]
            if supplied.get("source_claim_class") != original.get("class"):
                raise AtlasUnavailable("A CI source claim class cannot be upgraded during joining")
            _refs(supplied.get("source_psi_ids", []), datasets, "CI source dataset")
            if set(supplied.get("source_psi_ids", [])) != set(original.get("datasets", [])):
                raise AtlasUnavailable("A CI source-dataset identity changed during joining")
        defaults = mapping.get("default_path")
        if (not isinstance(defaults, dict) or defaults.get("habitat_id") not in habitats
                or defaults.get("fire_type_id") not in fire_types or defaults.get("insight_id") not in supplied_insights):
            raise AtlasUnavailable("Default navigation must resolve supplied registry identities")
        entries = manifest.get("sources", manifest) if isinstance(manifest, dict) else {}
        entries = entries if isinstance(entries, dict) else {}
        public = {
            "schema_version": "habitat-fire-atlas-api/1.0", "status": mapping["status"], "version": VERSION,
            "title": _clean(mapping.get("purpose_en")), "summary": _clean(mapping.get("scope_en")),
            "source_snapshot_note": _clean(mapping.get("source_snapshot_note_en")),
            "default_path": _project(defaults, ("habitat_id", "fire_type_id", "insight_id")),
            "defaults": {"habitat": defaults["habitat_id"], "fire_type": defaults["fire_type_id"], "insight": defaults["insight_id"]},
            "habitats": [], "fire_types": [], "datasets": [], "routes": [], "relations": [],
            "sources": [_source(item, entries, port) for item in sources.values()], "insights": [],
            "limitations": [_project(item, ("id", "text_en")) for item in limitations.values()],
            "limits": limit_text(list(limitations)),
            "gaps": [_project(item, ("id", "text_en")) for item in gaps.values()],
            "state_tags": [_project(item, ("id", "label_en")) for item in tags.values()],
            "applicability_legend": _clean(mapping.get("applicability_legend", [])),
            "out_of_scope_primary_scenarios": _clean(mapping.get("out_of_scope_primary_scenarios", [])),
            "input_bindings": {"mapping_sha256": mapping_sha, "insight_map_sha256": insight_sha, "qa_contract_sha256": qa_sha},
            "navigation_role": "Authored evidence relationships only; selection does not establish measured conditions, physical applicability, product effectiveness or operational safety.",
        }
        for dataset in datasets.values():
            item = _project(dataset, ("research_kind", "source_environment", "architecture_id", "doi", "routed", "unrouted_reason_en"))
            item.update({"id": dataset["psi_id"], "title": _clean(dataset.get("title_en")),
                         "short_name": _clean(dataset.get("short_name")), "summary": _clean(dataset.get("relevance_en")),
                         "source_ids": deepcopy(dataset.get("source_ref_ids", [])), "nasa_url": _url(dataset.get("nasa_url")),
                         "deep_links": _links(dataset.get("deep_links", [])), "limits": limit_text(dataset.get("limit_ids", [])),
                         "independent_target_habitat_incident_validation": dataset.get("independent_target_habitat_incident_validation")})
            public["datasets"].append(item)
        for kind in fire_types.values():
            item = _project(kind, ("id", "scenario_status", "state_tag_ids", "gap_ids"))
            item.update({"title": _clean(kind.get("label_en")), "context": _clean(kind.get("scenario_en")),
                         "examples": _clean(kind.get("example_labels_en", []))})
            public["fire_types"].append(item)
        for iid, supplied in supplied_insights.items():
            public["insights"].append({
                "id": iid, "title": _clean(supplied.get("title_en")), "summary": _clean(supplied.get("additional_knowledge_en")),
                "hypothesis": _clean(supplied.get("product_or_joint_effect_hypothesis_en")),
                "source_claim_class": original_insights[iid]["class"], "source_classification": original_insights[iid]["class"],
                "source_psi_ids": deepcopy(supplied["source_psi_ids"]), "source_ids": deepcopy(supplied.get("source_ref_ids", [])),
                "limits": limit_text(supplied.get("limit_ids", [])), "deep_links": _links(supplied.get("deep_links", [])),
                "public_copy_role": _clean(supplied.get("public_copy_role")),
            })
        for habitat in habitats.values():
            check_ids(habitat)
            _refs(habitat.get("immediate_related_psi_ids", []), datasets, "immediate dataset")
            _refs(habitat.get("all_related_psi_ids", []), datasets, "habitat dataset")
            item = _project(habitat, ("id", "gravity_context", "scenario_status", "immediate_related_psi_ids", "all_related_psi_ids"))
            item.update({"title": _clean(habitat.get("label_en")), "context": _clean(habitat.get("description_en")),
                         "intro": _clean(habitat.get("intro_en")), "limits": limit_text(habitat.get("limit_ids", [])),
                         "approved_environment_parameters": None, "world_contexts": {}})
            for world in habitat.get("sub_scenarios", []):
                if not isinstance(world, dict) or not _id(world.get("id")):
                    raise AtlasUnavailable("Invalid supplied rover sub-scenario")
                if world.get("direct_target_data_verified") not in (None, False):
                    raise AtlasUnavailable("This qualitative contract does not establish measured rover-world validation")
                key = {"moon_rover": "moon", "mars_rover": "mars"}.get(world["id"], world["id"])
                item["world_contexts"][key] = {"id": world["id"], "title": _clean(world.get("label_en")),
                    "gravity_context": _clean(world.get("gravity_context")),
                    "direct_target_data_verified": world.get("direct_target_data_verified"),
                    "context": _clean(world.get("context_en"))}
            seen_types = set()
            paths = habitat.get("fire_type_paths")
            if not isinstance(paths, list):
                raise AtlasUnavailable("Explicit habitat fire paths are required")
            for path in paths:
                fid = path.get("fire_type_id") if isinstance(path, dict) else None
                if fid not in fire_types or fid in seen_types:
                    raise AtlasUnavailable("A habitat fire path is unknown or duplicated")
                seen_types.add(fid); check_ids(path)
                if path.get("numeric_parameters_applied") is not False:
                    raise AtlasUnavailable("Habitat navigation cannot apply numeric conditions")
                if path.get("safety_approval") != "not_established":
                    raise AtlasUnavailable("This qualitative contract cannot establish safety approval")
                route = _project(path, ("state_tag_ids", "gap_ids", "scenario_status", "numeric_parameters_applied", "safety_approval"))
                route.update({"id": f"{habitat['id']}--{fid}", "habitat_id": habitat["id"], "fire_type_id": fid,
                              "scenario": _clean(path.get("scenario_en")), "dataset_links": [], "insight_links": [],
                              "gaps": [_project(gaps[g], ("id", "text_en")) for g in path.get("gap_ids", [])]})
                for name, target_key, registry in (("dataset_links", "psi_id", datasets), ("insight_links", "insight_id", supplied_insights)):
                    links = path.get(name)
                    if not isinstance(links, list):
                        raise AtlasUnavailable("Dataset and CI links must remain separate explicit lists")
                    seen_targets = set()
                    for link in links:
                        target = link.get(target_key) if isinstance(link, dict) else None
                        if target not in registry or target in seen_targets:
                            raise AtlasUnavailable("Unknown or duplicate path target")
                        seen_targets.add(target); check_ids(link)
                        role = link.get("evidence_applicability")
                        if role not in RELATIONSHIPS or not _text(link.get("why_en")):
                            raise AtlasUnavailable("Every link needs its supplied relationship and explanation")
                        for flag in ("target_incident_or_product_validated", "target_habitat_validated"):
                            if link.get(flag) is not None and link[flag] is not False:
                                raise AtlasUnavailable("An evidence-navigation link cannot qualify the target habitat or product")
                        if "partial_gravity" in str(habitat.get("gravity_context", "")) and role == "direct":
                            raise AtlasUnavailable("This source contract does not supply direct partial-gravity measurements")
                        if name == "insight_links" and link.get("source_claim_class") != original_insights[target].get("class"):
                            raise AtlasUnavailable("A path cannot upgrade the original CI claim class")
                        normalized = _project(link, ("link_role", "source_environment", "target_incident_or_product_validated", "target_habitat_validated", "source_claim_class", "limit_ids"))
                        normalized.update({"dataset_id" if name == "dataset_links" else "insight_id": target,
                            "relationship": role, "statement": _clean(link["why_en"]),
                            "source_ids": deepcopy(registry[target].get("source_ref_ids", [])),
                            "limits": limit_text(link.get("limit_ids", [])), "deep_links": _links(link.get("deep_links", []))})
                        route[name].append(normalized)
                        # Separate typed graph edges, with no dataset-to-CI edge.
                        public["relations"].append({"id": f"{route['id']}--{target_key}--{target}",
                            "habitat_id": habitat["id"], "fire_type_id": fid,
                            "target_type": "dataset" if name == "dataset_links" else "insight", **deepcopy(normalized)})
                public["routes"].append(route)
            public["habitats"].append(item)
        actual_counts = {"habitats": len(habitats), "fire_types": len(fire_types), "habitat_fire_paths": len(public["routes"]),
                         "dataset_inventory_entries": len(datasets), "insight_ids": len(supplied_insights)}
        if qa.get("counts") != actual_counts:
            raise AtlasUnavailable("Reviewed registry and path counts do not match the supplied input")
        return public


def catalog(mapping_path, insight_path, qa_contract_path, manifest, port):
    return HabitatAtlas(mapping_path, insight_path, qa_contract_path).catalog(manifest, port)
