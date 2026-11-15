"""Synthetic wire-contract checks; no credentials or external API calls."""
import json
import os
import unittest
from unittest.mock import patch

try:
    from .ai_service import AIConfig, AIService
    from .openai_responses import build_request, parse_response, OpenAIResponsesTransport
    from . import openai_responses as wire
    from .scope_policy import SCOPE_SYSTEM_RULE
except ImportError:
    from ai_service import AIConfig, AIService
    from openai_responses import build_request, parse_response, OpenAIResponsesTransport
    import openai_responses as wire
    from scope_policy import SCOPE_SYSTEM_RULE


def config(**changes):
    values = dict(base_url='https://api.openai.com/v1', model='gpt-6.1-sol',
                  api_key='synthetic-test-key', timeout=90, provider='openai_responses')
    return AIConfig(**(values | changes))


def completed(text='{"related": true}'):
    return {'status': 'completed', 'model': 'gpt-6.1-sol', 'service_tier': 'fast',
            'output': [{'type': 'reasoning', 'summary': []},
                       {'type': 'message', 'role': 'assistant', 'status': 'completed',
                        'content': [{'type': 'output_text', 'text': text}]}],
            'usage': {'input_tokens': 23, 'output_tokens': 41}}


class Reply:
    def __init__(self, raw): self.data = json.dumps(raw).encode()
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, limit): return self.data[:limit]


