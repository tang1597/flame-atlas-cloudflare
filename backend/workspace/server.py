"""Add a source-linked scene workspace to an existing loopback dashboard.

All previous endpoints are delegated to the supplied dashboard. No fitting,
generation or model-service restart is part of this integration.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from bridge import ReviewedEvidenceBridge, clean
from ai_service import AIService
from search_brief import prioritize_documents, build_brief, build_story
from search_plan import retrieve_plan, order_sources
from scope_policy import unrelated_result
from query_checks import query_issue, named_subject_gap, filter_excluded_sources, unsupported_comparison, missing_safety_conditions
from material_safety import build_material_safety
from markdown_synthesis import select_notes

HABITATS = {'space_station', 'crew_spacecraft', 'lunar_base', 'mars_base', 'pressurized_rover'}
FIRE_TYPES = {'solid_material_fire', 'electrical_overheating_smoke', 'liquid_fuel_fire', 'gaseous_fuel_fire'}
SEARCH_TYPES = FIRE_TYPES | {'auto'}
DEFAULT_TERMS = {'solid_material_fire': 'solid flammability flame spread',
                 'electrical_overheating_smoke': 'smoke aerosol detection',
                 'liquid_fuel_fire': 'droplet extinction',
                 'gaseous_fuel_fire': 'gaseous diffusion flame', 'auto': 'combustion fire safety'}


def context_from(payload):
    if not isinstance(payload, dict):
        raise ValueError('Supply a research context')
    if set(payload) - {'habitat', 'fire_type', 'world', 'query'}:
        raise ValueError('Only scene, fire type, rover context and keywords are supported')
    context = {key: payload.get(key) for key in ['habitat', 'fire_type', 'world', 'query']}
    if any(not isinstance(context[key], str) for key in ['habitat', 'fire_type', 'world']):
        raise ValueError('Scene and fire context must be strings')
    if context['habitat'] not in HABITATS or context['fire_type'] not in SEARCH_TYPES or context['world'] not in {'moon', 'mars'}:
        raise ValueError('Choose a listed scene and fire type')
    query = context['query']
    if not isinstance(query, str) or len(query) > 1000 or any(ord(c) < 32 and c not in '\t\n\r' for c in query):
        raise ValueError('Use a research query of at most 1000 characters')
    context['query'] = query.strip()
    return context


def workspace_search(bridge, atlas, payload, ai_service=None, presentation=None, narratives=None, dataset_markdown=None):
    context = context_from(payload)
    routes = [r for r in atlas.get('routes', []) if r['habitat_id'] == context['habitat'] and (context['fire_type'] == 'auto' or r['fire_type_id'] == context['fire_type'])]
    if not routes:
        raise ValueError('No reviewed scene route is available')
    allowed = list(dict.fromkeys(link['dataset_id'] for route in routes for link in route['dataset_links']))
    query = context['query'] or DEFAULT_TERMS[context['fire_type']]
    understanding = {'related': True, 'interpreted_query': query, 'method': 'scene_browse'}
    if ai_service is not None and context['query']:
        understanding = ai_service.analyze_query(context['query'])
        if understanding.get('related') is False:
            return {'documents': [], 'charts': [], 'context': context, 'understanding': understanding,
                    'query_brief': unrelated_result(), 'scope_refusal': True,
                    'ranking': {'label': ''}, 'summary': {'limits': []}}
        query = understanding.get('interpreted_query') or query
    issue = query_issue(context['query'] + '\n' + query, context['fire_type']) if context['query'] else None
    if issue:
        brief = {'overview': issue['overview'], 'source_ids': [], 'citation_ids': [], 'takeaways': [],
                 'actions': [], 'combined_insights': [], 'method': 'query_input_check'}
        if issue.get('category_suggestion'):
            brief['category_suggestion'] = issue['category_suggestion']
        return {'documents': [], 'charts': [], 'context': context, 'understanding': understanding,
                'query_brief': brief, 'query_issue': issue['kind'], 'ranking': {'label': ''}, 'summary': {'limits': []}}
    ranked = retrieve_plan(bridge, query, understanding.get('search_queries'), allowed)
    subject_gap = named_subject_gap(context['query'], ranked.get('documents', []))
    if subject_gap:
        return {'documents': [], 'charts': [], 'context': context, 'understanding': understanding,
                'query_issue': 'unknown_subject',
                'query_brief': {'overview': subject_gap, 'source_ids': [], 'citation_ids': [], 'takeaways': [],
                                'actions': [], 'combined_insights': [], 'method': 'named_subject_source_check'},
                'ranking': {'label': ''}, 'summary': {'limits': []}}
    result = bridge.enrich(ranked, context=context)
    result['documents'] = filter_excluded_sources(context['query'], result['documents'])
    comparison_gap = unsupported_comparison(context['query'], result['documents'])
    if comparison_gap:
        return {'documents': [], 'charts': [], 'context': context, 'understanding': understanding,
                'query_issue': 'unsupported_comparison',
                'query_brief': {'overview': comparison_gap, 'source_ids': [], 'citation_ids': [], 'takeaways': [],
                                'actions': [], 'combined_insights': [], 'method': 'comparison_source_check'},
                'ranking': {'label': ''}, 'summary': {'limits': []}}
    original_order = [document['id'] for document in result['documents']]
    candidates = prioritize_documents(result['documents'], limit=None)
    safety_answer = build_material_safety(context['query'], candidates)
    story_context = {**context, 'question_focus': understanding.get('question_focus', '')}
    story = build_story(query, candidates, context=story_context, narratives=narratives)
    story_ids = story.get('source_ids', [])
    narrative_pool = story.get('eligible_narratives', [])
    safety_ids = safety_answer.get('source_ids', []) if safety_answer else []
    required_ids = list(dict.fromkeys(safety_ids + story_ids + [i for n in narrative_pool for i in n.get('source_ids', [])]))
    result['documents'] = order_sources(candidates, required_ids, limit=12)
    brief = build_brief(query, result['documents'], context=context)
    brief.update(story)
    selected_ids = set(d['id'] for d in result['documents'])
    eligible_stories = [n for n in narrative_pool
                        if set(n.get('source_ids', [])) <= selected_ids]
    brief.pop('eligible_narratives', None)
    assisted = {}
    if ai_service is not None and result['documents'] and context['query']:
        if dataset_markdown is not None and getattr(getattr(ai_service, 'config', None), 'provider', None) == 'openai_responses':
            assisted = ai_service.summarize(query, result['documents'], narratives=eligible_stories,
                dataset_notes=select_notes(query, result['documents'], dataset_markdown))
        else:
            assisted = ai_service.summarize(query, result['documents'], narratives=eligible_stories)
        if assisted.get('related') is False:
            return {'documents': [], 'charts': [], 'context': context, 'understanding': understanding,
                    'query_brief': unrelated_result(), 'scope_refusal': True,
                    'ranking': {'label': ''}, 'summary': {'limits': []}}
        accepted_selection = bool(assisted.get('provider_used') and assisted.get('method') in {'api_evidence_selection', 'api_selected_reviewed_narrative', 'openai_markdown_synthesis'})
        brief['provider_selection_accepted'] = accepted_selection
        if accepted_selection:
            # The API selects real papers and reviewed story IDs, not new claims.
            selected_story = next((n for n in eligible_stories if (n.get('id') or n.get('narrative_id')) == assisted.get('narrative_id')), None)
            if assisted.get('method') == 'openai_markdown_synthesis':
                for key in ['overview', 'environment', 'source_ids', 'citation_ids', 'markdown_sources', 'generated', 'method']:
                    brief[key] = assisted[key]
                brief['overview_source_ids'] = list(assisted['source_ids'])
            elif selected_story:
                for key in ['overview', 'environment', 'combined_insights', 'narrative_id', 'source_ids',
                            'citation_ids', 'source_work_ids', 'source_bindings', 'limits']:
                    if key in selected_story:
                        brief[key] = selected_story[key]
                brief['overview_source_ids'] = list(selected_story.get('source_ids', []))
                brief['method'] = assisted['method']
            else:
                # Keep a focus-specific authored result or an explicit evidence
                # gap. Selected generic facts must not replace that answer.
                brief['method'] = 'reviewed_story_with_api_selected_sources'
            brief['provider_selection_method'] = assisted['method']
            brief['provider_used'] = True
            brief['provider_status'] = assisted.get('provider_status')
        else:
            brief['provider_used'] = bool(assisted.get('provider_used'))
            brief['provider_status'] = assisted.get('provider_status')
            brief['provider_selection_method'] = assisted.get('method')
    missing = missing_safety_conditions(context['query'])
    if missing and assisted.get('method') != 'openai_markdown_synthesis':
        brief['environment'] = (brief.get('environment', 'Cited experimental evidence').rstrip('.')
                                + '. Safety is not established: specify ' + ', '.join(missing) + '.')
        brief['environment'] += ' Ignition controls also need review.'
        brief['missing_operating_conditions'] = missing
    if (context['habitat'] in {'lunar_base', 'mars_base', 'pressurized_rover'}
            or re.search(r'\b(?:moon|lunar|mars|martian|rover)\b|月球|火星|車艙', context['query'], re.I)):
        brief['environment'] = (brief.get('environment', 'Cited experimental evidence').rstrip('.')
                                + '. Partial-gravity transfer is not validated by this result.')
    if safety_answer and assisted.get('method') != 'openai_markdown_synthesis':
        brief['safety_answer'] = safety_answer
        brief['source_ids'] = list(dict.fromkeys(safety_ids + brief.get('source_ids', [])))
    answer_ids = brief.get('source_ids', [])
    preferred_ids = assisted.get('preferred_document_ids', [])
    evidence_ids = list(dict.fromkeys([i for i in preferred_ids if i in answer_ids] + answer_ids + preferred_ids))
    result['documents'] = order_sources(result['documents'], evidence_ids, limit=12)
    chart_ids = {identifier for document in result['documents'] for identifier in document.get('chart_ids', [])}
    result['charts'] = [{**chart, 'presentation': (presentation or {}).get(chart['id'], {})}
                        for chart in result.get('charts', []) if chart['id'] in chart_ids]
    result['query_brief'] = clean(brief)
    result['understanding'] = understanding
    result['context'] = {**context, 'effective_query': query, 'allowed_study_ids': allowed,
                         'numeric_parameters_applied': False, 'operational_safety': 'unknown'}
    planned = bool(ranked.get('plan_executed'))
    ai_selected = bool(assisted.get('preferred_document_ids') and brief.get('provider_selection_accepted'))
    result['ranking'] = {'method': 'question_plan_then_selected_evidence' if planned or story_ids or ai_selected else 'insight_priority_then_relevance',
                         'label': 'Sources behind this answer first' if story_ids or ai_selected else 'Reviewed insights first',
                         'description': ranked.get('ranking_method'), 'score_is_safety': False,
                         'search_queries': ranked.get('search_queries', [query]),
                         'ai_planned': planned and understanding.get('method') == 'api_interpreted_query',
                         'ai_selected': ai_selected,
                         'lexical_order': original_order,
                         'returned_order': [d['id'] for d in result['documents']]}
    result.setdefault('provenance', {})['ranking_preserved'] = result['ranking']['returned_order'] == original_order[:12]
    result['provenance']['relevance_order_preserved_within_insight_tier'] = not bool(story_ids or ai_selected)
    return result


def integrated_handler(base_handler):
    class Handler(base_handler):
        def do_GET(self):
            path = urlsplit(self.path).path
            if path not in {'/api/workspace/status', '/api/status'} and not path.startswith('/api/workspace/charts/'):
                return super().do_GET()
            if not self.valid_request():
                return
            if urlsplit(self.path).query:
                return self.send_json({'error': 'Unexpected query parameters'}, 400)
            if path in {'/api/workspace/status', '/api/status'}:
                return self.send_json({'version': '0.10.3', 'layout': 'question-story-evidence',
                    'status': 'ready', 'training_stopped': True,
                    'semantic_retrieval': 'Configured existing frozen service; availability is reported per legacy search',
                    'physics_demo_url': self.server.physics_url,
                    'evidence_file_present': self.server.chains_path.is_file(),
                    'standards_file_present': self.server.standards_path.is_file(),
                    'baseline_version': '0.8.0', 'training_started': False,
                    'summary_method': 'reviewed_cross_source_story_selection', 'live_generation': False})
            identifier = unquote(path.removeprefix('/api/workspace/charts/'))
            if not re.fullmatch(r'[A-Za-z0-9_.:-]{1,160}', identifier):
                return self.send_json({'error': 'Invalid chart identity'}, 400)
            try:
                chart = self.server.workspace_bridge.get_chart(identifier)
                chart['presentation'] = getattr(self.server, 'workspace_presentation', {}).get(identifier, {})
                return self.send_json(chart)
            except (KeyError, ValueError):
                return self.send_json({'error': 'Reviewed comparison not found'}, 404)

        do_HEAD = do_GET

        def do_POST(self):
            if self.path != '/api/workspace/search':
                return super().do_POST()
            if not self.valid_request():
                return
            try:
                if self.headers.get('Transfer-Encoding'):
                    raise ValueError('Chunked requests are unsupported')
                size = int(self.headers.get('Content-Length', '0'))
                if not 0 < size <= 32768:
                    raise ValueError('Invalid body size')
                payload = json.loads(self.rfile.read(size))
                response = workspace_search(self.server.workspace_bridge, self.server.workspace_atlas, payload,
                                            getattr(self.server, 'workspace_ai', None),
                                            getattr(self.server, 'workspace_presentation', None),
                                            getattr(self.server, 'workspace_narratives', None),
                                            getattr(self.server, 'workspace_markdown', None))
            except (ValueError, UnicodeError, TypeError, KeyError):
                return self.send_json({'error': 'Choose a listed scene and fire type, and use up to 1000 characters of keywords.'}, 400)
            return self.send_json(response)
    return Handler


def make_integrated_server(config_path, port):
    config = json.loads(Path(config_path).read_text(encoding='utf-8-sig'))
    baseline_path = Path(config['baseline_server']).resolve(strict=True)
    sys.path.insert(0, str(baseline_path.parent))
    spec = importlib.util.spec_from_file_location('_retained_flame_dashboard', baseline_path)
    baseline = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(baseline)
    kwargs = dict(config['baseline_arguments'])
    kwargs.update(port=port, web_root=config['web_root'],
                  retriever=baseline.FrozenRetriever(config['semantic_url']))
    server = baseline.make_server(**kwargs)
    try:
        catalog = json.loads(Path(config['bridge_catalog']).read_text(encoding='utf-8-sig'))
        atlas = json.loads(Path(config['atlas_snapshot']).read_text(encoding='utf-8-sig'))
        server.workspace_bridge = ReviewedEvidenceBridge(catalog)
        server.workspace_atlas = atlas
        server.workspace_ai = AIService.from_environment()
        markdown_path = config.get('dataset_markdown_index')
        server.workspace_markdown = json.loads(Path(markdown_path).read_text(encoding='utf-8-sig')) if markdown_path else None
        narrative_path = config.get('narratives')
        server.workspace_narratives = json.loads(Path(narrative_path).read_text(encoding='utf-8-sig')) if narrative_path else None
        presentation_path = config.get('chart_presentation')
        server.workspace_presentation = json.loads(Path(presentation_path).read_text(encoding='utf-8-sig')) if presentation_path else {}
        if 'charts' in server.workspace_presentation:
            server.workspace_presentation = server.workspace_presentation['charts']
        server.RequestHandlerClass = integrated_handler(server.RequestHandlerClass)
        return server
    except Exception:
        server.server_close()
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--port', type=int, required=True)
    args = parser.parse_args()
    with make_integrated_server(args.config, args.port) as app:
        app.serve_forever()
