"""Conservative user-input checks; no numerical presets or safety decisions."""
import re
try:
    from .ai_service import _fuel_identities
except ImportError:
    from ai_service import _fuel_identities

LABELS = {'solid_material_fire': 'Solid materials', 'electrical_overheating_smoke': 'Electrical / smoke',
          'liquid_fuel_fire': 'Liquid fuels', 'gaseous_fuel_fire': 'Gas systems'}
NUMBER = r'([-+]?\d+(?:\.\d+)?)'


def condition_issues(query):
    text = query.replace('\u2212', '-')
    issues = []
    oxygen = re.findall(NUMBER + r'\s*%\s*(?:O2\b|oxygen\b|氧)', text, re.I)
    oxygen += re.findall(r'(?:oxygen(?:\s+(?:concentration|fraction))?|O2|氧濃度)\s*(?:(?:of|at|to)\s*|[=:：為是]\s*)?' + NUMBER + r'\s*%', text, re.I)
    if any(not 0 <= float(value) <= 100 for value in oxygen):
        issues.append('Oxygen concentration must be between 0% and 100%.')
    absolute_after = re.findall(NUMBER + r'\s*(?:kPa|MPa|Pa|bar|atm|psi)\s*(?:absolute|絕對)', text, re.I)
    absolute_first = re.findall(r'(?:absolute\s+pressure|絕對壓力)\s*(?:(?:of|at)\s*|[=:：為是]\s*)?' + NUMBER + r'\s*(?:kPa|MPa|Pa|bar|atm|psi)', text, re.I)
    if any(float(value) < 0 for value in absolute_after + absolute_first):
        issues.append('Absolute pressure cannot be negative; check the sign or specify gauge pressure.')
    same_state = (re.search(r'same chamber|single chamber|同一.{0,4}[艙室]', text, re.I)
                  and re.search(r'same time|simultaneous|at once|same.{0,9}chamber condition|同時', text, re.I))
    comparing = re.search(r'\bcompare\b|\bversus\b|\bvs\b|比較|對照', text, re.I)
    if same_state and not comparing and len(set(float(v) for v in oxygen)) > 1:
        issues.append('Clarify the oxygen concentration for one chamber state, or compare separate conditions.')
    return issues


def requested_category(query):
    # A cross-category comparison is intentional, not a mistaken selection.
    if re.search(r'\b(?:compare|compared|versus|vs)\b|difference between|比較|對照', query, re.I):
        return None
    if re.search(r'\b(?:detector|detection|alarm|aerosol)\b|smoke (?:aging|particle)|偵測|警報|氣膠', query, re.I):
        return 'electrical_overheating_smoke'
    patterns = {
        'solid_material_fire': r'\b(?:PMMA|cellulose|fabric|plastic|solid fuel|solid material)\b|固體|塑膠|布料',
        'liquid_fuel_fire': r'\b(?:droplet|droplets|liquid fuel|liquid fuels)\b|液滴|液態燃料',
        'gaseous_fuel_fire': r'\b(?:gaseous|gas flame|gas burner|lighter)\b|(?:propane|butane|methane|ethylene|propylene) flame|瓦斯|打火機',
    }
    matches = [kind for kind, pattern in patterns.items() if re.search(pattern, query, re.I)]
    return matches[0] if len(matches) == 1 else None


def query_issue(query, selected_type):
    problems = condition_issues(query)
    if problems:
        return {'kind': 'invalid_conditions', 'overview': ' '.join(problems), 'issues': problems}
    suggested = requested_category(query)
    if suggested and selected_type != 'auto' and selected_type != suggested:
        return {'kind': 'category_mismatch',
                'overview': 'This question concerns ' + LABELS[suggested].lower() + '. Search that category to find the matching experiments.',
                'category_suggestion': {'fire_type': suggested, 'label': 'Search ' + LABELS[suggested],
                    'scope_changed': False, 'source_ids': [], 'reason': 'The selected fire type differs from the explicit subject of the question.'}}
    return None


