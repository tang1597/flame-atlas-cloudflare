"""Natural-language paper discovery plus source-bounded scenario navigation.

Uses the existing frozen retrieval service; no fitting, generated claims or safety
classifier. Offline papers and experimental records never belong in the web root.
"""
from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

ALIASES = {
    "打火機": "lighter propane butane gas flame stability",
    "丙烷": "propane C3H8", "丁烷": "butane C4H10",
    "丙丁烷": "propane butane", "甲醇": "methanol CH3OH",
    "庚烷": "heptane C7H16", "十二烷": "dodecane C12H26",
    "液滴": "droplet", "低氧": "oxygen extinction", "熄滅": "extinction",
    "基地": "habitat lunar base", "微重力": "microgravity",
    "可控": "flame stability control", "噴口": "burner nozzle",
    "壓力": "pressure", "流量": "flow rate",
}
RANGES = (
    ("std_pressure_Pa", "Reported pressure", .001, "kPa"),
    ("std_oxygen_fraction", "Reported oxygen; source-specific scope", 100, "mol%"),
    ("std_airflow_m_s", "Reported airflow", 1, "m/s"),
    ("std_fuel_component_flow_kg_s", "Reported fuel-component mass flow", 1, "kg/s"),
)


def url(value):
    if not isinstance(value, str):
        return None
    parsed = urlsplit(value)
    return value if parsed.scheme in {"http", "https"} and parsed.hostname and not parsed.username and not parsed.password else None


def tokens(value):
    return set(re.findall(r"[a-z0-9]+", str(value).lower()))


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def phase_matches(document, phase):
    """Separate gas-burner and droplet sources before semantic relevance ranking."""
    if phase == "unspecified":
        return True
    studies = set(document.get("studyIds") or [])
    text = " ".join(str(document.get(k) or "") for k in ("title", "abstract", "topics")).lower()
    liquid = bool(studies & {"PSI-39", "PSI-68", "PSI-69"}) or "droplet" in text
    gas = bool(studies & {"PSI-10", "PSI-23", "PSI-107", "PSI-159"}) or any(x in text for x in ("gas-jet", "gaseous fuel", "coflow burner", "gas burner"))
    return (gas and not (liquid and not studies & {"PSI-10", "PSI-23", "PSI-107", "PSI-159"})) if phase == "gas" else liquid


