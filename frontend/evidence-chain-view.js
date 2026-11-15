/* Canonical evidence-chain rendering only: no retrieval, model execution or scientific matching. */
(function (global) {
  'use strict';
  const own = (value, key) => Object.prototype.hasOwnProperty.call(value || {}, key);
  const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
  const array = value => Array.isArray(value) ? value : value == null ? [] : [value];
  const finite = value => typeof value === 'number' && Number.isFinite(value);
  const KINDS = {measured:'Source measurement',source_measurement:'Source measurement',source_measured:'Source measurement',source_aggregate:'Source aggregate',source_computation:'Author-reported computation',source_computed:'Author-reported computation',figure_estimate:'Figure estimate · approximate',source_figure_estimate:'Figure estimate · approximate',figure_digitized:'Figure estimate · approximate',source_nominal_spec:'Source nominal specification',forward_prediction:'Fixed-model forward prediction',fixed_source_example:'Fixed source example',conservation_diagnostic:'Conservation diagnostic',source_trend_ratio:'Source trend ratio'};
  const FIGURES = new Set(['figure_estimate','source_figure_estimate','figure_digitized']);
  function sensitive(value) { return /(?:(?:^|[\s"'(=])[a-z]:[\\/]|file:\/\/|\\\\[^\\\s]+\\|https?:\/\/[^\s/@]+:[^\s/@]+@)/i.test(value) || /(?:^|[\s"'(])\/(?:Users|home|mnt|tmp|var|private|Volumes|root|workspace|workspaces|media|run|opt|srv|data|etc|usr)\//.test(value); }
  function text(value) {
    if (value == null || value === '') return 'Not supplied';
    if (typeof value === 'string') return sensitive(value) ? 'Private source detail withheld' : value;
    if (typeof value === 'boolean') return value ? 'Yes' : 'No';
    if (finite(value)) return String(value);
    if (Array.isArray(value)) return value.length ? value.map(text).join(' · ') : 'Not supplied';
    if (object(value)) { const chosen = ['text','statement','description','reason','why','label'].find(key => typeof value[key] === 'string'); return chosen ? text(value[chosen]) : 'Structured detail supplied; inspect the source fields.'; }
    return 'Not supplied';
  }
  function node(tag, cls, value, parent) { const el = document.createElement(tag); if (cls) el.className = cls; if (value != null) el.textContent = String(value); if (parent) parent.append(el); return el; }
  function target(container) { return typeof container === 'string' ? document.querySelector(container) : container; }
  function url(value) { if (typeof value !== 'string' || !/^https?:\/\//i.test(value)) return null; try { const parsed = new URL(value); return ['http:','https:'].includes(parsed.protocol) && !parsed.username && !parsed.password ? parsed.href : null; } catch (_) { return null; } }
  function link(parent, label, value) { const href = url(value); if (!href) return null; const el = node('a','chain-link',label,parent); el.href = href; el.target = '_blank'; el.rel = 'noopener noreferrer'; return el; }
  function notes(parent, values, empty, cls) { const entries = array(values); if (!entries.length) return node('p','chain-muted',empty || 'Not supplied.',parent); const list = node('ul',cls || 'chain-notes',null,parent); for (const entry of entries) node('li','',text(entry),list); return list; }
  function section(parent, name, title) { const details = node('details','chain-details',null,parent); details.dataset.section = name; node('summary','',title,details); return details; }
  function suppliedKind(value) { return typeof value === 'string' && value.trim() && !/^(?:unknown|none|not[_ ](?:reported|supplied|assessed))$/i.test(value.trim()); }
  function reportedValue(row) {
    const kind = suppliedKind(row?.kind), display = typeof row?.display_value === 'string' && row.display_value.trim() ? text(row.display_value) : null;
    if (row?.value != null && !finite(row.value)) return 'Numeric value withheld · invalid source declaration';
    if (display && kind) return FIGURES.has(row.kind) && !/^(?:≈|~|about\b|approximately\b)/i.test(display) ? '≈ ' + display : display;
    if (row?.value == null) return display && !/\d/.test(display) ? display : 'Not reported';
    if (!finite(row.value) || !kind) return 'Numeric value withheld · evidence type not supplied';
    return (FIGURES.has(row.kind) ? '≈ ' : '') + String(row.value);
  }
  function quantityTable(parent, values, label, isCondition) {
    const rows = array(values).filter(object);
    if (!rows.length) return node('p','chain-muted',isCondition ? 'Source condition fields are not supplied.' : 'Actual physical-data values are not supplied; no measurements are substituted.',parent);
    const wrap = node('div','chain-table-wrap',null,parent); wrap.tabIndex = 0; wrap.setAttribute('role','region'); wrap.setAttribute('aria-label',label);
    const table = node('table','chain-table',null,wrap); node('caption','',label,table);
    const head = node('tr','',null,node('thead','',null,table));
    for (const title of ['Source field','Reported value','Unit / evidence role',isCondition ? 'Source scope' : 'Location / denominator / uncertainty']) { const th = node('th','',title,head); th.scope = 'col'; }
    const body = node('tbody','',null,table);
    for (const row of rows) {
      const tr = node('tr','',null,body); const th = node('th','',text(row.label),tr); th.scope = 'row';
      node('td','chain-reported-value',reportedValue(row),tr);
      node('td','',text(row.unit) + ' · ' + (KINDS[row.kind] || (suppliedKind(row.kind) ? text(row.kind).replace(/_/g,' ') + ' (as supplied)' : 'Evidence type not supplied')),tr);
      const details = node('td','',null,tr);
      if (isCondition) node('p','',text(row.scope),details);
      else {
        node('p','',row.source_locator ? 'Source: ' + text(row.source_locator) : 'Exact source location not supplied.',details);
        if (row.denominator != null) node('p','', 'Reported denominator: ' + text(row.denominator),details);
        node('p','',row.uncertainty == null ? 'Uncertainty: not reported.' : 'Reported uncertainty: ' + text(row.uncertainty),details);
        if (FIGURES.has(row.kind)) node('p','chain-muted','Approximate source figure estimate; no interval or curve is inferred.',details);
      }
    }
    return table;
  }
  function sourceSha(source) { return source?.sha256 || source?.source_sha256 || source?.pdf_sha256 || null; }
  function sourceEdition(source) { return source?.edition || source?.source_edition || source?.version_id || null; }
  function normalizeDoi(value) { return typeof value === 'string' ? value.trim().replace(/^https?:\/\/(?:dx\.)?doi\.org\//i,'').replace(/^doi:\s*/i,'').toLowerCase() : ''; }
  function quoteContext(sources) {
    const parents = sources.map((_,index)=>index), aliases = new Map();
    function root(index) { while (parents[index] !== index) { parents[index] = parents[parents[index]]; index = parents[index]; } return index; }
    sources.forEach((source,index)=>{
      const doi = normalizeDoi(source.doi);
      const keys = [source.work_id ? 'work:' + String(source.work_id).toLowerCase() : '',source.paper_id ? 'paper:' + String(source.paper_id).toLowerCase() : '',doi ? 'doi:' + doi : '',sourceSha(source) ? 'sha:' + String(sourceSha(source)).toLowerCase() : ''].filter(Boolean);
      for (const key of keys) { if (aliases.has(key)) parents[root(index)] = root(aliases.get(key)); else aliases.set(key,index); }
    });
    return {paperIds:new Map(sources.map((source,index)=>[source,root(index)])),words:new Map(),shown:new Set()};
  }
  function quoteCandidate(source) {
    if (object(source.source_sentence)) return source.source_sentence;
    if (object(source.quote)) return source.quote;
    if (typeof source.quote_text !== 'string') return null;
    return {text:source.quote_text,verified:own(source,'quote_verified') ? source.quote_verified : source.verified,current_contiguous_whitespace_only_match:own(source,'quote_current_verified') ? source.quote_current_verified : source.current_contiguous_whitespace_only_match,verification_status:own(source,'quote_verification_status') ? source.quote_verification_status : source.verification_status,source_sha256:source.quote_source_sha256 || source.quote_sha256,physical_pdf_page:source.quote_pdf_page ?? source.pdf_page};
  }
  function renderQuote(parent, source, context) {
    const quote = quoteCandidate(source); if (!quote) return;
    const flags = ['verified','current_contiguous_whitespace_only_match'];
    const suppliedFlags = flags.filter(key=>own(quote,key) && quote[key] !== undefined);
    const status = typeof quote.verification_status === 'string' ? quote.verification_status.trim().toLowerCase() : null;
    const verified = !suppliedFlags.some(key=>quote[key] !== true) && (!own(quote,'verification_status') || quote.verification_status === undefined || status === 'verified') && (suppliedFlags.some(key=>quote[key] === true) || status === 'verified');
    const sha = sourceSha(source), ownSha = quote.source_sha256 || quote.sha256 || quote.pdf_sha256, pages = array(quote.physical_pdf_page ?? quote.physical_pdf_pages);
    const literal = typeof quote.text === 'string' ? quote.text.trim() : '';
    if (!verified || !literal || sensitive(literal) || typeof source.title !== 'string' || !source.title.trim() || typeof sha !== 'string' || !/^[a-f\d]{64}$/i.test(sha) || typeof ownSha !== 'string' || ownSha.toLowerCase() !== sha.toLowerCase() || typeof sourceEdition(source) !== 'string' || !sourceEdition(source).trim() || !pages.length || !pages.every(page=>Number.isInteger(page) && page>0)) { node('p','chain-muted','Literal excerpt withheld: current verification, exact-edition SHA or physical PDF page binding is not supplied.',parent); return; }
    const count = literal.split(/\s+/u).length, id = context.paperIds.get(source), key = String(id) + '|' + literal.replace(/\s+/gu,' ');
    if (context.shown.has(key) || count > 25 || literal.length > 500 || (context.words.get(id)||0) + count > 25) { node('p','chain-muted','Additional excerpt omitted to avoid repetition or exceeding the shared paper quotation limit.',parent); return; }
    context.shown.add(key); context.words.set(id,(context.words.get(id)||0)+count);
    const block = node('blockquote','chain-excerpt',null,parent); node('p','', '“' + literal + '”',block); node('cite','',text(source.title) + ' · physical PDF page ' + pages.join(', '),block);
  }
  function literature(parent, chain, result, context) {
    const sources = array(chain.literature).filter(object);
    if (!sources.length) node('p','chain-muted','Linked literature is not supplied for this chain.',parent);
    for (const source of sources) {
      const card = node('article','chain-source',null,parent); if (source.id) card.dataset.sourceId = sensitive(String(source.id)) ? 'withheld' : String(source.id);
      node('h4','',text(source.title),card);
      node('p','chain-muted','Source role: ' + text(source.source_role) + ' · Access: ' + text(source.access),card);
      node('p','chain-muted','Edition: ' + text(sourceEdition(source)),card);
      const locators = []; if (source.pdf_page != null) locators.push('Physical PDF page: ' + text(source.pdf_page)); if (source.figure != null) locators.push('Figure: ' + text(source.figure)); if (source.locator != null) locators.push('Location: ' + text(source.locator));
      node('p','chain-muted',locators.join(' · ') || 'Exact source page / figure location not supplied.',card);
      const links = node('div','chain-source-links',null,card); link(links,'Source ↗',source.url); const doi = normalizeDoi(source.doi); if (/^10\.\d{4,9}\/\S+$/i.test(doi)) link(links,'DOI ↗','https://doi.org/' + doi); else link(links,'DOI ↗',source.doi); link(links,'Local PDF ↗',source.local_pdf_url);
      if (sourceSha(source)) node('code','chain-source-sha','SHA-256: ' + text(sourceSha(source)),card);
      renderQuote(card,source,context);
    }
    if (array(result.semantic_sources).length) {
      const leads = section(parent,'retrieval-leads','Retrieved document IDs · search context only');
      node('p','chain-muted','Retrieval links are navigation leads, not independent scientific verification or condition matches.',leads);
      const list = node('ul','chain-notes',null,leads);
      for (const lead of array(result.semantic_sources)) node('li','',object(lead) ? text(lead.document_id || lead.canonical_document_id || lead.id || lead.title || 'Unidentified retrieval lead') : typeof lead === 'string' ? text(lead) : 'Unidentified retrieval lead',list);
    }
  }
  function modelDetails(parent, model, options) {
    if (!object(model)) return node('p','chain-muted','No source-bound model is assigned. Missing model inputs do not become predictions.',parent);
    node('p','chain-model-status','Supplied model status: ' + text(model.status),parent);
    node('p','', 'What it answers: ' + text(model.what_it_answers),parent);
    if (model.equation) { node('h4','', 'Equation and attribution',parent); node('pre','chain-equation',text(model.equation),parent); }
    notes(parent,model.limits,'Model applicability and limitations are not supplied.');
    if (model.source_overlap != null) node('p','chain-muted','Source overlap: ' + text(model.source_overlap),parent);
    node('p','chain-muted','Source-example replay and conservation diagnostics retain their roles; they do not establish independent validation or material-wide transferability.',parent);
    let details = url(model.details_url);
    if (!details && typeof model.id === 'string' && model.id.trim()) details = url(options.physicsUrl || 'http://127.0.0.1:8793/physics.html');
    if (details) link(parent,model.details_url ? 'Open assigned model details ↗' : 'Open advanced model checks ↗',details); else node('p','chain-muted','A detailed model page is not assigned to this chain.',parent);
  }
  function nextQueries(parent, choices, options) {
    const entries = array(choices).filter(object);
    if (!entries.length) return node('p','chain-muted','No source-grounded follow-up choices are supplied.',parent);
    const actions = node('div','chain-next-options',null,parent);
    for (const choice of entries) {
      const terms = Array.isArray(choice.query_terms) ? choice.query_terms.filter(term=>typeof term === 'string').join(' ') : typeof choice.query_terms === 'string' ? choice.query_terms : '';
      const query = terms.trim().slice(0,2000), button = node('button','chain-next-query',text(choice.label),actions); button.type = 'button';
      button.disabled = !query || sensitive(query) || typeof options.onNextQuery !== 'function';
      if (!button.disabled) button.addEventListener('click',()=>options.onNextQuery(query));
    }
  }
  function renderCard(parent, result, index, options, context, ids) {
    const chain = result.chain, card = node('article','chain-card',null,parent); const originalId = typeof chain.id === 'string' && chain.id.trim() && !sensitive(chain.id) ? chain.id : 'unbound-chain-' + (index+1);
    card.dataset.chainId = originalId; let id = 'evidence-chain-' + originalId.replace(/[^a-zA-Z0-9_-]/g,'-').slice(0,180); if (ids.has(id)) id += '-' + (index+1); ids.add(id); card.id = id;
    const ranked=options.isRanked!==false;
    const sources = array(chain.literature).filter(object), primary = sources[0] || {};
    const sourceTitle = typeof primary.title === 'string' && primary.title.trim() ? primary.title : chain.title;
    const sourceURL = url(primary.url), pdfURL = url(primary.local_pdf_url);
    const studies = array(chain.study_ids).map(text), header = node('header','chain-card-header',null,card);
    node('p','chain-rank',(ranked ? 'Search rank ' + (index+1) : 'Source library') + ' · ' + text(chain.pillar || chain.safety_goal) + (studies.length ? ' · ' + studies.join(' · ') : ''),header);
    const title = node('h3','',null,header); title.id = id + '-title'; card.setAttribute('aria-labelledby',title.id);
    if (pdfURL || sourceURL) link(title,text(sourceTitle),pdfURL || sourceURL); else title.textContent = text(sourceTitle);
    node('p','chain-material','Material: ' + text(chain.material),card);
    if (originalId === 'B-PREVENTION-01') node('p','chain-observation observation-hazard','SIBAL · combustion observed in cited test',card);
    node('p','chain-observation observation-unknown','Safety for your scenario: not established',card);
    node('p','chain-preview',text(chain.short_answer || chain.summary),card);
    if (sourceURL || pdfURL) {
      const quick = node('div','chain-quick-links',null,card);
      if (sourceURL) link(quick,'Source ↗',sourceURL);
      if (pdfURL) link(quick,'PDF ↗',pdfURL);
    }
    const details = section(card,'evidence-details','Evidence details'); details.classList.add('result-details');
    node('h4','',text(chain.title),details);
    node('p','chain-review','Review status: ' + text(chain.review_status),details);
    node('p','chain-answer',text(chain.short_answer || chain.summary),details);
    const facets = node('dl','chain-facets',null,details), insight = object(chain.safety_insight) ? chain.safety_insight : {};
    for (const [label,value] of [['Material',chain.material],['Environment match',chain.environment_match || 'Not separately supplied; inspect source conditions'],['Endpoint match',chain.endpoint_match || 'Not separately supplied; inspect physical data'],['Hardware',chain.experiment?.hardware],['Evidence grade',insight.evidence_level]]) { node('dt','',label,facets); node('dd','',text(value),facets); }
    const why = node('section','chain-rank-reasons',null,details); node('h4','', ranked ? 'Why this chain appears' : 'Source scope',why); if(ranked)notes(why,result.rank_reasons,'Grounded ranking reasons are not supplied.'); node('p','chain-muted',ranked ? 'Search order is retrieval relevance, not a safety score, confidence level or proof of matching conditions.' : 'Library browsing is not query-ranked. Inspect the supplied conditions and evidence scope before selecting an experiment.',why);
    const papers = section(details,'literature','Literature and source identity'); literature(papers,chain,result,context);
    const data = section(details,'physical-data','Actual physical data and source conditions'); quantityTable(data,chain.conditions,'Source conditions and their scope',true); quantityTable(data,chain.data,'Actual source-reported physical data',false);
    const closest = section(details,'closest-experiment','Closest source experiment'); const experiment = object(chain.experiment) ? chain.experiment : {};
    node('h4','',text(experiment.name),closest); node('p','', 'Hardware: ' + text(experiment.hardware),closest); node('p','', 'Closest-match basis: ' + text(experiment.closest_match_basis),closest); notes(closest,experiment.limits,'Experimental matching limitations are not supplied.'); node('p','chain-muted','A closest source experiment is a comparison reference, not a prediction for the requested conditions.',closest);
    const model = section(details,'model-status','Model status, equation and scope'); modelDetails(model,chain.model,options);
    const safety = section(details,'safety-insight','Source-bounded safety insight and limitations'); node('p','chain-insight',text(insight.statement || chain.insight),safety); node('p','chain-muted','Evidence level: ' + text(insight.evidence_level),safety); node('p','chain-muted','Applicable scope: ' + text(insight.scope),safety); notes(safety,insight.limits || chain.limitations,'Scope limitations are not supplied.'); node('h4','', 'Hypotheses to test · not established mechanisms',safety); notes(safety,insight.hypotheses,'No mechanism hypothesis is supplied.');
    const next = section(details,'next-queries','Follow-up questions'); nextQueries(next,chain.next_options || chain.next_queries,options);
    return card;
  }
  function clear(container, message) { const root = target(container); if (!root || typeof root.replaceChildren !== 'function') return null; root.replaceChildren(); node('p','chain-empty',message ? text(message) : 'No evidence chains are available for this query. Missing evidence is not a safety verdict.',root); return root; }
  function render(container, rankedResults, options = {}) {
    const root = target(container); if (!root || typeof root.replaceChildren !== 'function') throw new TypeError('Provide a DOM container for the evidence chains.');
    const results = Array.isArray(rankedResults) ? rankedResults.filter(result=>object(result) && object(result.chain)) : [];
    if (!results.length) { clear(root,options.emptyMessage); return {chainCount:0,element:root}; }
    root.replaceChildren(); const sources = results.flatMap(result=>array(result.chain.literature).filter(object)), context = quoteContext(sources), ids = new Set();
    results.forEach((result,index)=>renderCard(root,result,index,options,context,ids));
    return {chainCount:results.length,element:root};
  }
  global.FlameSafetyChainView = Object.freeze({render,clear});
})(typeof window !== 'undefined' ? window : globalThis);