def named_subject_gap(query, documents):
    """Check an explicitly named fuel/material against the actual result pool."""
    names = re.findall(r'\b(?:fuel|material)\s+(?:called\s+)?[\"\']?([A-Za-z0-9][A-Za-z0-9_-]*)', query, re.I)
    generic = {'flow', 'rate', 'supply', 'properties', 'selection', 'combustion', 'fire', 'fires', 'in', 'at', 'is', 'and', 'or', 'for', 'the', 'a'}
    def key(value):
        value = re.sub(r'\bpropene\b|丙烯', 'propylene', value.casefold())
        return re.sub(r'[^a-z0-9]', '', value)
    texts = [key(' '.join(str(d.get(field, '')) for field in ('title','abstract','summary','reviewed_search_terms'))) for d in documents]
    missing = [name for name in dict.fromkeys(names) if name.casefold() not in generic
               and not any(key(name) in text for text in texts)]
    return ('No matched source identifies ' + ', '.join(missing) + '. Check the material name or search a related fuel.') if missing else None


def _negative_materials(query):
    materials = {'polypropylene','polyethylene','ptfe','kapton','cotton','silicone','pyrell','pvc'}
    removed = []
    names = set()
    for match in re.finditer(r'\b(?:not|exclude|excluding|without)\s+([A-Za-z][A-Za-z0-9_-]*)', query, re.I):
        name = match.group(1)
        recognized = _fuel_identities(name) or ({name.casefold()} if name.casefold() in materials else set())
        if recognized:
            names.update(recognized)
            removed.append((match.start(), match.end()))
    positive_text = query
    for start, end in reversed(removed):
        positive_text = positive_text[:start] + ' ' + positive_text[end:]
    return names, _fuel_identities(positive_text)


def filter_excluded_sources(query, documents):
    excluded, positive = _negative_materials(query)
    if not excluded:
        return documents
    def identities(text):
        return _fuel_identities(text) | {name for name in excluded if re.search(r'\b' + re.escape(name) + r'\b', text, re.I)}
    result = []
    precision_material_query = bool(positive and re.search(r'\b(?:paper|papers|literature)\b|文獻', query, re.I))
    for doc in documents:
        direct = [i.get('claim','') for i in doc.get('insights', []) if i.get('relationship') == 'direct_source']
        primary = ' '.join([str(doc.get('title') or ''), str(doc.get('abstract') or '')] + direct)
        if any(identities(claim) & excluded for claim in direct):
            continue
        if not direct and identities(primary) & excluded and not _fuel_identities(doc.get('title','')) & positive:
            continue
        if precision_material_query and not _fuel_identities(primary) & positive:
            continue
        result.append(doc)
    return result


def unsupported_comparison(query, documents):
    fuels = _fuel_identities(query)
    if len(fuels) < 2 or not re.search(r'\b(?:compare|versus|vs)\b|比較|對照', query, re.I):
        return None
    for doc in documents:
        for insight in doc.get('insights', []):
            claim = insight.get('claim', '')
            if (insight.get('relationship') == 'direct_source' and fuels <= _fuel_identities(claim)
                    and re.search(r'compar|versus|higher|lower|difference|faster|slower', claim, re.I)):
                return None
    return 'A matched comparison of ' + ', '.join(sorted(fuels)) + ' is not established in the retrieved reviewed findings.'


def missing_safety_conditions(query):
    if not re.search(r'\bsafe\b|\bPASS\b|安全', query, re.I):
        return []
    required = {'oxygen concentration': r'\d+(?:\.\d+)?\s*%\s*(?:O2|oxygen)|(?:oxygen|O2)\s*(?:=|at)?\s*\d+(?:\.\d+)?\s*%',
                'absolute pressure': r'\d+(?:\.\d+)?\s*(?:kPa|MPa|Pa|bar|atm|psi)',
                'airflow': r'\d+(?:\.\d+)?\s*(?:cm/s|m/s|mm/s)',
                'material geometry': r'\d+(?:\.\d+)?\s*(?:mm|cm|m)\b(?!/s)'}
    return [name for name, pattern in required.items() if not re.search(pattern, query, re.I)]