class OpenAIConfigTests(unittest.TestCase):
    def test_explicit_opt_in_preserves_sol_max_and_fast(self):
        with patch.dict(os.environ, {'NASA_AI_PROVIDER': 'openai', 'OPENAI_API_KEY': 'synthetic-test-key'}, clear=True):
            selected = AIConfig.from_environment()
        self.assertEqual((selected.provider, selected.model, selected.reasoning_effort, selected.service_tier),
                         ('openai_responses', 'gpt-6.1-sol', 'max', 'fast'))
        self.assertNotIn('synthetic-test-key', repr(selected))

    def test_a_key_alone_does_not_switch_or_start_the_existing_demo(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-test-key'}, clear=True):
            self.assertEqual(AIConfig.from_environment().provider, 'existing_local_qwen')

    def test_missing_key_foreign_host_and_unsupported_settings_are_rejected(self):
        for change in [dict(api_key=''), dict(base_url='https://example.invalid/v1'),
                       dict(reasoning_effort='ultra'), dict(service_tier='ultrafast'),
                       dict(max_output_tokens=300)]:
            with self.subTest(change=change), self.assertRaises(ValueError): config(**change)


class ResponsesWireTests(unittest.TestCase):
    def test_schema_request_keeps_prompts_without_chat_only_parameters(self):
        schema = {'type': 'object', 'properties': {}, 'required': [], 'additionalProperties': False}
        request = {'messages': [{'role': 'system', 'content': SCOPE_SYSTEM_RULE + ' /no_think'},
                                {'role': 'user', 'content': '{"query":"synthetic smoke"}'}],
                   'temperature': 0, 'max_tokens': 380,
                   'response_format': {'type': 'json_schema', 'json_schema':
                       {'name': 'test_contract', 'strict': True, 'schema': schema}}}
        payload = build_request(request, config())
        self.assertEqual(payload['model'], 'gpt-6.1-sol')
        self.assertEqual(payload['reasoning'], {'effort': 'max'})
        self.assertEqual(payload['service_tier'], 'fast')
        self.assertEqual(payload['max_output_tokens'], 16384)
        self.assertEqual(payload['text']['format']['schema'], schema)
        self.assertIn(SCOPE_SYSTEM_RULE, payload['input'][0]['content'])
        self.assertNotIn('/no_think', payload['input'][0]['content'])
        self.assertFalse(payload['store'])
        for forbidden in ['temperature', 'top_p', 'max_tokens', 'messages', 'response_format', 'chat_template_kwargs']:
            self.assertNotIn(forbidden, payload)

    def test_completed_json_ignores_reasoning_items(self):
        self.assertEqual(parse_response(completed()), {'related': True})

    def test_internal_effort_override_is_validated_and_user_message_cannot_set_it(self):
        request = {'messages': [{'role': 'user', 'content': '{"_reasoning_effort":"max"}'}]}
        self.assertEqual(build_request(request, config(reasoning_effort='medium'))['reasoning'],
                         {'effort': 'medium'})
        request['_reasoning_effort'] = 'low'
        self.assertEqual(build_request(request, config(reasoning_effort='medium'))['reasoning'],
                         {'effort': 'low'})
        request['_reasoning_effort'] = 'ultra'
        with self.assertRaisesRegex(ValueError, 'unsupported_reasoning_effort_override'):
            build_request(request, config(reasoning_effort='medium'))

    def test_no_reviewed_options_remains_empty_using_supported_array_constraints(self):
        schema = {'type': 'object', 'properties': {'narrative_ids': {'type': 'array', 'const': []}},
                  'required': ['narrative_ids'], 'additionalProperties': False}
        request = {'messages': [], 'response_format': {'type': 'json_schema', 'json_schema':
                   {'name': 'empty_choices', 'strict': True, 'schema': schema}}}
        converted = build_request(request, config())['text']['format']['schema']
        self.assertEqual(converted['properties']['narrative_ids'],
                         {'type': 'array', 'items': {'type': 'string'}, 'minItems': 0, 'maxItems': 0})
        self.assertEqual(schema['properties']['narrative_ids'], {'type': 'array', 'const': []})

    def test_incomplete_refused_tool_output_and_nonobject_are_not_answers(self):
        cases = [completed(), completed(), completed(), completed('[]'), completed('not-json'), completed()]
        cases[0]['status'] = 'incomplete'
        cases[1]['output'][1]['content'] = [{'type': 'refusal', 'refusal': 'synthetic refusal'}]
        cases[2]['output'] = [{'type': 'function_call', 'arguments': '{}'}]
        cases[5]['output'] = []
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError): parse_response(case)

    def test_official_endpoint_auth_and_actual_tier_are_recorded_without_secrets(self):
        seen = []
        raw = completed(); raw['service_tier'] = 'default'
        def fake_open(request, timeout):
            seen.append(request)
            self.assertEqual(request.full_url, 'https://api.openai.com/v1/responses')
            self.assertEqual(request.get_header('Authorization'), 'Bearer synthetic-test-key')
            self.assertEqual(timeout, 90)
            return Reply(raw)
        transport = OpenAIResponsesTransport(config())
        with patch.object(wire, 'urlopen', fake_open):
            self.assertEqual(transport({'messages': [], 'response_format': {'type': 'json_object'}}), {'related': True})
        self.assertEqual(transport.metadata['requested_service_tier'], 'fast')
        self.assertEqual(transport.metadata['actual_service_tier'], 'default')
        self.assertEqual(transport.metadata['output_tokens'], 41)
        self.assertNotIn('synthetic-test-key', json.dumps(transport.metadata))
        self.assertNotIn('api_key', json.loads(seen[0].data))

    def test_integration_keeps_unrelated_refusal_local(self):
        service = AIService(config())
        with patch.object(wire, 'urlopen', side_effect=AssertionError('No network expected')):
            result = service.analyze_query('What is the weather?')
        self.assertEqual(result['response'], 'sorry this is not related')
        self.assertNotIn('synthetic-test-key', json.dumps(service.status()))

    def test_query_service_uses_responses_and_retains_identity_checks(self):
        candidate = {'related': True, 'interpreted_query': 'PMMA at 21% O2',
                     'question_focus': 'PMMA at 21% O2', 'search_queries': ['PMMA at 21% O2'],
                     'keywords': ['PMMA'], 'fire_type_hint': 'solid_material_fire', 'response': ''}
        seen = []
        def fake_open(request, timeout):
            seen.append(json.loads(request.data))
            return Reply(completed(json.dumps(candidate)))
        service = AIService(config(reasoning_effort='medium'))
        with patch.object(wire, 'urlopen', fake_open):
            result = service.analyze_query('PMMA at 21% O2')
            # The following answer-generation call retains medium. The routing
            # stage's lower effort must not mutate shared configuration.
            service._call('Synthetic answer stage', {}, 300)
        self.assertEqual(result['method'], 'api_interpreted_query')
        self.assertEqual(result['interpreted_query'], 'PMMA at 21% O2')
        self.assertEqual(seen[0]['reasoning']['effort'], 'low')
        self.assertEqual(seen[1]['reasoning']['effort'], 'medium')
        self.assertEqual(service.config.reasoning_effort, 'medium')
        self.assertEqual(result['provider_status']['last_response_metadata']['actual_service_tier'], 'fast')

    def test_provider_error_uses_honest_fallback_without_secret_or_exception_text(self):
        service = AIService(config())
        with patch.object(wire, 'urlopen', side_effect=OSError('synthetic-test-key private detail')):
            result = service.analyze_query('smoke detection')
        self.assertEqual(result['method'], 'conservative_spelling_fallback')
        self.assertFalse(result['provider_status']['last_call_succeeded'])
        self.assertNotIn('synthetic-test-key', json.dumps(result))

    def test_validated_query_cache_expires_and_cannot_be_mutated_by_caller(self):
        candidate = {'related': True, 'interpreted_query': 'PMMA at 21% O2',
                     'question_focus': 'PMMA at 21% O2', 'search_queries': ['PMMA at 21% O2'],
                     'keywords': ['PMMA'], 'fire_type_hint': 'solid_material_fire', 'response': ''}
        calls = []
        def transport(request):
            calls.append(request)
            return json.loads(json.dumps(candidate))
        service = AIService(config(reasoning_effort='medium'), transport=transport)
        first = service.analyze_query('PMMA at 21% O2')
        first['search_queries'].append('caller mutation')
        second = service.analyze_query('PMMA at 21% O2')
        self.assertEqual(len(calls), 1)
        self.assertEqual(second['search_queries'], ['PMMA at 21% O2'])
        self.assertTrue(second['provider_status']['query_cache_hit'])
        key = next(iter(service._query_cache))
        created, cached = service._query_cache[key]
        service._query_cache[key] = (created - 301, cached)
        self.assertFalse(service.analyze_query('PMMA at 21% O2')['provider_status']['query_cache_hit'])
        self.assertEqual(len(calls), 2)
        service.config = config(reasoning_effort='medium')
        service.analyze_query('PMMA at 21% O2')
        self.assertEqual(len(calls), 3)

    def test_query_cache_skips_failed_validation_and_refusals_and_is_bounded(self):
        calls = []
        def transport(request):
            calls.append(request)
            original = json.loads(request['messages'][1]['content'])['original']
            return {'related': True, 'interpreted_query': original,
                    'question_focus': original, 'search_queries': [original],
                    'keywords': ['PMMA'], 'fire_type_hint': 'solid_material_fire', 'response': ''}
        service = AIService(config(reasoning_effort='medium'), transport=transport)
        for number in range(33):
            service.analyze_query('PMMA at ' + str(number + 1) + '% O2')
        self.assertEqual(len(service._query_cache), 32)
        service.analyze_query('What is the weather?')
        self.assertEqual(len(calls), 33)
        service._transport = lambda request: {'related': True, 'interpreted_query': 'Wrong identity'}
        first = service.analyze_query('n-heptane extinction')
        second = service.analyze_query('n-heptane extinction')
        self.assertEqual(first['method'], 'conservative_spelling_fallback')
        self.assertEqual(second['method'], 'conservative_spelling_fallback')
        self.assertEqual(len(service._query_cache), 32)


if __name__ == '__main__': unittest.main()
