/* Source-chain navigation and declared search modes only; no model execution or client ranking. */
(function (global) {
  'use strict';
  const $=id=>document.getElementById(id);
  const object=value=>value!==null && typeof value==='object' && !Array.isArray(value);
  const finite=value=>typeof value==='number' && Number.isFinite(value);
  const own=(value,key)=>Object.prototype.hasOwnProperty.call(value || {},key);
  const PILLARS=new Set(['prevention','detection','suppression']);
  const state={initialized:false,view:'library',query:'',filters:{},results:[],searchPhase:'idle',searchSerial:0,searchController:null,searchMeta:null,searchError:'',chains:{phase:'loading',data:null,error:'',serial:0,controller:null},context:{phase:'loading',data:null,error:'',serial:0,controller:null},physicsUrl:'http://127.0.0.1:8793/physics.html'};
  function fail(message){throw new TypeError(message);}
  function safeText(value){if(value==null)return 'Not supplied';const text=String(value);return /(?:[a-z]:[\\/]|file:\/\/|\\\\[^\\\s]+\\)/i.test(text) ? 'Local path withheld' : text;}
  function node(tag,className,text,parent){const el=document.createElement(tag);if(className)el.className=className;if(text!=null)el.textContent=safeText(text);if(parent)parent.append(el);return el;}
  function array(value,name,max=1000){if(!Array.isArray(value) || value.length>max)fail(name+' must be a bounded array.');return value;}
  function validateChain(chain){
    if(!object(chain) || typeof chain.id!=='string' || !chain.id.trim() || typeof chain.title!=='string' || !chain.title.trim() || !PILLARS.has(chain.pillar))fail('A source chain needs an explicit ID, title and safety pillar.');
    for(const key of ['conditions','data']){
      if(chain[key]==null)continue;
      for(const field of array(chain[key],'chain.'+key)){
        if(!object(field))fail('A condition/data field must be an object.');
        if(own(field,'value') && field.value!==null && !finite(field.value))fail('Source values must be finite numbers or null; numeric strings are not measurements.');
        if(field.display_value!=null && typeof field.display_value!=='string')fail('display_value must remain descriptive source text.');
      }
    }
    for(const key of ['study_ids','literature','next_options','canonical_document_ids'])if(chain[key]!=null)array(chain[key],'chain.'+key);
    return chain;
  }
  function validateChains(payload){
    if(!object(payload) || payload.schema_version!=='fire-safety-chains-v1')fail('The source-chain service did not supply the agreed envelope.');
    const ids=new Set();for(const chain of array(payload.chains,'chains',200)){validateChain(chain);if(ids.has(chain.id))fail('Duplicate source-chain ID.');ids.add(chain.id);}return payload;
  }
  function validateContext(payload){
    if(!object(payload) || payload.schema_version!=='iss-fire-context-v1')fail('ISS source context did not supply the agreed envelope.');
    for(const key of ['documents','principles','classification_context','limits'])array(payload[key],key,500);return payload;
  }
  function validateSearch(payload,expectedQuery){
    if(!object(payload) || payload.schema_version!=='fire-safety-search-v1' || typeof payload.query!=='string')fail('The search service did not supply the agreed result envelope.');
    if(expectedQuery!=null && payload.query.trim()!==expectedQuery)fail('The service returned results for a different query.');
    if(!['pretrained_bge_plus_source_conditions','lexical_fallback'].includes(payload.search_mode) || !['available','unavailable'].includes(payload.semantic_status))fail('The service did not declare a supported search mode and semantic status.');
    if(payload.search_mode==='pretrained_bge_plus_source_conditions' && (payload.semantic_status!=='available' || typeof payload.semantic_model!=='string' || !payload.semantic_model.trim()))fail('Semantic ranking was declared without an available, named model.');
    if(payload.search_mode==='lexical_fallback' && (payload.semantic_status!=='unavailable' || payload.semantic_model!=null))fail('Fallback mode must explicitly report semantic ranking unavailable and no semantic model.');
    if(payload.semantic_model!=null && typeof payload.semantic_model!=='string')fail('semantic_model must be a name or null.');
    const ids=new Set();for(const result of array(payload.ranked_results,'ranked_results',200)){
      if(!object(result))fail('A ranked result must be an object.');validateChain(result.chain);if(ids.has(result.chain.id))fail('Duplicate ranked source-chain ID.');ids.add(result.chain.id);
      if(result.score!=null && !finite(result.score))fail('A retrieval score must be a finite number or null.');
      if(result.rank_reasons!=null)array(result.rank_reasons,'rank_reasons');
      if(result.semantic_sources!=null){const canonical=new Set(result.chain.canonical_document_ids || []);for(const source of array(result.semantic_sources,'semantic_sources')){if(object(source) && source.score!=null && !finite(source.score))fail('A semantic-source score must be finite or null.');const id=typeof source==='string' ? source : source?.id || source?.document_id || source?.canonical_document_id;if(typeof id!=='string' || !canonical.has(id))fail('A semantic source is not exactly bound to this chain.');}}
    }
    for(const key of ['warnings','suggested_options'])if(payload[key]!=null)array(payload[key],key);
    if(payload.standards_relevant!=null && typeof payload.standards_relevant!=='boolean')fail('standards_relevant is a context pointer, not a safety verdict.');return payload;
  }
  function filters(input={}){
    if(!object(input))fail('Search filters must be an object.');
    const output={};for(const key of Object.keys(input)){
      if(!['pillar','material','gravity'].includes(key))fail('Unsupported source filter.');
      if(input[key]==null || input[key]==='')continue;if(typeof input[key]!=='string')fail('Source filters must be text.');
      const value=input[key].trim();if(!value)continue;if(value.length>120)fail('Keep each source filter within 120 characters.');if(key==='pillar' && !PILLARS.has(value))fail('Unknown safety focus.');output[key]=value;
    }return output;
  }
  function readFilters(){return filters({pillar:$('pillar-filter').value,material:$('material-filter').value,gravity:$('gravity-filter').value});}
  function resetFilters(){for(const id of ['pillar-filter','material-filter','gravity-filter'])$(id).value='';}
  function appliedFilters(){const entries=Object.entries(state.filters);$('filter-count').textContent=entries.length?' ('+entries.length+' applied)':'';$('active-filters').textContent=entries.map(([key,value])=>key+': '+safeText(value)).join(' · ');$('active-filters').hidden=!entries.length;$('clear-filters').hidden=!entries.length;}
  function assessment(title,message,kind='unknown'){$('safety-assessment').className='safety-assessment assessment-'+kind;$('assessment-title').textContent=title;$('assessment-message').textContent=message;}
  function safeLink(value){if(typeof value!=='string' || !/^https?:\/\//i.test(value))return null;try{const url=new URL(value);return !url.username && !url.password && ['http:','https:'].includes(url.protocol) ? url.href : null;}catch(_){return null;}}
  function applyLinks(payload){const candidate=payload?.physics_demo_url || payload?.links?.physics_checks_url || payload?.physics_checks_url;const href=safeLink(candidate);if(href){state.physicsUrl=href;$('physics-link').href=href;}}
  function warnings(values){const root=$('source-warnings');root.replaceChildren();if(!Array.isArray(values) || !values.length){node('p','small-note','No additional source warnings were supplied.',root);return;}const ul=node('ul','',null,root);for(const value of values)node('li','',typeof value==='string' ? value : value?.text || value?.message || 'Source warning supplied without readable text.',ul);}
  function nextQuery(value){const query=Array.isArray(value) ? value.filter(item=>typeof item==='string').join(' ') : typeof value==='string' ? value : '';if(!query.trim())return;$('safety-query').value=query;void search(query,readFilters());}
  function renderOptions(options){const root=$('next-options');root.replaceChildren();$('next-questions').hidden=true;if(!Array.isArray(options) || !options.length)return;for(const option of options){if(!object(option))continue;const terms=Array.isArray(option.query_terms) ? option.query_terms.filter(item=>typeof item==='string').join(' ') : option.query_terms;if(typeof terms!=='string' || !terms.trim())continue;const button=node('button','next-option',option.label || terms,root);button.type='button';button.addEventListener('click',()=>nextQuery(terms));}$('next-questions').hidden=!root.children.length;}
  function clearResults(message){$('evidence-results').replaceChildren();node('p','empty-state',message,$('evidence-results'));$('results-count').textContent='';renderOptions([]);}
  function renderResults(results){
    if(!results.length){clearResults(state.view==='library' ? 'Reviewed source chains are pending. No draft evidence or values have been substituted.' : 'No source chains match this query and its supplied filters. No new safety insight has been generated.');return;}
    if(typeof global.FlameSafetyChainView?.render!=='function'){clearResults('The source-chain display module is unavailable. No interpretation is substituted.');return;}
    global.FlameSafetyChainView.render($('evidence-results'),results,{physicsUrl:state.physicsUrl,isRanked:state.view==='search',onNextQuery:nextQuery});$('results-count').textContent=results.length+' reviewed chain'+(results.length===1?'':'s');
  }
  function libraryView(){
    if(state.view!=='library')return;
    global.FlameStrategySearchLinks?.sync({phase:'library'});
    appliedFilters();assessment('SAFETY NOT ASSESSED','Browsing experiments does not assess your scenario.');
    $('results-heading').textContent='Reviewed studies';$('results-note').textContent=state.chains.data?.coverage_note || 'Source library only; these chains are not ranked for a query.';
    $('semantic-mode').textContent='Unranked library';$('semantic-mode').className='mode-badge';$('semantic-note').textContent='Browse the supplied evidence. Use a query to request semantic ranking and condition-matching reasons.';
    $('semantic-model').textContent='No semantic search is claimed for library browsing.';$('active-query').textContent='Library browsing: no query-specific result.';$('standards-pointer').textContent='ISS source context remains available in the pinned panel.';warnings([]);renderOptions([]);
    if(state.chains.phase==='loading'){$('search-status').textContent='Loading the source library…';clearResults('Source chains are loading.');return;}
    if(state.chains.phase==='unavailable'){$('search-status').textContent='Source library unavailable. A query may be retried against the evidence service.';clearResults(state.chains.error);return;}
    $('search-status').textContent=state.chains.data?.chains.length ? state.chains.data.chains.length+' reviewed evidence chains' : 'Reviewed studies pending';
    const results=(state.chains.data?.chains || []).map(chain=>({chain,score:null,rank_reasons:[],semantic_sources:[]}));renderResults(results);
  }
  function searchView(){
    global.FlameStrategySearchLinks?.sync({phase:state.searchPhase,query:state.query,filters:state.filters});
    appliedFilters();$('results-heading').textContent='Results';$('active-query').textContent='Query: '+safeText(state.query)+' · Submitted source filters: '+(Object.keys(state.filters).length ? Object.entries(state.filters).map(([key,value])=>key+': '+safeText(value)).join(' · ') : 'none');$('standards-pointer').textContent='';
    if(state.searchPhase==='loading'){assessment('ASSESSMENT PENDING','Searching reviewed evidence; safety remains unknown.','pending');$('search-status').textContent='Searching…';$('semantic-mode').textContent='Pending';$('semantic-mode').className='mode-badge';$('semantic-note').textContent='The search method and results will be shown only after the service responds.';$('semantic-model').textContent='Semantic service status pending.';warnings([]);clearResults('Searching reviewed studies…');return;}
    if(state.searchPhase==='unavailable'){assessment('SAFETY CANNOT BE DETERMINED','Evidence could not be loaded.','unavailable');$('search-status').textContent='Search unavailable';$('semantic-mode').textContent='Unavailable';$('semantic-mode').className='mode-badge unavailable';$('semantic-note').textContent='Browse the studies to inspect supplied evidence without a query ranking.';$('semantic-model').textContent='No semantic-ranking result is claimed.';warnings([state.searchError]);$('results-note').textContent='No ranked response was accepted for this query.';clearResults('Search unavailable. Retry or browse studies.');return;}
    const meta=state.searchMeta,fallback=meta.search_mode==='lexical_fallback';
    assessment(meta.ranked_results.length?'SAFETY NOT ESTABLISHED':'SAFETY CANNOT BE DETERMINED',meta.ranked_results.length?'Related experiments found. Your operating conditions are not validated.':'No matching reviewed evidence for these filters.');
    $('semantic-mode').textContent=fallback ? 'Lexical fallback' : 'Pretrained BGE';$('semantic-mode').className='mode-badge'+(fallback?' fallback':'');
    $('semantic-note').textContent=fallback ? 'Fallback results are explicitly declared by the service. They are not BGE semantic ranking, and no new insight is generated here.' : 'Frozen pretrained semantic retrieval supports navigation. Its score is not evidence quality, safety probability or model validation.';
    $('semantic-model').textContent='Search mode: '+meta.search_mode+' · semantic status: '+meta.semantic_status+' · model: '+(meta.semantic_model || 'not available');
    $('search-status').textContent=meta.ranked_results.length+' reviewed result'+(meta.ranked_results.length===1?'':'s');
    $('results-note').textContent='Ranking and matching reasons are supplied by the service. Material, environment, endpoint, hardware and evidence grade remain separate from retrieval score.';
    $('standards-pointer').textContent=meta.standards_relevant ? 'The service links this query to ISS source context. This pointer is not flight authorization or a controlled/uncontrolled-fire verdict.' : 'The ISS panel is independent source context; no fire classification is inferred from this search.';
    warnings(meta.warnings || []);renderResults(meta.ranked_results);renderOptions(meta.suggested_options || []);
  }
  async function requestJSON(url,options){const response=await global.fetch(url,{cache:'no-store',...options});if(!response.ok)throw Error('The local evidence service is unavailable (HTTP '+response.status+').');return response.json();}
  function cancelSearch(){++state.searchSerial;state.searchController?.abort();state.searchController=null;state.searchPhase='idle';$('search-button').setAttribute('aria-busy','false');$('search-button').textContent='Search';}
  async function search(query,inputFilters={}){
    let q,chosen;try{if(typeof query!=='string' || !(q=query.trim()))fail('Enter a safety question or choose one of the examples.');if(q.length>2000)fail('Keep the question within 2000 characters.');chosen=filters(inputFilters);}catch(error){$('search-status').textContent=safeText(error.message);return getState();}
    cancelSearch();const serial=state.searchSerial;state.searchController=new AbortController();state.view='search';state.query=q;state.filters=chosen;state.results=[];state.searchMeta=null;state.searchError='';state.searchPhase='loading';$('safety-query').value=q;$('search-button').setAttribute('aria-busy','true');$('search-button').textContent='Search again';searchView();
    try{const payload=await requestJSON('/api/search',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({query:q,filters:chosen}),signal:state.searchController.signal});if(serial!==state.searchSerial)return getState();validateSearch(payload,q);state.searchMeta=payload;state.results=payload.ranked_results;state.searchPhase='ready';applyLinks(payload);searchView();}
    catch(error){if(serial!==state.searchSerial || error.name==='AbortError')return getState();state.searchPhase='unavailable';state.searchError=safeText(error.message);state.results=[];state.searchMeta=null;searchView();}
    finally{if(serial===state.searchSerial){$('search-button').setAttribute('aria-busy','false');$('search-button').textContent='Search';}}return getState();
  }
  async function loadChains(){
    state.chains.controller?.abort();const serial=++state.chains.serial;state.chains.controller=new AbortController();state.chains.phase='loading';state.chains.error='';libraryView();
    try{const payload=await requestJSON('/api/evidence-chains',{headers:{Accept:'application/json'},signal:state.chains.controller.signal});if(serial!==state.chains.serial)return;validateChains(payload);state.chains.data=payload;state.chains.phase='ready';applyLinks(payload);libraryView();}
    catch(error){if(serial!==state.chains.serial || error.name==='AbortError')return;state.chains.data=null;state.chains.phase='unavailable';state.chains.error=safeText(error.message);libraryView();}return getState();
  }
  async function loadContext(){
    state.context.controller?.abort();const serial=++state.context.serial;state.context.controller=new AbortController();state.context.phase='loading';$('refresh-context').disabled=true;global.FlameSafetyISS?.clear($('iss-context'),'Loading official-source context…');
    try{const payload=await requestJSON('/api/iss-fire-context',{headers:{Accept:'application/json'},signal:state.context.controller.signal});if(serial!==state.context.serial)return;validateContext(payload);state.context.data=payload;state.context.phase='ready';global.FlameSafetyISS?.render($('iss-context'),payload);}
    catch(error){if(serial!==state.context.serial || error.name==='AbortError')return;state.context.data=null;state.context.phase='unavailable';state.context.error=safeText(error.message);global.FlameSafetyISS?.clear($('iss-context'),'ISS context unavailable: '+state.context.error+' No requirement or fire definition is substituted.');}
    finally{if(serial===state.context.serial)$('refresh-context').disabled=false;}return getState();
  }
  function browse(){cancelSearch();state.view='library';state.query='';state.filters={};state.searchMeta=null;state.results=[];resetFilters();libraryView();if(state.chains.phase==='unavailable')void loadChains();return getState();}
  function getState(){return {view:state.view,query:state.query,filters:{...state.filters},searchPhase:state.searchPhase,chainPhase:state.chains.phase,contextPhase:state.context.phase,chainCount:state.chains.data?.chains.length || 0,resultIds:state.results.map(result=>result.chain.id),searchMode:state.searchMeta?.search_mode || null,semanticStatus:state.searchMeta?.semantic_status || null,physicsUrl:state.physicsUrl};}
  function init(){
    if(state.initialized)return getState();state.initialized=true;
    $('query-form').addEventListener('submit',event=>{event.preventDefault();void search($('safety-query').value,readFilters());});$('browse-button').addEventListener('click',browse);$('refresh-context').addEventListener('click',()=>void loadContext());
    $('clear-filters').addEventListener('click',()=>{resetFilters();if(state.view==='search' && state.query)void search(state.query,{});else browse();});
    $('iss-link').addEventListener('click',()=>{$('iss-fire-context').open=true;});
    for(const button of Array.from($('scenario-options').children)){if(!button.dataset.query)continue;button.addEventListener('click',()=>{resetFilters();$('safety-query').value=button.dataset.query;void search(button.dataset.query,{});});}
    global.FlameSafetyISS?.clear($('iss-context'),'Official-source context is pending.');void loadChains();void loadContext();
    // A fuel-page research link uses the same reviewed search path and limits.
    try{const query=new URL(global.location.href).searchParams.get('q')?.trim();if(query&&query.length<=2000){$('safety-query').value=query;void search(query,{});}}catch(_){}
    return getState();
  }
  global.FlameSafetyApp=Object.freeze({init,search,browse,loadChains,loadContext,getState,validateChain,validateChains,validateContext,validateSearch,filters});
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})(typeof window!=='undefined'?window:globalThis);
