"""Stable evidence tiers and a query-level, source-grounded fallback brief.

No corpus lookup, model request, query repair or scientific calculation occurs
here. Only already eligible source documents and their reviewed notes are used.
The caller owns scope refusal and any separately labeled live-AI integration.
"""
from __future__ import annotations

from copy import deepcopy
import re
from urllib.parse import urlsplit


RELATIONS = {"direct_source", "related_work", "related_psi"}


def _documents(value):
    rows = value.get("documents") if isinstance(value, dict) else value
    if not isinstance(rows, list) or any(not isinstance(d, dict) or not isinstance(d.get("id"), str) or not d["id"] for d in rows):
        raise ValueError("Supply already eligible, enriched documents with explicit IDs")
    if len({d["id"] for d in rows}) != len(rows):
        raise ValueError("Document IDs must be unique")
    return rows


def _insights(document):
    result = []
    for insight in document.get("insights", []):
        if not isinstance(insight, dict) or insight.get("relationship") not in RELATIONS:
            continue
        if any(not isinstance(insight.get(k), str) or not insight[k].strip() for k in ("claim", "status", "pillar")):
            continue
        locator = insight.get("source_locator")
        if not ((isinstance(locator, str) and locator.strip()) or (isinstance(locator, dict) and locator)):
            continue
        result.append(insight)
    return result


def prioritize_documents(documents, limit=12):
    """Reorder only the input IDs, stably within three evidence tiers."""
    rows = _documents(documents)
    if limit is not None and (isinstance(limit, bool) or not isinstance(limit, int) or limit < 1):
        raise ValueError("Limit must be a positive integer or None")
    tiers = [[], [], []]
    for ordinal, original in enumerate(rows, 1):
        document = deepcopy(original)
        insights = _insights(document)
        tier = 0 if any(i["relationship"] == "direct_source" for i in insights) else 1 if insights else 2
        document["lexical_rank"] = document.get("lexical_rank", document.get("rank", ordinal))
        document["evidence_tier"] = ("direct_source_insights", "related_source_insights", "source_gap")[tier]
        tiers[tier].append(document)
    result = [d for tier in tiers for d in tier]
    if limit is not None:
        result = result[:limit]
    for ordinal, document in enumerate(result, 1):
        document["rank"] = ordinal
    return result


def _words(text):
    return set(re.findall(r"[a-z0-9]+", str(text).lower()))


def _has(text, *patterns):
    return all(re.search(p, text, re.I) for p in patterns)


# These are qualitative links between observables, not numerical predictions.
# A link is used only if the supplied reviewed claims contain its descriptors.
MECHANISMS = [
    {"id": "reaction_stage", "terms": "cool flame heptane extinction droplet",
     "patterns": (r"cool", r"hot|visible", r"continu|persist|after|disappear"),
     "text": "The retrieved cool-flame evidence separates loss of a visible hot flame from the end of fuel reaction; the measured reaction stage and extinction endpoint matter."},
    {"id": "quenching_blowoff", "terms": "solid PMMA flow ventilation quenching blowoff extinction",
     "patterns": (r"quench", r"blow.?off"),
     "text": "The matched solid-fire evidence distinguishes low-flow quenching from high-flow blowoff. They are different extinction regimes, rather than one universal ventilation threshold."},
    {"id": "smoke_detection_chain", "terms": "smoke aerosol particle detector detection aging sensor",
     "patterns": (r"smoke|aerosol|particle", r"size|aging|aged|residence|transport|response"),
     "text": "The matched smoke evidence separates aerosol properties and transport from a detector's response. A particle-size or aging result is not itself an alarm-performance result."},
    {"id": "oxygen_pressure", "terms": "oxygen pressure normoxic flammability lunar",
     "patterns": (r"oxygen", r"pressure", r"normoxic|partial pressure|low.pressure.high.oxygen|oxygen fraction"),
     "text": "The matched atmosphere evidence retains oxygen fraction and total pressure separately; normoxic conditions do not automatically make two fire tests equivalent."},
    {"id": "solid_geometry", "terms": "PMMA solid thickness geometry backing substrate groove spread",
     "patterns": (r"thickness|groov|substrate|backing|boundary.layer", r"heat|spread|flame"),
     "text": "In the matched solid-fire evidence, geometry and heat transfer help determine flame spread. Material identity alone does not specify a component's burning behavior."},
    {"id": "soot_onset", "terms": "SPICE smoke point soot nozzle burner length",
     "patterns": (r"smoke.point|soot.emission", r"onset|burner|nozzle|length"),
     "text": "The retrieved smoke-point evidence concerns soot-emission onset under a burner protocol; that observable differs from arbitrary-flow flame length and a cabin alarm threshold."},
    {"id": "termination_mode", "terms": "BRE emulator fuel isolation supply extinction stop",
     "patterns": (r"fuel", r"supply|cut.?off|stopp", r"self.ext|command|terminat"),
     "text": "A commanded fuel cutoff and self-extinction are different experiment endpoints. The recorded termination mode must accompany a burning or extinction comparison."},
    {"id": "flow_heat_transport", "terms": "flow ventilation oxygen heat transport flame",
     "patterns": (r"flow|ventilation", r"oxygen", r"heat"),
     "text": "The matched studies treat airflow as part of both reactant delivery and heat transfer, rather than an isolated fan setting."},
]


