import { DurableObject } from 'cloudflare:workers';

const CONTAINER_PROFILE = 'concise-medium-v1';
const AI_SEARCHES_PER_HOUR = 300;

async function consumesAIQuota(request) {
  const path = new URL(request.url).pathname;
  if (path === '/api/liquid/compare') return false;
  if (path === '/api/workspace/search') {
    try {
      // The public gateway already enforces the 32 KiB body cap. Clone so
      // reading the small JSON here does not consume the forwarded request.
      const payload = await request.clone().json();
      if (payload && typeof payload === 'object' && !Array.isArray(payload) &&
          (payload.query === undefined || (typeof payload.query === 'string' && !payload.query.trim())))
        return false;
    } catch {} // Invalid JSON remains subject to normal backend validation.
  }
  return true;
}

export class FlameContainer extends DurableObject {
  starting;
  tail = Promise.resolve();

  async ready() {
    const container = this.ctx.container;
    if (container.running) {
      const active = await container.inspect();
      if (!active || active.image !== container.images.base || active.labels?.profile !== CONTAINER_PROFILE)
        await container.destroy();
    }
    if (!container.running) {
      container.start({image: container.images.base, instance: 'standard-1', enableInternet: true,
        labels: {profile: CONTAINER_PROFILE},
        env: {OPENAI_API_KEY: this.env.OPENAI_API_KEY, FLAME_PROXY_TOKEN: this.env.FLAME_PROXY_TOKEN,
          NASA_AI_PROVIDER: 'openai', NASA_AI_MODEL: 'gpt-6.1-sol',
          NASA_OPENAI_REASONING_EFFORT: 'medium', NASA_OPENAI_SERVICE_TIER: 'default',
          NASA_OPENAI_MAX_OUTPUT_TOKENS: '4096', NASA_AI_TIMEOUT_SECONDS: '45'}});
    }
    await container.setInactivityTimeout(300000);
    for (let attempt = 0; attempt < 100; attempt++) {
      try {
        const result = await container.getTcpPort(8080).fetch('http://container/health', {signal: AbortSignal.timeout(1000)});
        const ok = result.ok;
        await result.body?.cancel();
        if (ok) return;
      } catch {}
      await new Promise(resolve => setTimeout(resolve, 300));
    }
    throw new Error('Container readiness timeout');
  }

  async fetch(request) {
    // Serialize complete searches: the retained AI service admits one call at
    // a time. Static requests do not wait for this queue.
    if (request.method === 'POST') {
      if (await consumesAIQuota(request)) {
        const hour = Math.floor(Date.now() / 3600000);
        const accepted = await this.ctx.storage.transaction(async txn => {
          const old = await txn.get('demo-hourly-requests');
          const count = old?.hour === hour ? old.count : 0;
          if (count >= AI_SEARCHES_PER_HOUR) return false;
          await txn.put('demo-hourly-requests', {hour, count: count + 1});
          return true;
        });
        if (!accepted) {
          const retry = Math.max(1, Math.ceil(((hour + 1) * 3600000 - Date.now()) / 1000));
          return Response.json({error: 'AI search hourly limit reached. Browsing and sliders remain available.',
            code: 'ai_search_rate_limit', retry_after_seconds: retry},
            {status: 429, headers: {'Retry-After': String(retry)}});
        }
      }
      const work = this.tail.then(() => this.forward(request));
      this.tail = work.catch(() => {});
      return work;
    }
    return this.forward(request);
  }

  async forward(request) {
    this.starting ??= this.ready().finally(() => {this.starting = undefined;});
    await this.starting;
    const url = new URL(request.url);
    url.protocol = 'http:';
    url.host = 'container';
    const forwarded = new Request(url, request);
    forwarded.headers.delete('host');
    forwarded.headers.delete('origin');
    forwarded.headers.set('X-Flame-Proxy-Token', this.env.FLAME_PROXY_TOKEN);
    return this.ctx.container.getTcpPort(8080).fetch(forwarded);
  }
}

export default {
  async fetch(request, env) {
    if (!env.OPENAI_API_KEY || !env.FLAME_PROXY_TOKEN || env.FLAME_PROXY_TOKEN.length < 32)
      return Response.json({error: 'Server secrets are not configured.'}, {status: 503});
    const url = new URL(request.url);
    const origin = request.headers.get('Origin');
    if (origin && origin !== url.origin) return new Response('Origin denied', {status: 403});
    if (!['GET', 'HEAD', 'POST'].includes(request.method)) return new Response('Method denied', {status: 405});
    if (request.method === 'POST') {
      if (!['/api/workspace/search', '/api/search', '/api/liquid/compare', '/api/scenario/search'].includes(url.pathname))
        return new Response('Unknown route', {status: 404});
      const reader = request.body?.getReader();
      if (!reader) return new Response('Empty input', {status: 400});
      const chunks = []; let size = 0;
      while (true) {
        const chunk = await reader.read();
        if (chunk.done) break;
        size += chunk.value.byteLength;
        if (size > 32768) {await reader.cancel(); return new Response('Invalid input size', {status: 413});}
        chunks.push(chunk.value);
      }
      if (!size) return new Response('Empty input', {status: 400});
      const body = new Uint8Array(size); let offset = 0;
      for (const chunk of chunks) {body.set(chunk, offset); offset += chunk.byteLength;}
      request = new Request(request, {body});
    }
    try {return await env.FLAME_CONTAINER.getByName('demo').fetch(request);}
    catch {return Response.json({error: 'Demo backend is starting or unavailable.'}, {status: 503});}
  }
};
