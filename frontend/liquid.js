/* Read-only liquid comparison client. Predictions and support decisions come from the service. */
(function(global){
  'use strict';
  const $=id=>document.getElementById(id);
  const object=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
  const finite=x=>typeof x==='number'&&Number.isFinite(x);
  const FIELDS=[['diameter_mm','diameter'],['pressure_kpa','pressure'],['oxygen_percent','oxygen']];
  const SCENARIOS=['unignited_baseline','source_experiment'];
  const state={catalog:null,fuel:null,reference:null,serial:0,controller:null,timer:null,paperSerial:0,paperController:null,paperLast:null,phase:'loading',last:null};
  function text(value){if(value==null||value==='')return 'Not supplied';const s=String(value).replace(/\bm2\/s\b/g,'m²/s').replace(/\bm3\/s\b/g,'m³/s');return /(?:^|[\s"'(=])[a-z]:[\\/]|file:\/\/|\\\\[^\\\s]+\\/i.test(s)?'Private source detail withheld':s;}
  function node(tag,cls,value,parent){const el=document.createElement(tag);if(cls)el.className=cls;if(value!=null)el.textContent=text(value);if(parent)parent.append(el);return el;}
  function safeURL(value){if(typeof value!=='string'||!/^https?:\/\//i.test(value))return null;try{const u=new URL(value);return !u.username&&!u.password&&['http:','https:'].includes(u.protocol)?u.href:null;}catch(_){return null;}}
  function link(parent,label,value){const href=safeURL(value);if(!href)return;const el=node('a','',label,parent);el.href=href;el.target='_blank';el.rel='noopener noreferrer';}
  function format(value){if(!finite(value))return 'Not available';if(value===0)return '0';const a=Math.abs(value);return a<.001||a>=1e6?value.toExponential(3):Number(value.toPrecision(5)).toString();}
  function boundedArray(value,label){if(!Array.isArray(value)||value.length>2000)throw Error('Invalid '+label+' response.');return value;}
  function validateOperatingChecks(value){if(value==null)return;if(!object(value)||!['conditional_pass','fail','unknown'].includes(value.status))throw Error('Operating-check status unavailable.');for(const check of boundedArray(value.checks||[],'operating criteria')){if(!object(check)||typeof check.label!=='string'||!['pass','fail','pending'].includes(check.status))throw Error('Invalid operating criterion.');for(const key of ['input','min','max'])if(check[key]!=null&&!finite(check[key]))throw Error('Operating limits require finite values.');}boundedArray(value.pending||[],'pending operating criteria');}
  function validateCatalog(payload){
    if(!object(payload)||payload.schema_version!=='liquid-catalog-v1')throw Error('Liquid evidence catalog unavailable.');
    const ids=new Set();for(const fuel of boundedArray(payload.fuels,'fuel catalog')){
      if(!object(fuel)||typeof fuel.id!=='string'||!fuel.id||ids.has(fuel.id)||typeof fuel.label!=='string')throw Error('Invalid fuel identity.');ids.add(fuel.id);
      const cases=new Set();for(const row of boundedArray(fuel.cases,'reference experiments')){
        if(!object(row)||typeof row.id!=='string'||!row.id||cases.has(row.id))throw Error('Invalid reference identity.');cases.add(row.id);
        for(const [key] of FIELDS)if(!finite(row[key]))throw Error('Reference controls require finite source values.');
      }
      if(!object(fuel.controls))throw Error('Missing control ranges.');
      for(const [key] of FIELDS){const range=fuel.controls[key];if(!object(range)||![range.min,range.max,range.step].every(finite)||range.min>=range.max||range.step<=0)throw Error('Invalid control range.');}
      if(fuel.cases.length&&(!object(fuel.baseline)||FIELDS.some(([key])=>!finite(fuel.baseline[key]))))throw Error('Unignited scenario preset unavailable.');
      if(fuel.demo_preset&&(!object(fuel.demo_preset)||FIELDS.some(([key])=>!finite(fuel.demo_preset[key]))||!cases.has(fuel.demo_preset.reference_id)))throw Error('Supported example preset unavailable.');
    }return payload;
  }
  function validateComparison(payload){
    if(!object(payload)||payload.schema_version!=='liquid-compare-v1'||!object(payload.input)||!object(payload.reference)||!object(payload.support))throw Error('Comparison response unavailable.');
    if(!['exact_record','within_surface_support','outside_surface_support','within_marginal_ranges','outside_data_range','insufficient_evidence','unavailable'].includes(payload.support.status)||typeof payload.reference_matches_input!=='boolean')throw Error('Input support status was not established.');
    if(!SCENARIOS.includes(payload.scenario)||payload.input.scenario!==payload.scenario)throw Error('Scenario identity was not established.');
    for(const m of [...boundedArray(payload.metrics,'comparison metrics'),...boundedArray(payload.stored_metrics||[],'stored reference metrics')]){
      if(!object(m)||typeof m.id!=='string'||typeof m.label!=='string'||typeof m.unit!=='string')throw Error('Invalid comparison quantity.');
      for(const key of ['observed','predicted'])if(m[key]!==null&&!finite(m[key]))throw Error('Metric values must be finite numbers or null.');
    }
    const exactReplay=payload.support.status==='exact_record'&&payload.reference_matches_input&&payload.prediction_mode==='stored_prediction_replay';
    const surfaceInterpolation=payload.support.status==='within_surface_support'&&payload.prediction_mode==='stored_output_interpolation'&&payload.input.prediction_method==='stored_surface'&&payload.scenario==='source_experiment';
    if(payload.metrics.some(m=>m.predicted!==null)&&!exactReplay&&!surfaceInterpolation)throw Error('Unsupported scenario returned a prediction.');
    if(surfaceInterpolation&&payload.metrics.some(m=>m.observed!==null))throw Error('An interpolation was presented as an observation.');
    if(!payload.reference_matches_input&&payload.metrics.some(m=>m.observed!==null))throw Error('A reference observation was assigned to different input conditions.');
    if(payload.scenario==='unignited_baseline'&&payload.metrics.some(m=>m.observed!==null||m.predicted!==null))throw Error('Burning data were assigned to an unignited scenario.');
    validateOperatingChecks(payload.operating_checks);
    return payload;
  }
  function support(title,message,kind='unknown'){$('liquid-support').hidden=false;$('liquid-support').className='liquid-support support-'+kind;$('support-title').textContent=title;$('support-message').textContent=text(message);}
  function modelSupport(payload){let kind='pending',title='MODEL DATA SUPPORT: PENDING';if(payload){const rows=Array.isArray(payload.metrics)?payload.metrics:[],validMode=payload.prediction_mode==='stored_prediction_replay'&&payload.support?.status==='exact_record'||payload.prediction_mode==='stored_output_interpolation'&&payload.support?.status==='within_surface_support';const available=validMode?rows.filter(row=>finite(row.predicted)).length:0;if(available&&available===rows.length){kind='pass';title='MODEL DATA SUPPORT: PASS';}else if(available){kind='partial';title='MODEL DATA SUPPORT: PARTIAL SUPPORT';}else{kind='outside';title='OUTSIDE MODEL SUPPORT';}}$('model-data-support').className='model-data-support model-support-'+kind;$('model-support-title').textContent=title;}
  function clearOutput(message){$('liquid-metrics').replaceChildren();node('p','empty-state',message,$('liquid-metrics'));$('liquid-chart').replaceChildren();$('liquid-chart').hidden=true;$('liquid-research').replaceChildren();$('liquid-research').hidden=true;$('prediction-mode').textContent='';$('comparison-context').textContent='';$('liquid-source-details').replaceChildren();$('liquid-validation-content').replaceChildren();state.last=null;}
  function pending(){state.phase='pending';support('CHECKING DATA SUPPORT','Safety remains unestablished while the comparison loads.');clearOutput('Loading comparison…');$('liquid-compare').setAttribute('aria-busy','true');}
  function enabled(value){for(const id of ['liquid-fuel','liquid-scenario','liquid-reference','liquid-compare','liquid-reset',...FIELDS.flatMap(([,id])=>[id+'-range',id+'-value'])])$(id).disabled=!value;}
  function scenario(){return $('liquid-scenario').value==='unignited_baseline'?'unignited_baseline':'source_experiment';}
  function safetyScenario(payload){const checks=payload?.operating_checks,titles={conditional_pass:'SAFETY CHECK: PASS',fail:'SAFETY CHECK: FAIL',unknown:'SAFETY CHECK: UNKNOWN'},valid=object(checks)&&Object.hasOwn(titles,checks.status);$('liquid-safety').className='safety-assessment '+(valid&&checks.status==='fail'?'assessment-outside':valid&&checks.status==='conditional_pass'?'assessment-pass':'assessment-unknown');$('liquid-safety-title').textContent=valid?titles[checks.status]:'SAFETY CHECK: UNKNOWN';$('liquid-safety-message').textContent=valid?text(checks.message||checks.scope):'Peak chamber pressure, thermal load and containment failure are not predicted.';operatingCriteria(valid?checks:null);}
  function operatingCriteria(checks){const details=$('operating-criteria'),root=$('operating-criteria-content');root.replaceChildren();details.hidden=!checks;if(!checks)return;node('p','',checks.scope||'Selected archived protocol checks, not complete equipment approval.',root);const rows=node('ul','operating-check-list',null,root);for(const check of checks.checks||[]){const li=node('li','operating-check-'+check.status,null,rows);node('strong','',check.label,li);const unit=typeof check.unit==='string'?check.unit:'',input=finite(check.input)?format(check.input)+(unit?' '+unit:''):'Unknown',limit=finite(check.min)&&finite(check.max)?format(check.min)+'–'+format(check.max):finite(check.max)?'≤ '+format(check.max):finite(check.min)?'≥ '+format(check.min):'Pending';node('p','',input+' · archived limit '+limit+(unit?' '+unit:'')+' · '+check.status.toUpperCase(),li);link(li,(check.source_title||'Archived source')+(check.pdf_page!=null?' · p. '+text(check.pdf_page):'')+' ↗',check.source_url);}if(checks.pending?.length){node('h3','', 'Still pending',root);list(root,checks.pending);}}

  function selectedFuel(){return state.catalog?.fuels.find(f=>f.id===$('liquid-fuel').value)||null;}
  function selectedReference(){return state.fuel?.cases.find(c=>c.id===$('liquid-reference').value)||null;}
  function refinements(options){const chips=$('scenario-followups');chips.replaceChildren();for(const option of options){if(!object(option)||typeof option.label!=='string'||typeof option.query!=='string')continue;const button=node('button','',option.label,chips);button.type='button';button.addEventListener('click',()=>{$('liquid-query').value=option.query;filterFuels();});}chips.hidden=!chips.children.length;}
  function liquidRefinements(){const base=(state.fuel?.source_fuel||state.fuel?.label?.split(' · ')[0]||'C12H26')+' droplets';return [['Oxygen concentration','oxygen concentration'],['Pressure','pressure'],['Droplet size','initial droplet diameter'],['Hot / cool flames','hot cool flame transition'],['Dilution','helium carbon dioxide dilution']].map(([label,term])=>({label,query:base+' '+term}));}
  function normalizeQuery(value){return String(value).normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu,' ').trim();}
  function filterFuels(){
    if(!state.catalog)return;invalidate();const query=$('liquid-query').value.trim(),tokens=normalizeQuery(query).split(' ').filter(Boolean),gasQuery=/lighter|打火機|propane|丙烷|butane|丁烷/i.test(query);
    const ratio=/60\D{0,8}40/.test(query)?'60/40':/75\D{0,8}25/.test(query)?'75/25':null,wantsBlend=Boolean(ratio)||/iso.?dodecane/i.test(query)||/dodecane|十二烷|C12H26/i.test(query)&&/blend|fuel mixture|混合燃料/i.test(query);const matches=state.catalog.fuels.filter(fuel=>{if(wantsBlend&&fuel.formulation_kind&&fuel.formulation_kind!=='binary_blend')return false;if(ratio&&fuel.formulation_kind&&(!fuel.label.includes(ratio)||fuel.formulation_kind!=='binary_blend'))return false;const aliases=[fuel.label,fuel.id,...(Array.isArray(fuel.search_terms)?fuel.search_terms:[])],haystack=normalizeQuery(aliases.join(' '));return tokens.every(token=>haystack.includes(token))||aliases.some(alias=>normalizeQuery(alias).length>=2&&normalizeQuery(query).replaceAll(' ','').includes(normalizeQuery(alias).replaceAll(' ','')));});
    const select=$('liquid-fuel');select.replaceChildren();state.fuel=null;state.reference=null;$('liquid-scenario').value='source_experiment';safetyScenario();$('liquid-literature-link').hidden=true;$('liquid-reference').replaceChildren();
    const hasLiquid=matches.length>0&&!gasQuery;void searchScenario(query,hasLiquid);
    if(!hasLiquid){enabled(false);return;}
    if(!matches.length){const placeholder=node('option','', 'No matching fuel dataset',select);placeholder.value='';}
    for(const fuel of matches){const option=node('option','',fuel.label,select);option.value=fuel.id;}
    if(matches.length){select.value=(matches.find(fuel=>fuel.id===state.catalog.default_fuel)||matches[0]).id;$('liquid-search-status').textContent=matches.length+' matching fuel dataset'+(matches.length===1?'':'s')+' · chamber test preset loaded';showReferences();return;}
    select.value='';enabled(false);select.disabled=!matches.length;state.phase=matches.length?'selection':'no_match';clearOutput(matches.length?'Choose a matching fuel dataset to load its preset.':'No data match this fuel search. Try a fuel name or formula.');$('liquid-search-status').textContent=matches.length+' matching fuel datasets';support(matches.length?'CHOOSE A MATCHING FUEL':'NO MATCHING FUEL',matches.length?'Select one of the matching datasets.':'No earlier result is being used.');$('mixture-context').textContent='';
  }
  function showReferences(){
    invalidate();
    $('liquid-controls').hidden=false;$('liquid-workspace').className='liquid-workspace';$('liquid-result-heading').textContent='Model prediction';$('liquid-details').hidden=false;$('liquid-validation').hidden=false;$('liquid-validation').open=false;$('scenario-data-details').hidden=true;
    state.fuel=selectedFuel();const root=$('liquid-reference');root.replaceChildren();
    for(const row of state.fuel?.cases||[]){const option=node('option','',row.label||row.id,root);option.value=row.id;}
    root.value=state.fuel?.default_reference_id||state.fuel?.cases[0]?.id||'';
    if(!state.fuel?.cases.length){enabled(false);$('liquid-fuel').disabled=false;support('NO COMPLETE REFERENCE','No complete source experiment is available for this fuel.');clearOutput('No comparison values supplied.');return;}
    enabled(true);$('liquid-scenario').value='source_experiment';setReference();
  }
  function setReference(){
    state.reference=selectedReference();if(!state.reference)return;
    const baseline=scenario()==='unignited_baseline',preset=baseline?{...state.fuel.baseline,diameter_mm:state.reference.diameter_mm}:state.fuel.demo_preset||state.reference;
    if(!baseline&&preset.reference_id){const anchor=state.fuel.cases.find(row=>row.id===preset.reference_id);if(anchor){state.reference=anchor;$('liquid-reference').value=anchor.id;}}
    for(const [key,id] of FIELDS){const bounds=state.fuel.controls[key],slider=$(id+'-range'),number=$(id+'-value');const exploration=key==='oxygen_percent'?{min:0,max:Math.max(40,bounds.max)}:key==='pressure_kpa'?{min:Math.min(25,bounds.min),max:Math.max(600,bounds.max)}:bounds;slider.setAttribute('min',String(Math.min(exploration.min,preset[key])));slider.setAttribute('max',String(Math.max(exploration.max,preset[key])));slider.setAttribute('step',String(bounds.step));number.setAttribute('min','0');number.setAttribute('step','any');if(key==='oxygen_percent')number.setAttribute('max','100');slider.value=String(preset[key]);number.value=String(preset[key]);}
    $('mixture-context').textContent=baseline?'Room-air preset: 101.325 kPa, 21 mol% O₂. Temperature is not measured or modeled.':text(state.reference.mixture_context||state.fuel.mixture_context||'Additional mixture conditions remain bound to the reference experiment.');
    $('liquid-literature-link').href='./index.html?q='+encodeURIComponent(state.fuel.fuel||state.fuel.name||state.fuel.label);$('liquid-literature-link').hidden=false;safetyScenario();
    queueComparison(0);
  }
  function readInput(){
    if(!state.fuel||!state.reference)throw Error('Select a fuel and reference experiment.');
    const value={fuel:state.fuel.id,reference_id:state.reference.id,reference_policy:'nearest_compatible',prediction_method:'stored_surface',scenario:scenario()};
    for(const [key,id] of FIELDS){const raw=$(id+'-value').value;if(typeof raw!=='string'||!raw.trim())throw Error('Enter all three physical conditions.');value[key]=Number(raw);if(!finite(value[key]))throw Error('Enter finite physical conditions.');}
    if(value.diameter_mm<=0||value.pressure_kpa<=0||value.oxygen_percent<0||value.oxygen_percent>100)throw Error('Use positive diameter/pressure and oxygen between 0 and 100 mol%.');
    return value;
  }
  function invalidate(){++state.serial;state.controller?.abort();state.controller=null;if(state.timer!==null){clearTimeout(state.timer);state.timer=null;}safetyScenario();modelSupport();}
  function queueComparison(delay=220){invalidate();pending();const serial=state.serial;state.timer=setTimeout(()=>{state.timer=null;if(serial===state.serial)void compare();},delay);}
  function changed(key,id,fromRange){const source=$(id+(fromRange?'-range':'-value')),target=$(id+(fromRange?'-value':'-range'));target.value=source.value;queueComparison();}
  function list(parent,values,empty){const rows=Array.isArray(values)?values:[];if(!rows.length){if(empty)node('p','',empty,parent);return;}const ul=node('ul','',null,parent);for(const row of rows)node('li','',object(row)?row.message||row.reason||row.label||'Source qualification supplied':row,ul);}
  function details(payload){
    const root=$('liquid-source-details');root.replaceChildren();const reference=payload.reference;
    node('h3','',reference.label||reference.id,root);const dl=node('dl','',null,root);
    const fields=[['Fuel formulation',state.fuel?.description||state.fuel?.label],['Reported fuel label',reference.fuel],['Dataset',reference.dataset],['Test',reference.test_id],['Source location',reference.source_locator],['Comparison role','Matched source experiment; not a measurement at every slider position']];
    for(const [label,value] of fields){node('dt','',label,dl);node('dd','',value,dl);}
    if(object(reference.conditions)){const conditions=node('dl','',null,root);for(const [label,value] of Object.entries(reference.conditions)){node('dt','',conditionLabel(label),conditions);node('dd','',object(value)?value.display_value||value.display||'Source-defined condition':value,conditions);}}
    link(root,'NASA source ↗',reference.source_url);if(reference.source_sha256)node('p','', 'Source SHA-256: '+text(reference.source_sha256),root);
    node('h3','', 'Operating safety',root);node('p','', 'Archived protocol checks are separate from model-output support. Dynamic pressure, thermal load, containment and full procedure compliance remain unverified.',root);const model=object(payload.model)?payload.model:{};node('h3','', 'Model and prediction identity',root);if(model.id)node('p','', 'Model: '+model.id,root);if(model.method||!model.id)node('p','',model.method||'Existing model details not supplied',root);if(model.equation)node('p','',model.equation,root);
    list(root,model.limits,'No further model limits supplied.');list(root,payload.support.reasons);list(root,payload.warnings);
    if(payload.prediction_mode==='stored_output_interpolation'){node('h3','', 'Stored-output interpolation',root);node('p','', 'Geometric interpolation of stored predictions, not a rerun of the original regression. Uncertainty is unknown.',root);for(const row of payload.metrics){const interpolation=row.interpolation;if(!object(interpolation))continue;node('h3','',row.label,root);const contributors=Array.isArray(interpolation.contributors)?interpolation.contributors:[];node('p','', 'Log-output barycentric interpolation · '+contributors.length+' source outputs',root);const ul=node('ul','',null,root);for(const source of contributors)node('li','',text(source.source_id)+' · weight '+format(source.weight)+' · '+text(source.validation_kind)+(source.fold==null?'':' · fold '+text(source.fold)),ul);}}
    for(const row of payload.reference_matches_input?payload.metrics:payload.stored_metrics||[]){const metadata=object(row.metadata)?row.metadata:{};if(!metadata.model_id&&!metadata.scope)continue;node('h3','',row.label,root);if(metadata.model_id)node('p','', 'Model: '+metadata.model_id,root);if(metadata.scope)node('p','',metadata.scope,root);}
  }
  function predictionProvenance(cell,row){
    if(row.predicted===null)return;
    const metadata=object(row.metadata)?row.metadata:{};let validation;
    if(metadata.validation_kind==='group_held_out')validation='Held-out '+(metadata.fold==null?'estimate · fold unknown':'fold '+metadata.fold);
    else if(metadata.validation_kind==='full_fit_unlabelled_row')validation='Full-fit estimate (no held-out target)';
    else validation=row.status&&row.status!=='stored_source_values'?row.status:'Stored estimate · validation unknown';
    node('small','liquid-validation',validation,cell);
    if(metadata.domain==='held_out_extrapolation')node('small','liquid-domain-outside','Outside fold training range',cell);
  }
  function metricTable(root,rows,predictionLabel){
    if(!rows.length){node('p','empty-state','No supported comparison quantities for this source.',root);return;}
    const wrap=node('div','liquid-table-wrap',null,root);wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label','Source measurements and model predictions');
    const table=node('table','liquid-table',null,wrap),head=node('tr','',null,node('thead','',null,table));
    for(const label of ['Quantity','Reported experiment',predictionLabel]){const th=node('th','',label,head);th.scope='col';}
    const body=node('tbody','',null,table);
    for(const row of rows){const tr=node('tr','',null,body),th=node('th','',row.label,tr);th.scope='row';node('small','',row.unit,th);const observed=node('td',row.observed===null?'liquid-missing':'liquid-reported',format(row.observed),tr);if(row.observed===null)observed.textContent='Not reported';const predicted=node('td',row.predicted===null?'liquid-missing':'',row.predicted===null?'Withheld':format(row.predicted),tr);if(finite(row.observed)&&row.observed!==0&&finite(row.predicted)){const error=finite(row.relative_error_percent)?Math.abs(row.relative_error_percent):100*Math.abs(row.predicted-row.observed)/Math.abs(row.observed);node('small','liquid-model-error','Absolute error '+error.toFixed(1)+'% vs experiment',predicted);}predictionProvenance(predicted,row);if(row.scope)node('small','',row.scope,th);}
  }
  function metrics(payload){const root=$('liquid-metrics');root.replaceChildren();const table=node('table','liquid-table liquid-model-table',null,root),head=node('tr','',null,node('thead','',null,table));for(const label of ['Quantity','Model prediction']){const th=node('th','',label,head);th.scope='col';}const body=node('tbody','',null,table);for(const row of payload.metrics){const tr=node('tr','',null,body),th=node('th','',row.label,tr);th.scope='row';node('small','',row.unit,th);const td=node('td',row.predicted===null?'liquid-missing':'liquid-primary-prediction',row.predicted===null?'Withheld':format(row.predicted),tr);if(payload.prediction_mode!=='stored_output_interpolation')predictionProvenance(td,row);}}
  function validation(payload){const root=$('liquid-validation-content');root.replaceChildren();node('p','', 'Matched experiment: '+text(payload.reference.label||payload.reference.id),root);node('p','',conditionLine(payload.reference.conditions),root);if(!payload.reference_matches_input)node('p','liquid-reference-mismatch',payload.scenario==='unignited_baseline'?'Ignited reference experiment only — not an unignited scenario prediction.':'Matched source comparison only — not predictions at requested conditions.',root);const rows=payload.reference_matches_input?payload.metrics:payload.stored_metrics||[];metricTable(root,rows,'Model estimate');}
  function chart(payload){
    const root=$('liquid-chart');root.replaceChildren();const rows=payload.scenario==='unignited_baseline'?[]:payload.metrics.filter(r=>finite(r.observed)&&finite(r.predicted)&&r.observed>=0&&r.predicted>=0&&(r.observed>0||r.predicted>0));
    root.hidden=!rows.length;if(!rows.length)return;node('h3','', 'Exact-record comparison',root);node('p','', 'Source-analyzed values and stored model estimates. Each quantity uses its own scale; this is not a simulated time history.',root);
    const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 650 '+(rows.length*58+24));svg.setAttribute('role','img');svg.setAttribute('aria-label','Scalar source values compared with model estimates; each row has its own scale');root.append(svg);
    function shape(tag,attrs,value){const el=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))el.setAttribute(k,String(v));if(value!=null)el.textContent=text(value);svg.append(el);return el;}
    rows.forEach((r,i)=>{const y=i*58+20,max=Math.max(r.observed,r.predicted)*1.12,start=220,length=330;shape('text',{x:0,y},r.label+' ('+r.unit+')');shape('line',{x1:start,y1:y+7,x2:start+length,y2:y+7,stroke:'#d9e2da'});shape('circle',{cx:start+length*r.observed/max,cy:y+7,r:4,fill:'#2e6a48'});shape('rect',{x:start+length*r.predicted/max-4,y:y+3,width:8,height:8,fill:'#956119'});shape('text',{x:start,y:y+27},'Source '+format(r.observed));shape('text',{x:420,y:y+27},'Model '+format(r.predicted));});
  }
  function conditionLabel(key){return ({diameter_mm:'Initial diameter (mm)',pressure_kpa:'Pressure (kPa)',oxygen_percent:'O₂ (mol%)',helium_percent:'He (mol%)',carbon_dioxide_percent:'CO₂ (mol%)',nitrogen_percent:'N₂ (mol%)'})[key]||key;}
  function conditionLine(conditions){return ['diameter_mm','pressure_kpa','oxygen_percent','helium_percent','carbon_dioxide_percent','nitrogen_percent'].map(key=>conditionLabel(key)+': '+(finite(conditions?.[key])?format(conditions[key]):'Unknown')).join(' · ');}
  function research(payload,target='liquid-research',heading='Source investigations'){const root=$(target);root.replaceChildren();const studies=Array.isArray(payload.studies)?payload.studies.slice(0,target==='paper-results'?8:4):[];root.hidden=!studies.length;if(!studies.length)return;node('h2','',heading,root);const cards=node('div','liquid-research-cards',null,root);for(const study of studies){if(!object(study)||typeof study.title!=='string')continue;const article=node('article','',null,cards);node('h3','',study.title,article);const links=node('p','',null,article);link(links,'Source ↗',study.source_url||study.url);link(links,'NASA data ↗',study.data_url||study.nasa_data_url);if(study.summary&&target!=='paper-results')node('p','liquid-study-summary',study.summary,article);for(const range of Array.isArray(study.parameter_ranges)?study.parameter_ranges:[]){if(!object(range))continue;node('div','liquid-source-ranges',text(range.label)+': '+format(range.min)+'–'+format(range.max)+' '+text(range.unit)+(range.scope?' · '+text(range.scope):''),article);}}}
  function render(payload){
    const supportState=payload.support,labels={exact_record:['EXACT SOURCE RECORD · STORED COMPARISON','unknown'],within_surface_support:['STORED-OUTPUT INTERPOLATION','unknown'],outside_surface_support:['OUTSIDE STORED-OUTPUT SUPPORT','outside'],within_marginal_ranges:['WITHIN CHECKED INPUT RANGES · PREDICTION WITHHELD','unknown'],outside_data_range:['OUTSIDE DATA RANGE','outside'],insufficient_evidence:['PREDICTION WITHHELD','unknown'],unavailable:['MODEL UNAVAILABLE','unavailable']};
    let [title,kind]=labels[supportState.status];let message=supportState.message||'Inspect the supporting conditions and limits.';
    if(payload.scenario==='unignited_baseline'){title=supportState.status==='outside_data_range'?'OUTSIDE DATA RANGE · UNIGNITED SCENARIO':'UNIGNITED SCENARIO · SAFETY UNDETERMINED';message='Post-ignition models do not establish ignition or safety for this scenario.';}
    if(payload.prediction_mode==='unavailable_missing_frozen_model')message+=' New-condition predictions are withheld: frozen model coefficients are unavailable.';
    support(title,message,kind);
    const modes={stored_prediction_replay:'Stored prediction at recorded condition',stored_output_interpolation:'Interpolated stored-model output',unavailable_outside_surface_support:'Prediction withheld · outside stored-output support',unavailable_missing_frozen_model:'New prediction withheld · model coefficients unavailable',unavailable_unignited_scenario:'No burning prediction for baseline'};
    $('prediction-mode').className='prediction-badge';$('prediction-mode').textContent=modes[payload.prediction_mode]||text(payload.prediction_mode||'Prediction identity not supplied');
    const context=$('comparison-context');context.replaceChildren();node('p','', 'Requested: diameter '+format(payload.input.diameter_mm)+' mm · '+format(payload.input.pressure_kpa)+' kPa · O₂ '+format(payload.input.oxygen_percent)+' mol%',context);
    if(!payload.reference_matches_input&&payload.scenario!=='unignited_baseline'&&payload.prediction_mode!=='stored_output_interpolation')node('p','liquid-reference-mismatch','Entered conditions differ; new prediction withheld.',context);
    safetyScenario(payload);modelSupport(payload);$('liquid-support').hidden=true;research(payload);metrics(payload);validation(payload);$('liquid-chart').replaceChildren();$('liquid-chart').hidden=true;details(payload);state.last=payload;state.phase='ready';
  }
  async function requestJSON(url,options={}){const response=await global.fetch(url,{cache:'no-store',...options});if(!response.ok)throw Error('Liquid comparison service unavailable (HTTP '+response.status+').');return response.json();}
  async function searchScenario(query,hasLiquid=false){
    global.FlameStrategySearchLinks?.sync({phase:'loading',query});
    const serial=++state.paperSerial;state.paperController?.abort();state.paperController=new AbortController();state.paperLast=null;$('paper-results').replaceChildren();$('paper-results').hidden=false;node('p','empty-state','Searching related papers…',$('paper-results'));$('scenario-followups').replaceChildren();$('scenario-followups').hidden=true;
    if(!hasLiquid){state.phase='scenario_loading';$('liquid-controls').hidden=true;$('liquid-workspace').className='liquid-workspace gas-context';$('liquid-details').hidden=true;$('liquid-validation').hidden=true;$('scenario-data-details').hidden=true;$('liquid-result-heading').textContent='Model prediction';clearOutput('Searching related investigations…');support('SEARCHING RESEARCH','Finding fuel and scenario evidence.');safetyScenario();}$('liquid-search-status').textContent='Searching related papers…';
    try{
      const payload=await requestJSON('/api/scenario/search',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({query}),signal:state.paperController.signal});if(serial!==state.paperSerial)return;
      if(!object(payload)||payload.schema_version!=='scenario-search-v1'||payload.query!==query||!object(payload.context)||!object(payload.assessment)||payload.assessment.status!=='not_established'||!object(payload.prediction)||payload.prediction.available!==false)throw Error('Scenario evidence response unavailable.');
      boundedArray(payload.studies,'scenario investigations');boundedArray(payload.follow_up_options||[],'search refinements');
      validateOperatingChecks(payload.operating_checks);
      research(payload,'paper-results','Related papers');if(!payload.studies.length){$('paper-results').hidden=false;node('p','empty-state','No related papers were found for this query.',$('paper-results'));}
      if(!hasLiquid){$('liquid-support').hidden=true;$('liquid-safety').className='safety-assessment assessment-unknown';safetyScenario(payload);const context=$('comparison-context');context.replaceChildren();if(payload.context.title)node('p','liquid-context-title',payload.context.title,context);node('p','',payload.context.summary||'Fuel and environment require further specification.',context);research({studies:payload.datasets||[]},'scenario-datasets','Related experimental data');$('scenario-data-details').hidden=!(payload.datasets||[]).length;modelSupport({metrics:[]});$('prediction-mode').textContent='No numerical prediction';$('liquid-metrics').replaceChildren();node('p','empty-state',payload.prediction.reason||'No supported numerical model is available for this scenario.',$('liquid-metrics'));state.phase=payload.studies.length?'scenario_ready':'no_match';state.last=payload;}
      refinements(payload.follow_up_options||[]);
      $('liquid-literature-link').href='./index.html?q='+encodeURIComponent(query);$('liquid-literature-link').hidden=false;$('liquid-search-status').textContent=payload.studies.length+' related paper'+(payload.studies.length===1?'':'s')+(payload.search_mode?' · '+text(payload.search_mode).replaceAll('_',' '):'');state.paperLast=payload;
      global.FlameStrategySearchLinks?.sync({phase:'ready',query});
    }catch(error){if(serial!==state.paperSerial||error.name==='AbortError')return;$('paper-results').replaceChildren();node('p','empty-state','Paper search unavailable; no earlier results are being reused.',$('paper-results'));if(!hasLiquid){state.phase='unavailable';support('SCENARIO SEARCH UNAVAILABLE',error.message,'unavailable');clearOutput('No earlier result or numerical prediction is being used.');}$('liquid-search-status').textContent='Paper search unavailable';}
  }
  async function compare(){
    invalidate();let input;try{input=readInput();}catch(error){support('CHECK THE INPUTS',error.message);clearOutput('No prediction was requested.');$('liquid-compare').setAttribute('aria-busy','false');state.phase='invalid';return;}
    const serial=state.serial;state.controller=new AbortController();pending();
    try{const payload=validateComparison(await requestJSON('/api/liquid/compare',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(input),signal:state.controller.signal}));if(serial!==state.serial)return;for(const key of ['fuel','reference_id','scenario','prediction_method','reference_policy',...FIELDS.map(([key])=>key)])if(payload.input[key]!==input[key])throw Error('The service returned different comparison conditions.');render(payload);}
    catch(error){if(serial!==state.serial||error.name==='AbortError')return;state.phase='unavailable';modelSupport({metrics:[]});support('COMPARISON UNAVAILABLE',error.message,'unavailable');clearOutput('No current prediction or safety verdict is available.');}
    finally{if(serial===state.serial)$('liquid-compare').setAttribute('aria-busy','false');}
  }
  async function init(){
    enabled(false);$('paper-results').hidden=true;$('liquid-scenario').value='source_experiment';safetyScenario();$('liquid-controls').addEventListener('submit',e=>{e.preventDefault();void compare();});$('liquid-fuel').addEventListener('change',()=>{showReferences();if(state.fuel){$('liquid-query').value=state.fuel.fuel||state.fuel.name||state.fuel.label;void searchScenario($('liquid-query').value,true);}});$('liquid-scenario').addEventListener('change',setReference);$('liquid-reference').addEventListener('change',setReference);$('liquid-reset').addEventListener('click',()=>{$('liquid-scenario').value='source_experiment';setReference();});$('liquid-search-form').addEventListener('submit',e=>{e.preventDefault();filterFuels();});$('liquid-query').addEventListener('input',filterFuels);
    for(const [key,id] of FIELDS){$(id+'-range').addEventListener('input',()=>changed(key,id,true));$(id+'-value').addEventListener('input',()=>changed(key,id,false));}
    try{state.catalog=validateCatalog(await requestJSON('/api/liquid/catalog'));const select=$('liquid-fuel');select.replaceChildren();for(const f of state.catalog.fuels){const option=node('option','',f.label,select);option.value=f.id;}select.value=state.catalog.default_fuel||state.catalog.fuels[0]?.id||'';if(!state.catalog.fuels.length)throw Error('No reviewed liquid fuels are available.');$('liquid-query').disabled=false;$('liquid-search').disabled=false;$('liquid-search-status').textContent=state.catalog.fuels.length+' available fuel datasets';const initialQuery=new URL(global.location?.href||'http://localhost/').searchParams.get('q');if(initialQuery){$('liquid-query').value=initialQuery;filterFuels();}else{showReferences();refinements(liquidRefinements());}}
    catch(error){state.phase='unavailable';support('LIQUID DATA UNAVAILABLE',error.message,'unavailable');clearOutput('No data have been substituted.');}
  }
  global.FlameLiquid=Object.freeze({init,compare,validateCatalog,validateComparison,format,getState:()=>({phase:state.phase,fuel:state.fuel?.id||null,reference:state.reference?.id||null,last:state.last,papers:state.paperLast})});
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>void init(),{once:true});else void init();
})(typeof window!=='undefined'?window:globalThis);