def _source_identity(document):
    doi = document.get("doi")
    return ("doi:" + doi.strip().lower()) if isinstance(doi, str) and doi.strip() else document["id"]


def _category_suggestion(query, documents, context):
    selected = context.get("fire_type")
    if selected not in {"gaseous_fuel_fire", "solid_material_fire", "gas", "solid"}:
        return None
    explicit_droplet = bool(re.search(r"droplet|liquid.drop|液滴", query, re.I))
    heptane_cool = _has(query, r"heptane|c7h16|庚烷", r"cool|冷焰")
    if not (explicit_droplet or heptane_cool):
        return None
    # A real matched source result prevents a no-data routing suggestion.
    for document in documents:
        for insight in _insights(document):
            if insight["relationship"] != "direct_source":
                continue
            text = insight["claim"]
            if explicit_droplet and re.search(r"droplet|liquid.drop", text, re.I):
                return None
            if heptane_cool and _has(text, r"heptane|c7h16", r"cool"):
                return None
    return {"fire_type": "liquid_fuel_fire", "label": "Try Liquid fuel / droplets",
            "reason": "Check the liquid-droplet category for the requested droplet or n-heptane cool-flame studies. No corresponding source result is established in the current category.",
            "status": "Query-routing suggestion, not an added search result or a phase determination",
            "scope_changed": False, "source_ids": []}


