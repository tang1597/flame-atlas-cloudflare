"""Server-only Responses API transport; never trains or changes the local model."""
from __future__ import annotations

import json
import time
from urllib.request import Request, urlopen


def _responses_schema(schema):
    # The local decoder accepts const: []; the API's documented subset uses
    # item/count constraints. Keep empty choices empty without inventing IDs.
    if isinstance(schema, dict):
        if schema.get('type') == 'array' and schema.get('const') == []:
            return {'type': 'array', 'items': {'type': 'string'}, 'minItems': 0, 'maxItems': 0}
        return {key: _responses_schema(value) for key, value in schema.items()}
    if isinstance(schema, list):
        return [_responses_schema(value) for value in schema]
    return schema


def build_request(chat_request, config):
    """Keep the existing evidence contract, using the selected Sol API settings."""
    response_format = chat_request.get('response_format', {'type': 'json_object'})
    if response_format['type'] == 'json_schema':
        spec = response_format['json_schema']
        format_config = {'type': 'json_schema', 'name': spec['name'],
                         'strict': spec.get('strict', True), 'schema': _responses_schema(spec['schema'])}
    elif response_format['type'] == 'json_object':
        format_config = {'type': 'json_object'}
    else:
        raise ValueError('unsupported_response_format')
    messages = []
    for message in chat_request['messages']:
        content = message['content']
        if message['role'] == 'system':
            content = content.removesuffix(' /no_think')
        messages.append({'role': message['role'], 'content': content})
    return {'model': config.model, 'input': messages,
            'reasoning': {'effort': config.reasoning_effort},
            'service_tier': config.service_tier,
            # Reasoning and visible output share this budget. The old local
            # model's small visible-output budget is insufficient for max effort.
            'max_output_tokens': config.max_output_tokens,
            'text': {'format': format_config}, 'stream': False, 'store': False}


def parse_response(raw):
    if raw.get('status') != 'completed' or raw.get('error'):
        raise ValueError('incomplete_generation')
    pieces = []
    for item in raw.get('output', []):
        if item.get('type') == 'reasoning':
            continue
        if item.get('type') != 'message' or item.get('role') != 'assistant' or item.get('status') != 'completed':
            raise ValueError('unexpected_output_item')
        for part in item.get('content', []):
            if part.get('type') != 'output_text' or not isinstance(part.get('text'), str):
                raise ValueError('refused_or_invalid_output')
            pieces.append(part['text'])
    if not pieces:
        raise ValueError('empty_output')
    candidate = json.loads(''.join(pieces))
    if not isinstance(candidate, dict):
        raise ValueError('invalid_response_object')
    return candidate


class OpenAIResponsesTransport:
    def __init__(self, config):
        if config.base_url.rstrip('/') != 'https://api.openai.com/v1':
            raise ValueError('OpenAI provider requires the official HTTPS endpoint')
        if not config.api_key.strip():
            raise ValueError('Set OPENAI_API_KEY in the server environment')
        self.config = config
        self.metadata = None

    def __call__(self, chat_request):
        self.metadata = None
        body = build_request(chat_request, self.config)
        request = Request(self.config.base_url.rstrip('/') + '/responses',
            data=json.dumps(body, ensure_ascii=False).encode('utf-8'),
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer ' + self.config.api_key})
        started = time.monotonic()
        with urlopen(request, timeout=self.config.timeout) as response:
            data = response.read(1024 * 1024 + 1)
        if len(data) > 1024 * 1024:
            raise ValueError('response_too_large')
        raw = json.loads(data)
        candidate = parse_response(raw)
        usage = raw.get('usage') or {}
        self.metadata = {'model': raw.get('model'),
                         'requested_service_tier': self.config.service_tier,
                         'actual_service_tier': raw.get('service_tier'),
                         'latency_seconds': round(time.monotonic() - started, 3),
                         'input_tokens': usage.get('input_tokens'),
                         'output_tokens': usage.get('output_tokens')}
        return candidate
