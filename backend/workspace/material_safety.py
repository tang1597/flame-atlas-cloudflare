"""Describe relevant experiments, without imposing one universal control factor."""
import re
try:
    from .search_brief import _work_matches
except ImportError:
    from search_brief import _work_matches


def build_material_safety(query, documents):
    if not re.search(r'\bPMMA\b', query, re.I) or not re.search(r'\bsafe\b|\bPASS\b|安全', query, re.I):
        return None
    profiles = [
        {'work':'doi:10.1016/j.combustflame.2018.10.016', 'terms':r'pressure|kPa|bar|atm|psi|壓力',
         'description':'ground PMMA pressure tests at fixed airflow'},
        {'work':'doi:10.1007/s10694-019-00863-3', 'terms':r'thickness|groove|slab|sheet|geometry|厚度|幾何',
         'description':'Saffire PMMA slab tests comparing thickness and groove geometry'},
        {'work':'ntrs:20150008961', 'terms':r'oxygen|O2|airflow|flow|氧|流速',
         'description':'ISS BASS-II tests varying oxygen and airflow to measure extinction'},
    ]
    eligible = []
    for profile in profiles:
        source = next((d for d in documents if _work_matches(d, profile['work']) and any(
            i.get('relationship') == 'direct_source' and i.get('source_locator') for i in d.get('insights', []))), None)
        if source:
            eligible.append((bool(re.search(profile['terms'],query,re.I)), profile, source))
    eligible.sort(key=lambda row:not row[0])
    matched = [row for row in eligible if row[0]][:2] or eligible[:1]
    if not matched:
        return None
    sources = [row[2] for row in matched]
    descriptions = [row[1]['description'] for row in matched]
    locators = [i['source_locator'] for d in sources for i in d['insights']
                if i.get('relationship') == 'direct_source' and i.get('source_locator')]
    return {'scope':'material_fire', 'decision':'not_established',
            'question_scope':'Can these inputs establish fire safety?',
            'headline':'No—these inputs are insufficient to establish fire safety.',
            'key_dependency':'',
            'explanation':'Available studies include ' + ' and '.join(descriptions) + '. These studies do not establish fire safety for your exact conditions.',
            'source_ids':[d['id'] for d in sources], 'source_locators':list(dict.fromkeys(locators)),
            'experiments':[{'source_id':row[2]['id'],'work':row[1]['work'],'description':row[1]['description']} for row in matched],
            'limits':['The described experiments are related evidence, not a validated prediction for the requested condition combination.',
                      'The controlling variables depend on the question and experimental architecture; airflow is not a universal priority.']}