def build_brief(query, documents, context=None):
    """Summarize the supplied query result set, independent of any paper click."""
    if not isinstance(query, str):
        raise ValueError("Query must be a string")
    rows = _documents(documents)
    context = context if isinstance(context, dict) else {}
    terms = _words(query)
    items = []
    for ordinal, document in enumerate(rows):
        for insight in _insights(document):
            text = insight["claim"] + " " + str(insight.get("design_implication", ""))
            items.append({"document": document, "insight": insight, "text": text,
                          "overlap": len(terms & _words(text)), "order": ordinal})
    direct = [i for i in items if i["insight"]["relationship"] == "direct_source"]
    related = [i for i in items if i["insight"]["relationship"] != "direct_source"]
    ordered = sorted(direct, key=lambda i: (-i["overlap"], i["order"])) + sorted(related, key=lambda i: (-i["overlap"], i["order"]))
    concepts = []
    for mechanism in MECHANISMS:
        support = [i for i in ordered if _has(i["text"], *mechanism["patterns"])]
        if support:
            source_ids, works = [], set()
            for item in support:
                work = _source_identity(item["document"])
                if work not in works:
                    works.add(work); source_ids.append(item["document"]["id"])
                if len(source_ids) == 4:
                    break
            concepts.append({**mechanism, "source_ids": source_ids,
                             "score": len(terms & _words(mechanism["terms"])),
                             "first_order": min(i["order"] for i in support),
                             "direct_support": any(i["insight"]["relationship"] == "direct_source" for i in support)})
    concepts.sort(key=lambda c: (-c["score"], not c["direct_support"], c["first_order"]))
    if concepts:
        overview = concepts[0]["text"]
        overview_ids = concepts[0]["source_ids"]
        if not concepts[0]["direct_support"]:
            overview = "Related-source context: " + overview
    elif ordered:
        overview = "The matching reviewed evidence addresses " + ", ".join(dict.fromkeys(i["insight"]["pillar"] for i in ordered)) + ". Its source-specific outcomes and proposed actions are separated below."
        overview_ids = list(dict.fromkeys(i["document"]["id"] for i in ordered))
        if not direct:
            overview = "Related-source context: " + overview
    elif rows:
        overview = "Matching source records were found, but this result set does not yet contain a source-reviewed physical finding. The records are bibliographic leads rather than established fire-control results."
        overview_ids = []
    else:
        overview = "No eligible source result matches this query in the selected category."
        overview_ids = []

    takeaways, actions, seen_claims, seen_works = [], [], set(), set()
    # Prefer source diversity without claiming the studies are independent.
    first_pass, second_pass = [], []
    for item in ordered:
        identity = _source_identity(item["document"])
        if identity not in seen_works:
            first_pass.append(item); seen_works.add(identity)
        else:
            second_pass.append(item)
    for item in first_pass + second_pass:
        insight, document = item["insight"], item["document"]
        key = " ".join(insight["claim"].split()).lower()
        if key in seen_claims:
            continue
        seen_claims.add(key)
        prefix = "Related-source evidence: " if insight["relationship"] != "direct_source" else ""
        source_part = re.split(r"\s+(?:Design implication|Proposed use|Proposed application):\s*", insight["claim"], maxsplit=1, flags=re.I)[0]
        takeaways.append({"text": prefix + source_part, "source_ids": [document["id"]],
                          "relationship": insight["relationship"], "status": insight["status"],
                          "source_locator": deepcopy(insight["source_locator"])})
        if len(takeaways) == 2:
            break
    for item in ordered:
        insight, document = item["insight"], item["document"]
        action = insight.get("design_implication")
        if isinstance(action, str) and action.strip():
            actions.append({"text": action, "source_ids": [document["id"]],
                            "relationship": insight["relationship"], "status": "Research design implication, not a validated operating instruction",
                            "source_locator": deepcopy(insight["source_locator"])})
            break
    source_ids = list(dict.fromkeys(overview_ids + [s for item in takeaways + actions for s in item["source_ids"]]))
    result = {"overview": overview, "overview_source_ids": overview_ids, "takeaways": takeaways,
              "actions": actions, "source_ids": source_ids,
              "method": "deterministic_reviewed_source_synthesis", "generated_by_api": False,
              "considered_source_ids": [d["id"] for d in rows], "scope_changed": False,
              "engineering_safety_approved": False}
    suggestion = _category_suggestion(query, rows, context)
    if suggestion:
        result["category_suggestion"] = suggestion
        if rows:
            result["overview"] = "The current category has no reviewed result for the requested fuel/phase combination. " + result["overview"]
    return result


def _narrative_rows(narratives):
    if narratives is None:
        return []
    if isinstance(narratives, dict):
        narratives = narratives.get("narratives", narratives.get("narrative_options", narratives.get("eligible_narratives", [])))
    if not isinstance(narratives, list):
        raise ValueError("Reviewed narratives must be an explicit list or overlay object")
    return narratives


FOCUS_PATTERNS = {
    "pressure": r"\bpressures?\b|壓力",
    "oxygen": r"\boxygen\b|\bO2\b|氧濃度|氧氣",
    "initial_diameter": r"initial (?:droplet |drop )?(?:diameters?|sizes?)|(?:droplet|drop) (?:diameters?|sizes?)|初始.{0,3}(?:直徑|尺寸)",
    "diameter": r"\bdiameters?\b|直徑",
    "thickness": r"\bthickness(?:es)?\b|厚度",
    "particle_size": r"particle sizes?|particle diameters?|粒徑",
    "flow": r"\b(?:airflows?|flows?|coflows?)\b|\bventilation\b|fan speeds?|流速|通風",
    "gravity": r"\bgravity\b|重力差異|重力影響",
    "temperature": r"\btemperatures?\b|溫度",
    "alarm_delay": r"alarm delays?|alarm latenc(?:y|ies)|detection delays?|detection latenc(?:y|ies)|time to (?:alarm|detect)|how (?:long|quickly|fast).{0,30}(?:alarm|detect)|警報延遲|偵測延遲",
    "geometry": r"\bgeometr(?:y|ies)\b|\bshapes?\b|\b(?:radius|radii)\b|\bwidths?\b|形狀|幾何",
}
ALARM_TIMING_CLAIM = (r"\b(?:alarm|detection)[-\s]+(?:latenc(?:y|ies)|delays?)\b|"
    r"\btime (?:to|until|before) (?:an? )?(?:alarm|detection|detect)\b|"
    r"\b(?:alarm|detector) (?:trigger|activation|triggering) (?:time|delay|latency)\b|"
    r"\balarm (?:response )?(?:time|timing)\b|"
    r"\b(?:delay|latenc(?:y|ies)) (?:in|of|before|to) (?:the )?(?:alarm|detection)\b|警報延遲|偵測延遲")