class ScenarioResearch:
    def __init__(self, csv_path=None, corpus_path=None, retriever=None):
        self.retriever = retriever
        self.documents = {}
        self.rows = []
        if corpus_path:
            try:
                payload = json.loads(Path(corpus_path).read_text(encoding="utf-8-sig"))
                self.documents = {d["id"]: d for d in payload.get("documents", []) if isinstance(d, dict) and isinstance(d.get("id"), str)}
            except (OSError, ValueError, TypeError):
                pass
        if csv_path:
            try:
                with Path(csv_path).open(encoding="utf-8-sig", newline="") as source:
                    self.rows = [{key: row.get(key) for key in ("dataset", "experiment", "fuel", "record_type", "oxygen_scope", "std_oxygen_scope", *(r[0] for r in RANGES))}
                                 for row in csv.DictReader(source) if row.get("dataset") in {"PSI-159", "PSI-107", "PSI-10"}]
            except (OSError, ValueError, TypeError):
                pass

    def search(self, payload):
        query = payload.get("query") if isinstance(payload, dict) else None
        if not isinstance(query, str) or not query.strip() or len(query) > 2000:
            raise ValueError("Supply a natural-language research query of 1-2000 characters")
        query = query.strip()
        expanded = query + " " + " ".join(v for k, v in ALIASES.items() if k in query)
        lower = expanded.lower()
        gas = any(x in lower for x in ("lighter", "propane", "butane", "c3h8", "c4h10"))
        phase = "gas" if gas else "liquid" if any(x in lower for x in ("droplet", "methanol", "heptane", "dodecane", "c12h26", "ch3oh")) else "unspecified"
        eligible = {key: document for key, document in self.documents.items() if phase_matches(document, phase)}
        ranked, mode = [], "lexical_fallback"
        if self.retriever and eligible:
            try:
                response = self.retriever(expanded, sorted(eligible))
                candidates = response.get("results")
                if not isinstance(candidates, list):
                    raise ValueError("Malformed retrieval result")
                seen = set()
                for item in candidates:
                    if not isinstance(item, dict):
                        raise ValueError("Malformed retrieval row")
                    document = item.get("document") or {}
                    identifier = item.get("id") or (document.get("id") if isinstance(document, dict) else None)
                    if identifier in eligible and identifier not in seen:
                        ranked.append(eligible[identifier]); seen.add(identifier)
                mode = "frozen_bge"
            except (OSError, ValueError, TypeError, KeyError):
                ranked = []
        if mode == "lexical_fallback":
            terms = tokens(expanded) - {"the", "in", "a", "paper", "papers", "find", "research", "about", "is", "can"}
            scored = []
            for document in eligible.values():
                haystack = tokens(" ".join(str(document.get(k, "")) for k in ("title", "abstract", "searchKeyphrases", "topics")))
                score = len(terms & haystack)
                if score:
                    scored.append((score, document["id"], document))
            ranked = [d for _, _, d in sorted(scored, key=lambda x: (-x[0], x[1]))]
        papers = []
        for document in ranked[:6]:
            links = document.get("nasaDataLinks") or []
            data_url = next((url(x) for x in links if isinstance(x, str) and url(x)), None)
            if not data_url:
                study = next((s for s in document.get("studyIds", []) if isinstance(s, str) and re.fullmatch(r"PSI-\d+", s)), None)
                data_url = "https://psi.nasa.gov/physci/repo/data/investigations/" + study if study else None
            papers.append({"id": document["id"], "title": document.get("title") or "Untitled source",
                           "source_url": url(document.get("doiUrl")) or url(document.get("sourceUrl")),
                           "data_url": data_url, "summary": "Retrieved source; relevance is not a safety verdict. Open the source for its abstract and methods.",
                           "year": document.get("year"), "study_ids": document.get("studyIds") or [],
                           "abstract_available": bool(document.get("abstract")), "review_status": "retrieved_not_newly_reviewed"})
        datasets = []
        if gas:
            wants_propane = any(x in lower for x in ("propane", "c3h8"))
            wants_butane = any(x in lower for x in ("butane", "c4h10"))
            if "lighter" in lower:
                wants_propane = wants_butane = True
            groups = defaultdict(list)
            for row in self.rows:
                fuel = (row.get("fuel") or "").lower()
                if wants_propane and ("propane" in fuel or "c3h8" in fuel) or wants_butane and ("butane" in fuel or "c4h10" in fuel):
                    groups[row["dataset"]].append(row)
            for dataset, rows in sorted(groups.items()):
                ranges = []
                for field, label, scale, unit in RANGES:
                    values = [number(r.get(field)) for r in rows]
                    values = [v * scale for v in values if v is not None]
                    if values:
                        ranges.append({"label": label, "min": min(values), "max": max(values), "unit": unit,
                                       "scope": "Source marginal range across related records, not a safety limit. Oxygen may refer to the oxidizer stream rather than the cabin."})
                source = "https://psi.nasa.gov/physci/repo/data/investigations/" + dataset
                datasets.append({"id": dataset, "title": dataset + " · " + ", ".join(sorted({r["experiment"] for r in rows})),
                                 "source_url": source, "data_url": source, "record_count": len(rows),
                                 "record_types": dict(Counter(r["record_type"] for r in rows)),
                                 "summary": "Related fuels: " + ", ".join(sorted({r["fuel"] for r in rows})) + ". Burner geometry and atmosphere must be matched before transfer to a lighter.",
                                 "parameter_ranges": ranges})
        return {"schema_version": "scenario-search-v1", "query": query, "search_mode": mode,
                "context": {"title": "Gas burner / lighter research" if gas else "Combustion paper search", "phase": phase,
                            "summary": "Pressurized-habitat use is a scenario assumption. Fuel blend, nozzle, flow and atmosphere remain to be specified." if gas else "Search papers first; explore supported liquid conditions separately."},
                "studies": papers, "datasets": datasets,
                "source_filter": {"phase": phase, "eligible_documents": len(eligible), "basis": "Reported study IDs and source phase terminology; relevance is not device validation."},
                "assessment": {"status": "not_established", "title": "CONTROLLABILITY UNDETERMINED" if gas else "SAFETY UNDETERMINED",
                               "message": "Related research does not establish control or operating approval for this specific device and environment."},
                "prediction": {"available": False, "reason": "No validated gas-device model is connected." if gas else "Use the liquid surface controls where supported."},
                "follow_up_options": [{"label": label, "query": query + " " + term} for label, term in (("Fuel composition", "fuel composition"), ("Nozzle geometry", "nozzle geometry"), ("Pressure", "pressure"), ("Airflow", "airflow"), ("Gravity", "gravity"))] if gas else [{"label":label,"query":query+" "+term} for label,term in (("Oxygen concentration","oxygen concentration"),("Pressure","pressure"),("Droplet size","initial droplet diameter"),("Hot / cool flames","hot cool flame transition"),("Dilution","helium carbon dioxide dilution"))]}
