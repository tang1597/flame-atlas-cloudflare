# Flame Atlas — Cloudflare handoff

Current frontend, retained Python backend, runtime datasets and dataset Markdown. The original research repository remains unchanged. The verified initial package is deployed from `main`.

## Included

- 370 literature records; 29 source-linked experiment/model chart views.
- Full standardized CSV snapshot (2,225 rows), reviewed catalogs, scene mappings and existing model declarations in `data/runtime.zip`.
- 525 existing dataset Markdown notes (45 solid, 102 gas, 57 liquid, 321 smoke), used as retrieved context by GPT API summary synthesis.
- 21 original NASA source tables and 18 distinct derivation inputs in `research/raw_sources.zip`. These are not the complete instrument/video archive.
- A source index for 21 local full-text IDs / 20 distinct PDFs; PDF bytes are supplied separately offline, not publicly redistributed here. Original DOI/NTRS/NASA links remain available.

## Local acceptance

```text
python -m pip install -r requirements.txt
python prepare_data.py
python run.py --check --ai-mode off
python run.py --port 8820
```

Normal startup requires a server-side `OPENAI_API_KEY`. The Cloudflare deployment uses `gpt-6.1-sol`, medium reasoning effort for concise answers and the standard (`default`) service tier. Query rewriting uses low effort while answer synthesis remains medium. Validated query plans and summaries use separate bounded five-minute in-memory caches. Synthesis receives six relevant source records (eight for comparison questions) plus up to three retrieved dataset Markdown excerpts, generates two concise query-level paragraphs, and validates source IDs, exact evidence spans and numeric claims. These checks are not proof of scientific entailment. API errors use an explicitly labeled reviewed fallback. A live n-heptane query successfully generated a Markdown-grounded summary; scientific answer quality still needs expert review. `--ai-mode off` is only the explicit offline acceptance mode.

## Cloudflare deployment target

This package preserves the Python/scipy backend using **Cloudflare Workers + Containers**. It is not a static Pages-only app. `Dockerfile` restores hash-pinned data, and `wrangler.jsonc` defines one container-backed Durable Object. The public Worker enforces same-origin requests, a small POST body limit, a global 30-POST/hour demo cap and serial search processing. The original backend keeps its loopback Host restrictions behind an authenticated container ingress.

Deployment requires a Cloudflare account with Containers support, Docker, current Node/npm and Wrangler. From this checkout:

```text
npx wrangler login
npx wrangler secret put OPENAI_API_KEY
npx wrangler secret put FLAME_PROXY_TOKEN
npx wrangler deploy
```

Enter secrets in the secret prompt/dashboard, never in source, browser JavaScript or chat. Use a newly generated random proxy token of at least 32 characters. The container must have Internet access for the OpenAI API. The supplied instance is standard-1 (4 GiB); account availability and billing must be checked before deployment. The owner has activated Workers Paid and authorized deployment and API usage; secrets are held only in Cloudflare. Containers may need time to provision after a first deployment.

The original 8793 physics helper and 8784 frozen semantic service were not listening at inventory time. Their old links remain in retained auxiliary pages, while the main workspace's charts and sliders use packaged data. Original full instrument archives, videos, model weights and credentials are excluded.

## Validation

204 Python contracts, 55 JavaScript cases, 5 packaging contracts and 9 synthetic Cloudflare gateway contracts passed. Complete and split ZIPs produced identical relocated files. A new local instance loaded the 370-record index, liquid catalog, habitat/strategy routes and PMMA/heptane/smoke searches with linked numeric charts. See `VALIDATION.json`. The Cloudflare build produced and deployed the Docker image successfully. The public app and data endpoints returned HTTP 200. A live n-heptane query returned 12 papers, 10 chart links and `openai_markdown_synthesis`, citing a dataset Markdown note. That pre-standard-switch Fast/max request took 83.5 seconds end to end (59.488 seconds synthesis). The same query on medium/default completed in 44.31 seconds (12.869 seconds synthesis), producing 46 English words with retained source citations. The public UI rendered the concise summary, and the PRF50 diameter slider updated its fixed-condition source-fit output from 0.64552 to 0.428 mm²/s.

Public demo: https://flame-atlas.hank098173.workers.dev/

Current speed release: the same live query completed in 19.281 seconds, then 4.485 seconds on an immediate repeat with both validated caches hit. Final synthesis remained medium on the standard tier; query planning used low. See `research/LIVE_LATENCY_ACCEPTANCE_20261115.json`. These are single-query measurements, not a guaranteed response time.

## Official deployment references

- https://developers.cloudflare.com/containers/get-started/
- https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/
- https://developers.cloudflare.com/containers/platform/limits/
- https://developers.openai.com/api/docs/models/gpt-6.1-sol

This independent project does not represent NASA's views or imply NASA endorsement.