def _question_focus(query, context=None):
    supplied = (context or {}).get("question_focus", "")
    if isinstance(supplied, list):
        supplied = " ".join(s for s in supplied if isinstance(s, str))
    if not isinstance(supplied, str):
        supplied = ""
    text = query + " " + supplied.replace("_", " ")
    focus = [key for key, pattern in FOCUS_PATTERNS.items() if re.search(pattern, text, re.I)]
    if re.search(r"response times?", text, re.I) and re.search(r"alarm|detector|detection|smoke", text, re.I) and "alarm_delay" not in focus:
        focus.append("alarm_delay")
    if "initial_diameter" in focus or "particle_size" in focus:
        focus = [f for f in focus if f != "diameter"]
    return focus


def _work_matches(document, work):
    """Check available canonical identity; never infer identity from a title."""
    if not isinstance(work, str) or not work:
        return False
    if work.startswith("doi:"):
        doi = document.get("doi")
        return bool(doi) and "doi:" + doi.strip().lower() == work.lower()
    if work.startswith("ntrs:"):
        identifier = work.split(":", 1)[1]
        try:
            source = urlsplit(document.get("source_url") or "")
            exact_url = source.hostname == "ntrs.nasa.gov" and bool(re.match(r"/(?:api/)?citations/" + re.escape(identifier) + r"(?:/|$)", source.path))
        except ValueError:
            exact_url = False
        return exact_url or identifier in document.get("ntrsIds", [])
    if work.startswith("source-sha256:"):
        sha = work.split(":", 1)[1]
        return any(e.get("source_sha256") == sha for e in document.get("evidence", [])) or any(i.get("source_sha256") == sha for i in document.get("insights", []))
    return False


def _instantiate_narrative(narrative, rows):
    if not isinstance(narrative, dict):
        return None
    identifier = narrative.get("id") or narrative.get("narrative_id")
    text = narrative.get("text") or narrative.get("overview")
    bindings = narrative.get("source_bindings")
    if not isinstance(identifier, str) or not isinstance(text, str) or not 1 <= len(text.split()) <= 75:
        return None
    if not isinstance(bindings, list) or len(bindings) < 2 or not narrative.get("environment"):
        return None
    actual = {d["id"]: d for d in rows}
    selected_ids, works, selected_bindings = [], [], []
    for binding in bindings:
        if not isinstance(binding, dict) or binding.get("relationship") != "direct_source":
            return None
        candidates = binding.get("document_ids", [])
        work = binding.get("source_work_id")
        work = work.strip().lower() if isinstance(work, str) else work
        selected = next((d for d in rows if d["id"] in candidates
                         and any(i["relationship"] == "direct_source" for i in _insights(d))
                         and _work_matches(d, work)), None)
        locators = binding.get("source_locators")
        if selected is None or not isinstance(locators, list) or not locators or not all(isinstance(s, str) and s.strip() for s in locators) or not binding.get("supported_findings"):
            return None
        selected_ids.append(selected["id"]); works.append(work)
        selected_bindings.append({**deepcopy(binding), "document_ids": [selected["id"]]})
    if len(set(works)) < 2 or len(set(selected_ids)) < 2:
        return None
    # Every required source group must be fulfilled, including optional groups
    # not represented by the source-binding list. Nothing is fetched or added.
    required = narrative.get("required_source_groups", [])
    if not isinstance(required, list) or any(not isinstance(g, list) or not any(i in actual for i in g) for g in required):
        return None
    cards = []
    for original in narrative.get("combined_insights", [])[:2]:
        if not isinstance(original, dict) or not original.get("text") or not original.get("action"):
            continue
        cards.append({**deepcopy(original), "citation_ids": list(dict.fromkeys(selected_ids)),
                      "source_ids": list(dict.fromkeys(selected_ids)), "source_work_ids": list(dict.fromkeys(works)),
                      "evidence_kind": "cross_source_interpretation"})
    if not cards:
        return None
    return {"id": identifier, "narrative_id": identifier, "text": text, "overview": text,
            "environment": narrative["environment"], "family": narrative.get("family"),
            "query_terms": deepcopy(narrative.get("query_terms", [])), "priority": narrative.get("priority", 0),
            "answer_topics": deepcopy(narrative.get("answer_topics", [])),
            "combined_insights": cards, "source_ids": list(dict.fromkeys(selected_ids)),
            "citation_ids": list(dict.fromkeys(selected_ids)), "source_work_ids": list(dict.fromkeys(works)),
            "source_bindings": selected_bindings, "required_source_groups": [[i] for i in dict.fromkeys(selected_ids)],
            "limits": deepcopy(narrative.get("limits", [])), "evidence_kind": "cross_source_interpretation"}


