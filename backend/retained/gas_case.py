"""Read-only, source-curated gas-case catalog; no model or procedure engine.

The manifest is used only to attach an exact-edition local PDF link. This
module neither reads source PDFs nor emits private manifest paths. Actual PDF
bytes and their digest are checked by the server's existing source handler.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


VERSION = "1.0.0"
CASE_PATH = Path(__file__).resolve().parent / "case_studies" / "gas_isolation.json"
IDENTIFIER = re.compile(r"[A-Za-z0-9_-]{1,120}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
PUBLIC_FIELDS = (
    "schema_version", "case_id", "case_type", "title", "summary", "input_fields",
    "conditions", "sources", "related_records", "limits", "next_options",
    "science_gate", "provenance",
)
OPTIONAL_PUBLIC_FIELDS = (
    "language", "condition_count", "situational_condition_count",
    "unknown_context_condition_count", "conditions_are_mutually_exclusive",
    "condition_count_role", "input_role", "unknown_numeric_fields",
)
CONDITION_FIELDS = (
    "id", "title", "condition", "intervention_basis", "secondary_risks",
    "evidence_grade", "gaps", "source_ids", "source_locators", "unknowns",
    "not_established", "field_procedure",
)
PRIVATE_FIELDS = frozenset({
    "path", "local_path", "local_pdf", "source_path", "absolute_path",
    "workspace_path", "csv_path", "raw_data", "raw_records", "raw_rows",
    "source_cells", "training_data", "weights", "measurements", "observed_values",
})


def _reject_constant(value):
    raise ValueError("Non-finite JSON values are not allowed")


def _read_case():
    # No import-time file access and no executable configuration/eval.
    return json.loads(CASE_PATH.read_text(encoding="utf-8-sig"),
                      parse_constant=_reject_constant)


def _public_url(value):
    if not isinstance(value, str) or any(ord(char) < 32 for char in value):
        return False
    try:
        parsed = urlsplit(value)
        return bool(parsed.scheme in {"http", "https"} and parsed.hostname
                    and not parsed.username and not parsed.password)
    except ValueError:
        return False


def _check_public_tree(value):
    if isinstance(value, dict):
        if PRIVATE_FIELDS.intersection(value):
            raise ValueError("Private paths or experimental data are not public case content")
        if value.get("field_procedure") is not None:
            raise ValueError("This catalog cannot publish an operating procedure")
        for child in value.values():
            _check_public_tree(child)
    elif isinstance(value, list):
        for child in value:
            _check_public_tree(child)
    elif isinstance(value, str):
        if (re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", value)
                or re.search(r"(?:^|\s)\\\\[^\s\\]+\\", value)
                or re.search(r"(?:^|\s)/(?:mnt|home|Users|tmp|workspace)/", value)):
            raise ValueError("Absolute file paths are not public case content")


def _validate_document(value):
    if not isinstance(value, dict) or any(field not in value for field in PUBLIC_FIELDS):
        raise ValueError("Incomplete gas-case catalog")
    _check_public_tree(value)
    if not isinstance(value["sources"], list) or not value["sources"]:
        raise ValueError("Source identities are required")
    source_ids = set()
    source_roles = {}
    for source in value["sources"]:
        if not isinstance(source, dict):
            raise ValueError("Invalid source identity")
        sid = source.get("id")
        if not isinstance(sid, str) or not IDENTIFIER.fullmatch(sid) or sid in source_ids:
            raise ValueError("Invalid or duplicate source identifier")
        if (not source.get("title") or not source.get("authority")
                or not source.get("edition") or not _public_url(source.get("url"))):
            raise ValueError("Source identity, authority and official URL are required")
        if source.get("role") not in {"guidance", "related_experiment", "unknown"}:
            raise ValueError("Source role must distinguish guidance, experiment or unknown")
        digest = source.get("sha256")
        if digest is not None and (not isinstance(digest, str) or not SHA256.fullmatch(digest)):
            raise ValueError("Invalid source SHA256")
        page = source.get("pdf_page")
        if page is not None and (isinstance(page, bool) or not isinstance(page, int) or page < 1):
            raise ValueError("PDF page must be a positive physical-page integer or null")
        source_ids.add(sid)
        source_roles[sid] = source["role"]

    conditions = value["conditions"]
    if not isinstance(conditions, list) or not conditions:
        raise ValueError("Authored case conditions are required")
    condition_ids = set()
    for condition in conditions:
        if not isinstance(condition, dict) or any(k not in condition for k in CONDITION_FIELDS):
            raise ValueError("Incomplete authored condition")
        cid = condition["id"]
        if not isinstance(cid, str) or not IDENTIFIER.fullmatch(cid) or cid in condition_ids:
            raise ValueError("Invalid or duplicate condition identifier")
        if condition["field_procedure"] is not None:
            raise ValueError("This catalog cannot publish an operating procedure")
        if (condition.get("numeric_safe_threshold") is not None
                or condition.get("intervention_success_probability") is not None):
            raise ValueError("No numerical safety threshold or success probability is established")
        refs = condition["source_ids"]
        if not isinstance(refs, list) or any(sid not in source_ids for sid in refs):
            raise ValueError("Condition references an unknown source")
        for field in ("intervention_basis", "secondary_risks"):
            items = condition[field]
            if not isinstance(items, list):
                raise ValueError("Evidence items must retain text, role and source identities")
            for item in items:
                if (not isinstance(item, dict) or not isinstance(item.get("text"), str)
                        or not item["text"].strip()
                        or item.get("role") not in {"guidance", "related_experiment", "unknown"}
                        or not isinstance(item.get("source_ids"), list)
                        or any(sid not in refs for sid in item["source_ids"])):
                    raise ValueError("Invalid evidence item or source role")
                if item["role"] == "guidance" and (not item["source_ids"] or any(
                        source_roles[sid] != "guidance" for sid in item["source_ids"])):
                    raise ValueError("Related experiments cannot become official guidance")
        if not isinstance(condition["source_locators"], list):
            raise ValueError("Source locators must be explicit")
        for locator in condition["source_locators"]:
            if not isinstance(locator, dict) or locator.get("source_id") not in refs:
                raise ValueError("Locator references an unknown source")
        condition_ids.add(cid)
    if not isinstance(value["related_records"], list):
        raise ValueError("Related records must remain distinct from guidance")
    for record in value["related_records"]:
        if not isinstance(record, dict) or record.get("role") != "related_experiment":
            raise ValueError("Related records must retain their experiment role")
        refs = record.get("source_ids")
        if not isinstance(refs, list) or any(sid not in source_ids for sid in refs):
            raise ValueError("Related record references an unknown source")
        if not isinstance(record.get("source_locators"), list) or any(
                not isinstance(loc, dict) or loc.get("source_id") not in refs
                for loc in record["source_locators"]):
            raise ValueError("Related-record locator references an unknown source")
    if not isinstance(value["science_gate"], dict):
        raise ValueError("A source-only science gate is required")
    gate = value["science_gate"]
    if (gate.get("source_only") is not True
            or gate.get("automatic_field_approval") is not False
            or gate.get("field_procedure_provided") is not False):
        raise ValueError("Source-only content cannot supply field approval or procedures")
    return value


def _manifest_entries(manifest):
    if not isinstance(manifest, dict):
        return {}
    entries = manifest.get("sources", manifest)
    return entries if isinstance(entries, dict) else {}


def catalog(manifest, port):
    """Return authored conditions with optional exact-SHA local PDF links.

    Accepts either the server's source-ID mapping or a {"sources": ...}
    manifest. Missing, null or mismatched hashes never authorize a local link.
    Reported-context inputs are returned unchanged; no classification, query
    scoring, valve sequence, numerical model or safety approval is performed.
    """
    if isinstance(port, bool) or not isinstance(port, int) or not 1 <= port <= 65535:
        raise ValueError("A valid loopback server port is required")
    document = _validate_document(_read_case())
    public = {key: deepcopy(document[key]) for key in PUBLIC_FIELDS}
    public.update({key: deepcopy(document[key]) for key in OPTIONAL_PUBLIC_FIELDS
                   if key in document})
    public["version"] = VERSION
    entries = _manifest_entries(manifest)
    for source in public["sources"]:
        # Never carry a stale or caller-supplied local link out of curation.
        source["local_pdf_url"] = None
        digest = source.get("sha256")
        entry = entries.get(source["id"])
        if not (isinstance(digest, str) and SHA256.fullmatch(digest)
                and isinstance(entry, dict) and entry.get("sha256") == digest
                and isinstance(entry.get("path"), (str, Path))
                and Path(entry["path"]).suffix.lower() == ".pdf"):
            continue
        page = source.get("pdf_page")
        fragment = f"#page={page}" if page is not None else ""
        source["local_pdf_url"] = (
            f"http://127.0.0.1:{port}/sources/{source['id']}.pdf{fragment}"
        )
    return public
