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
assert.equal(started.env.OPENAI_API_KEY,'synthetic-key');
assert.equal(started.env.NASA_AI_MODEL,'gpt-6.1-sol');
assert.equal(forwarded.headers.get('X-Flame-Proxy-Token'),env.FLAME_PROXY_TOKEN);
assert.equal(forwarded.headers.get('Origin'),null);
console.log(JSON.stringify({status:'PASS',contracts:6,live_cloudflare:false,live_openai:false}));