def eligible_narratives(query, documents, context=None, narratives=None, limit=2):
    """Return only compact reviewed stories whose exact source works are present."""
    if not isinstance(query, str):
        raise ValueError("Query must be a string")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("Narrative limit must be positive")
    rows = _documents(documents)
    context = context if isinstance(context, dict) else {}
    family = {"solid_material_fire": "solid", "electrical_overheating_smoke": "smoke",
              "liquid_fuel_fire": "liquid", "gaseous_fuel_fire": "gas"}.get(context.get("fire_type"))
    generic = {"fire", "flame", "flames", "combustion", "safety", "nasa", "space", "spacecraft", "microgravity", "research", "a", "the", "in", "of", "and"}
    terms = _words(query) - generic
    focus = _question_focus(query, context)
    options = []
    for narrative in _narrative_rows(narratives):
        item = _instantiate_narrative(narrative, rows)
        if item is None:
            continue
        if focus and not set(focus).issubset(set(item["answer_topics"])):
            continue
        overlap = len(terms & _words(" ".join(item["query_terms"])))
        if terms and not overlap:
            continue
        options.append((overlap, item["family"] == family if family else False, item["priority"], item))
    options.sort(key=lambda p: (-p[0], -p[1], -p[2]))
    return [deepcopy(p[3]) for p in options[:limit]]


def _compact_complete(text, maximum=65):
    if not isinstance(text, str) or not text.strip():
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    result = []
    for sentence in sentences:
        if len((" ".join(result + [sentence])).split()) > maximum:
            break
        result.append(sentence)
    return " ".join(result)


def _source_environment(source):
    diagram = source.get("diagram") or {}
    title = str(source.get("title", ""))
    primary = title + " " + str(diagram.get("label", ""))
    gravity = "Microgravity" if re.search(r"microgravity|zero.gravity", primary, re.I) else "Low-gravity" if re.search(r"low.gravity", primary, re.I) else None
    def environment(subject):
        return gravity + " " + subject + " conditions" if gravity else "Reported " + subject + " conditions"
    environments = {"solid": "Reported solid-fuel combustion conditions", "smoke": "Reported smoke-generation and sensing conditions",
        "droplet": "Reported droplet-combustion conditions", "jet": "Reported jet-flame conditions",
        "sphere": "Reported spherical-burner conditions", "disk": "Reported disk-burner conditions"}
    if diagram.get("source_locator") and diagram.get("kind") in environments:
        subject = environments[diagram["kind"]].removeprefix("Reported ").removesuffix(" conditions")
        return environment(subject)
    # Primary source title can identify the study subject. Incidental smoke or
    # sensor keywords inside a solid-fire result cannot redefine its apparatus.
    if re.search(r"PMMA|polymethyl|solid.fuel|fabric|suppression of solids", title, re.I):
        return environment("solid-fuel and flow")
    if re.search(r"droplet", title, re.I):
        return environment("droplet-combustion")
    if re.search(r"smoke|aerosol|detector", title, re.I):
        return environment("smoke-generation and sensing")
    if re.search(r"coflow", title, re.I):
        return environment("coflow flame")
    return "Conditions of the cited source"


