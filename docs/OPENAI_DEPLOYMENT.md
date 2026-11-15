# Flame Atlas API deployment preparation

The optional server adapter uses the OpenAI Responses API. The selected model
is `gpt-6.1-sol`, reasoning effort `max`, service tier `fast`. Official API
effort values do not include `ultra`. Fast has a price premium; this project
uses the owner's explicit Fast selection and does not request Ultrafast.

This is an adapter and configuration handoff, not a published production
service. Synthetic tests do not establish account access, real latency or API
quality. A server-side key and a deployment host are still needed for live
acceptance. The existing local demo remains on its existing provider unless
the server is explicitly configured and restarted by the operator.

## Server configuration

Set these in the hosting provider's environment/secret settings. Do not put a
key in browser code, GitHub, a URL, launch-config JSON, or a chat message.

```text
NASA_AI_PROVIDER=openai
NASA_AI_MODEL=gpt-6.1-sol
NASA_OPENAI_REASONING_EFFORT=max
NASA_OPENAI_SERVICE_TIER=fast
NASA_OPENAI_MAX_OUTPUT_TOKENS=16384
NASA_AI_TIMEOUT_SECONDS=90
OPENAI_API_KEY=<server-side secret>
```

The OpenAI provider only accepts `https://api.openai.com/v1`; remove stale
`NASA_AI_BASE_URL` and `OPENAI_BASE_URL` overrides. A key alone does not switch
the provider. Missing keys and unsupported efforts fail configuration explicitly.
No model substitution or automatic retry incurs additional calls.

Requests retain the application's persistent combustion-only scope rule and
source-ID/structured-output constraints. Temperature and other unsupported
Chat Completions options are omitted. Responses are not stored through the
API (`store: false`); this does not assert a Zero Data Retention agreement.
Incomplete responses, refusals, invalid JSON and provider errors use the
existing labeled fallback rather than claiming successful AI synthesis.

## Hosting boundary

The browser calls the same-origin `/api/workspace/search` and chart routes.
The key belongs exclusively to the Python backend. Static GitHub Pages alone
cannot run this backend or protect a key embedded in JavaScript.

The current server wraps a retained offline dashboard and uses an operator's
trusted launch configuration, reviewed catalog, narrative annotations, chart
registry and source manifest. Those machine-specific paths are not a portable
cloud release. Before public hosting, package a licensed, reviewed, small
catalog and the required server dependencies; replace local full-paper links
with DOI/NTRS links unless distribution is expressly allowed. Keep experimental
archives, complete papers, model weights and credentials offline. Configure
HTTPS, deployment origin handling and an authenticated/rate-limited backend
before exposing a paid API route. The current loopback-only server is not
public hosting configuration.

## Live acceptance after key and host setup

1. Run a relevant query through `/api/workspace/search`. Confirm the response's
   `query_understanding.provider_status` identifies `openai_responses`,
   `gpt-6.1-sol`, `max` and requested tier `fast` without exposing a key.
2. Run one typo query, one source-supported fire question, and one clearly
   unrelated question. The last must still return `sorry this is not related`.
3. Confirm cited sources exist and preserve fuel identities, conditions and
   the experiment-specific evidence limits.
4. Read `last_response_metadata` within each `provider_status`: actual
   model/tier, latency and token counts.
   A request for Fast is not proof that Fast was actually used. Some requests
   can be processed at `default`; do not report an unmeasured speedup.
5. Record end-to-end query and summary latency separately before deciding
   whether max effort meets the interactive experience requirement. Timeouts
   remain labeled fallback, not successful model output.

## Official references

- [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [Fast mode](https://developers.openai.com/api/docs/guides/fast-mode)
- [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
