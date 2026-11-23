import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const source = (await readFile(new URL('./worker.mjs', import.meta.url), 'utf8')).replace(
  "import { DurableObject } from 'cloudflare:workers';",
  'class DurableObject {constructor(ctx,env){this.ctx=ctx;this.env=env;}}');
const {default: worker, FlameContainer} = await import('data:text/javascript;base64,' + Buffer.from(source).toString('base64'));
const env = {OPENAI_API_KEY:'synthetic-key', FLAME_PROXY_TOKEN:'synthetic-proxy-token-at-least-32-characters',
  FLAME_CONTAINER:{getByName:()=>({fetch:async request=>Response.json({path:new URL(request.url).pathname})})}};
assert.equal((await worker.fetch(new Request('https://demo.test/'),{})).status,503);
assert.equal((await worker.fetch(new Request('https://demo.test/',{headers:{Origin:'https://other.test'}}),env)).status,403);
assert.equal((await worker.fetch(new Request('https://demo.test/unknown',{method:'POST',body:'{}'}),env)).status,404);
assert.equal((await worker.fetch(new Request('https://demo.test/api/workspace/search',{method:'POST',body:'x'.repeat(40000)}),env)).status,413);
assert.equal((await worker.fetch(new Request('https://demo.test/api/workspace/search',{method:'POST',body:'{}'}),env)).status,200);
let started, forwarded;
const port = {fetch:async request=>{
  if (typeof request==='string') return new Response('healthy');
  forwarded=request; return new Response('ok');
}};
const ctx = {container:{running:false,images:{base:'synthetic-image'},start:options=>{started=options;},
  setInactivityTimeout:async()=>{},getTcpPort:()=>port},storage:{transaction:async callback=>callback({get:async()=>null,put:async()=>{}})}};
const object = new FlameContainer(ctx,env);
assert.equal((await object.fetch(new Request('https://demo.test/'))).status,200);
assert.equal(started.enableInternet,true);
assert.equal(started.labels.profile,'concise-medium-v1');
assert.equal(started.env.OPENAI_API_KEY,'synthetic-key');
assert.equal(started.env.NASA_AI_MODEL,'gpt-6.1-sol');
assert.equal(started.env.NASA_OPENAI_REASONING_EFFORT,'medium');
assert.equal(started.env.NASA_OPENAI_SERVICE_TIER,'default');
assert.equal(started.env.NASA_OPENAI_MAX_OUTPUT_TOKENS,'4096');
assert.equal(started.env.NASA_AI_TIMEOUT_SECONDS,'45');
assert.equal(forwarded.headers.get('X-Flame-Proxy-Token'),env.FLAME_PROXY_TOKEN);
assert.equal(forwarded.headers.get('Origin'),null);

// Reuse the persistent DO: replace an obsolete image or startup profile,
// await a completed stop before starting, and keep a matching container alive.
for (const active of [
  {image:'old-image',labels:{profile:'concise-medium-v1'}},
  {image:'synthetic-image',labels:{profile:'old-profile'}},
  {image:'synthetic-image',labels:{profile:'concise-medium-v1'}}
]) {
  const events = [];
  const container = {running:true,images:{base:'synthetic-image'},
    inspect:async()=>active,
    destroy:async(...args)=>{
      assert.equal(args.length,0);
      events.push('destroy');
      await Promise.resolve();
      container.running=false;
      events.push('stopped');
    },
    start:options=>{
      assert.equal(container.running,false);
      assert.equal(options.image,'synthetic-image');
      assert.equal(options.labels.profile,'concise-medium-v1');
      assert.equal(options.env.NASA_OPENAI_REASONING_EFFORT,'medium');
      assert.equal(options.env.NASA_OPENAI_SERVICE_TIER,'default');
      container.running=true;
      events.push('start');
    },
    setInactivityTimeout:async()=>{},getTcpPort:()=>port};
  await new FlameContainer({...ctx,container},env).ready();
  const matching = active.image==='synthetic-image' && active.labels.profile==='concise-medium-v1';
  assert.deepEqual(events,matching ? [] : ['destroy','stopped','start']);
}
console.log(JSON.stringify({status:'PASS',contracts:9,live_cloudflare:false,live_openai:false}));