def build_story(query, documents, context=None, narratives=None):
    """Whole-query environment → discovery → safety interpretation.

    Cross-source conclusions require a reviewed overlay and two distinct source
    works. Without one, the fallback retains a source-specific statement and
    does not relabel it as a combined finding.
    """
    rows = _documents(documents)
    result = build_brief(query, rows, context)
    focus = _question_focus(query, context)
    options = eligible_narratives(query, rows, context, narratives)
    result.update(environment="Conditions of the cited studies", combined_insights=[],
                  citation_ids=deepcopy(result["source_ids"]), eligible_narratives=options,
                  narrative_id=None, narrative_ids=[], question_focus=focus)
    if options:
        selected = options[0]
        result.update(overview=selected["overview"], environment=selected["environment"],
                      combined_insights=deepcopy(selected["combined_insights"]),
                      source_ids=deepcopy(selected["source_ids"]), citation_ids=deepcopy(selected["source_ids"]),
                      overview_source_ids=deepcopy(selected["source_ids"]),
                      source_work_ids=deepcopy(selected["source_work_ids"]),
                      narrative_id=selected["id"], narrative_ids=[selected["id"]],
                      method="reviewed_cross_source_story", takeaways=[], actions=[])
    else:
        # Use an authored per-source result rather than an unbound generic
        # mechanism statement. The original paper text is left untouched.
        source = next((d for d in rows if _insights(d)), None)
        focused_insight = None
        if focus:
            candidates = []
            fuel_patterns = {"n-heptane": r"heptane|c7h16", "PMMA": r"PMMA|polymethyl", "methanol": r"methanol|CH3OH",
                             "n-dodecane": r"dodecane|c12h26", "propane": r"propane|c3h8"}
            wanted_fuel = next(((name, pattern) for name, pattern in fuel_patterns.items() if re.search(pattern, query, re.I)), None)
            for ordinal, doc in enumerate(rows):
                for insight in _insights(doc):
                    claim = re.split(r"\s+(?:Design implication|Proposed use|Proposed application):\s*", insight["claim"], maxsplit=1, flags=re.I)[0]
                    covered = sum(bool(re.search(ALARM_TIMING_CLAIM if f == "alarm_delay" else FOCUS_PATTERNS[f], claim, re.I)) for f in focus)
                    if covered != len(focus):
                        continue
                    own_text = claim + " " + str(doc.get("title", ""))
                    fuel_match = not wanted_fuel or bool(re.search(wanted_fuel[1], own_text, re.I))
                    if not fuel_match:
                        continue
                    candidates.append((covered == len(focus), fuel_match, covered, insight["relationship"] == "direct_source", -ordinal, doc, insight, claim))
            candidates.sort(key=lambda c: c[:5], reverse=True)
            if candidates:
                _, fuel_match, _, _, _, source, focused_insight, claim = candidates[0]
                summary = _compact_complete(claim, 48)
                if summary:
                    label = ", ".join(f.replace("_", " ") for f in focus)
                    if fuel_match:
                        summary = "Closest reviewed " + label + " statement: " + summary
                    else:
                        summary = "Related source context: " + summary
                        summary += " This does not establish " + wanted_fuel[0] + " behavior for the requested " + label + " change."
                    result.update(overview=summary, overview_source_ids=[source["id"]], source_ids=[source["id"]],
                                  citation_ids=[source["id"]], method="reviewed_focus_statement", environment=_source_environment(source),
                                  takeaways=[], actions=[], answer_status="source_statement_only")
                    result["focused_source_locator"] = deepcopy(focused_insight["source_locator"])
                    return result
            label = ", ".join(f.replace("_", " ") for f in focus)
            fuel_label = (" for " + wanted_fuel[0]) if wanted_fuel else ""
            result.update(overview="The retrieved reviewed findings do not establish the requested " + label + " response" + fuel_label + ".",
                          source_ids=[], citation_ids=[], overview_source_ids=[], combined_insights=[], takeaways=[], actions=[],
                          method="reviewed_focus_gap", answer_status="not_established_in_retrieved_evidence")
            return result
        if source:
            summary = _compact_complete(source.get("summary"))
            if not summary:
                summary = _compact_complete(_insights(source)[0]["claim"])
            if summary:
                result.update(overview=summary, overview_source_ids=[source["id"]],
                              source_ids=[source["id"]], citation_ids=[source["id"]],
                              method="reviewed_single_source_story", environment=_source_environment(source), takeaways=[], actions=[])
                relation = _insights(source)[0]["relationship"]
                if relation != "direct_source" and not summary.startswith("Related"):
                    result["overview"] = "Related-source context: " + summary
    return result
