/* Habitat navigation over supplied, reviewed relationships. No scientific fallback data. */
(function (root, factory) {
  'use strict';
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.HabitatFireAtlas = api;
  if (root && root.document) {
    const boot = () => api.createApp({ window: root, document: root.document, fetch: root.fetch.bind(root) }).start();
    if (root.document.readyState === 'loading') root.document.addEventListener('DOMContentLoaded', boot, { once: true });
    else boot();
  }
})(typeof window !== 'undefined' ? window : null, function () {
  'use strict';
  const HABITATS = Object.freeze(['space_station', 'crew_spacecraft', 'lunar_base', 'mars_base', 'pressurized_rover']);
  const FIRE_TYPES = Object.freeze(['solid_material_fire', 'electrical_overheating_smoke', 'liquid_fuel_fire', 'gaseous_fuel_fire']);
  const WORLDS = Object.freeze(['moon', 'mars']);
  const RELATIONSHIPS = Object.freeze(['direct', 'analogue', 'related', 'hypothesis', 'unknown']);
  const PAGES = new Set(['/index.html', '/strategies.html', '/liquid.html', '/gas-case.html']);
  const API = '/api/habitat-atlas';
  const GRAVITY_LABELS = Object.freeze({ microgravity: 'Microgravity research context', mission_phase_dependent: 'Gravity depends on mission phase', lunar_partial_gravity: 'Lunar surface context', martian_partial_gravity: 'Mars surface context', moon_or_mars_partial_gravity: 'Partial gravity · analogue' });
  const RELATIONSHIP_LABELS = Object.freeze({ direct: 'Direct', analogue: 'Analogue', related: 'Related', hypothesis: 'Hypothesis', unknown: 'Unknown' });
  const valueText = value => typeof value === 'string' ? value : '';
  const unique = values => [...new Set(values)];
  function refs(value) {
    if (value == null) return [];
    if (!Array.isArray(value) || value.some(v => typeof v !== 'string')) throw Error('Invalid references');
    return unique(value);
  }
  function registry(items, name) {
    if (!Array.isArray(items)) throw Error('Missing ' + name);
    const result = new Map();
    for (const item of items) {
      if (!item || typeof item !== 'object' || typeof item.id !== 'string' || !/^[A-Za-z0-9_.:-]{1,160}$/.test(item.id) || result.has(item.id)) throw Error('Invalid ' + name);
      result.set(item.id, item);
    }
    return result;
  }
  function normalizePayload(payload) {
    if (!payload || typeof payload !== 'object' || typeof payload.schema_version !== 'string' || payload.status !== 'reviewed_qualitative_navigation_mapping') throw Error('Reviewed atlas required');
    const data = {
      title: valueText(payload.title), habitats: registry(payload.habitats, 'habitats'),
      fireTypes: registry(payload.fire_types, 'fire types'), datasets: registry(payload.datasets, 'datasets'),
      insights: registry(payload.insights, 'insights'), sources: registry(payload.sources, 'sources'),
      stateTags: registry(payload.state_tags || [], 'state tags'), gaps: registry(payload.gaps || [], 'gaps'), routes: []
    };
    if (HABITATS.some(id => !data.habitats.has(id)) || FIRE_TYPES.some(id => !data.fireTypes.has(id)) || !Array.isArray(payload.routes)) throw Error('Incomplete atlas');
    const ids = new Set();
    for (const route of payload.routes) {
      const id = route?.habitat_id + '/' + route?.fire_type_id;
      if (!route || ids.has(id) || !HABITATS.includes(route.habitat_id) || !FIRE_TYPES.includes(route.fire_type_id)) throw Error('Invalid route');
      ids.add(id);
      const links = (items, key) => {
        if (!Array.isArray(items)) throw Error('Missing relationship list');
        return items.map(item => {
          if (!item || typeof item[key] !== 'string' || !RELATIONSHIPS.includes(item.relationship)) throw Error('Invalid relationship');
          return { ...item, source_ids: refs(item.source_ids) };
        });
      };
      data.routes.push({ ...route, dataset_links: links(route.dataset_links, 'dataset_id'), insight_links: links(route.insight_links, 'insight_id'), state_tag_ids: refs(route.state_tag_ids), gap_ids: refs(route.gap_ids) });
    }
    return data;
  }
  function urlState(input) {
    const url = new URL(input, 'http://127.0.0.1/');
    const requested = { habitat: url.searchParams.get('habitat'), fireType: url.searchParams.get('fire_type'), world: url.searchParams.get('world') };
    return {
      habitat: HABITATS.includes(requested.habitat) ? requested.habitat : 'space_station',
      fireType: requested.fireType === '' || (HABITATS.includes(requested.habitat) && !url.searchParams.has('fire_type')) ? null : FIRE_TYPES.includes(requested.fireType) ? requested.fireType : 'electrical_overheating_smoke',
      world: WORLDS.includes(requested.world) ? requested.world : 'moon',
      invalid: Boolean((requested.habitat && !HABITATS.includes(requested.habitat)) || (requested.fireType && !FIRE_TYPES.includes(requested.fireType)) || (requested.world && !WORLDS.includes(requested.world)))
    };
  }
  function sourceURL(value, origin) {
    if (typeof value !== 'string' || /[\u0000-\u001f\u007f]/.test(value)) return null;
    try {
      if (!(value.startsWith('/') && !value.startsWith('//')) && !/^https?:\/\//i.test(value)) return null;
      const url = new URL(value, origin);
      if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) return null;
      return url.href;
    } catch (_) { return null; }
  }
  function caseURL(value, origin) {
    if (typeof value !== 'string' || /[\u0000-\u001f\u007f]/.test(value)) return null;
    try {
      const rawPath = decodeURIComponent(value.split(/[?#]/)[0]);
      if (rawPath.includes('\\') || rawPath.split('/').some(part => part === '..')) return null;
      const url = new URL(value, origin);
      if (url.origin !== new URL(origin).origin || url.username || url.password || !PAGES.has(url.pathname)) return null;
      return url.href;
    } catch (_) { return null; }
  }
  function textLines(value) {
    if (typeof value === 'string') return value.trim() ? [value] : [];
    if (Array.isArray(value)) return value.flatMap(textLines);
    if (value && typeof value === 'object') return ['text', 'summary', 'description', 'context', 'description_en', 'interior_context', 'intro'].flatMap(key => textLines(value[key]));
    return [];
  }
  function createApp(environment) {
    const doc = environment.document, win = environment.window, fetcher = environment.fetch;
    const byId = id => doc.getElementById(id);
    const controls = (id, selector) => [...byId(id).querySelectorAll(selector)];
    const habitatButtons = controls('habitat-map', 'button[data-habitat]');
    const fireButtons = controls('fire-types', 'button[data-fire-type]');
    const worldControl = byId('rover-world');
    const state = { ...urlState(win.location.href), data: null, phase: 'idle', serial: 0, controller: null, drawerReturn: null, destroyed: false };
    const origin = () => win.location.href;
    function node(tag, text, parent, className) {
      const item = doc.createElement(tag);
      if (text != null) item.textContent = String(text);
      if (className) item.className = className;
      if (parent) parent.appendChild(item);
      return item;
    }
    function link(label, url, parent, external) {
      if (!url) return null;
      const a = node('a', label, parent);
      a.href = url;
      if (external) { a.target = '_blank'; a.rel = 'noopener noreferrer'; }
      return a;
    }
    function details(parent, heading, lines) {
      const values = lines.flatMap(textLines);
      if (!values.length) return null;
      const box = node('details', null, parent, 'atlas-details');
      node('summary', heading, box);
      for (const text of values) node('p', text, box);
      return box;
    }
    function addCaseLinks(record, parent) {
      if (!Array.isArray(record?.deep_links)) return;
      const seen = new Set();
      const valid = record.deep_links.map(item => ({ label: valueText(item?.label), url: caseURL(item?.url, origin()) })).filter(item => {
        if (!item.label || !item.url || seen.has(item.url)) return false;
        seen.add(item.url); return true;
      });
      if (!valid.length) return;
      const box = node('div', null, parent, 'atlas-links');
      for (const item of valid) link(item.label, item.url, box, false);
    }
    function badge(value, parent) {
      const item = node('span', RELATIONSHIP_LABELS[value] || 'Unknown', parent, 'relationship-badge ' + value + ' relationship-' + value);
      item.setAttribute('data-relationship', value);
    }
    function scrollToElement(element, block) {
      if (!element || typeof element.scrollIntoView !== 'function') return;
      let reduced = false;
      try { reduced = Boolean(win.matchMedia?.('(prefers-reduced-motion: reduce)').matches); } catch (_) {}
      element.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block });
    }
    function revealResearch() {
      const title = byId('habitat-title');
      title.focus({ preventScroll: true });
      scrollToElement(title, 'start');
    }
    function returnToMap(event) {
      event.preventDefault(); hideEvidence(false);
      const selected = habitatButtons.find(button => button.dataset.habitat === state.habitat);
      if (!selected) return;
      selected.focus({ preventScroll: true }); scrollToElement(selected, 'center');
    }
    function hideEvidence(restore) {
      const drawer = byId('evidence-drawer');
      drawer.open = false;
      drawer.hidden = true;
      drawer.setAttribute('aria-hidden', 'true');
      if (restore && state.drawerReturn?.focus) state.drawerReturn.focus();
      state.drawerReturn = null;
    }
    function showEvidence(label, sourceIds, limits, opener) {
      const drawer = byId('evidence-drawer');
      const content = byId('evidence-drawer-content');
      if (!content) return;
      content.replaceChildren();
      state.drawerReturn = opener || doc.activeElement;
      drawer.hidden = false;
      drawer.open = true;
      drawer.setAttribute('aria-hidden', 'false');
      drawer.setAttribute('aria-label', 'Evidence sources');
      const close = node('button', 'Close evidence', content, 'quiet-button');
      close.type = 'button'; close.addEventListener('click', () => hideEvidence(true));
      const heading = node('h2', label, content);
      heading.id = 'atlas-evidence-title'; drawer.setAttribute('aria-labelledby', heading.id);
      const ids = unique(sourceIds);
      if (!ids.length) node('p', 'Source references were not supplied.', content, 'atlas-empty');
      for (const id of ids) {
        const source = state.data?.sources.get(id), article = node('article', null, content, 'atlas-source');
        node('h3', source ? valueText(source.title) || id : 'Source details not supplied: ' + id, article);
        if (!source) continue;
        if (source.edition) node('p', valueText(source.edition), article);
        if (source.doi) node('p', 'DOI: ' + valueText(source.doi), article);
        link('Primary source', sourceURL(source.url, origin()), article, true);
        const pages = [];
        for (const item of Array.isArray(source.direct_page_links) ? source.direct_page_links : []) {
          if (Number.isInteger(item.physical_pdf_page) && item.physical_pdf_page > 0) pages.push({ page: item.physical_pdf_page, url: sourceURL(item.url, origin()) });
        }
        if (source.local_pdf_url) {
          let url = sourceURL(source.local_pdf_url, origin());
          if (url && Number.isInteger(source.pdf_page) && source.pdf_page > 0 && /\.pdf(?:[?#]|$)/i.test(url)) {
            const target = new URL(url);
            if (!target.hash) target.hash = 'page=' + source.pdf_page;
            url = target.href;
          }
          link('Exact-edition PDF' + (Number.isInteger(source.pdf_page) && source.pdf_page > 0 ? ' · page ' + source.pdf_page : ''), url, article, true);
        }
        for (const item of pages) link('Physical PDF page ' + item.page, item.url, article, true);
        details(article, 'Source scope', [source.scope, source.limits]);
      }
      details(content, 'Evidence limits', [limits]);
      close.focus();
    }
    function evidenceButton(parent, label, ids, limits) {
      const button = node('button', 'View evidence', parent, 'evidence-toggle');
      button.type = 'button'; button.addEventListener('click', () => showEvidence(label, ids, limits, button));
    }
    function updateURL() {
      try {
        const url = new URL(win.location.href);
        url.searchParams.set('habitat', state.habitat); url.searchParams.set('fire_type', state.fireType || ''); url.searchParams.set('world', state.world);
        win.history.replaceState(null, '', url.href);
      } catch (_) {}
    }
    function selectionButtons() {
      for (const button of habitatButtons) {
        const selected = button.dataset.habitat === state.habitat;
        button.setAttribute('aria-pressed', String(selected)); button.classList.toggle('selected', selected);
      }
      for (const button of fireButtons) {
        const selected = button.dataset.fireType === state.fireType;
        button.setAttribute('aria-pressed', String(selected)); button.classList.toggle('selected', selected);
      }
      worldControl.value = state.world; worldControl.hidden = state.habitat !== 'pressurized_rover'; worldControl.disabled = state.habitat !== 'pressurized_rover';
    }
    function render() {
      selectionButtons();
      const datasets = byId('dataset-list'), insights = byId('insight-list'), context = byId('habitat-context'), error = byId('atlas-error');
      datasets.replaceChildren(); insights.replaceChildren(); context.replaceChildren(); error.replaceChildren(); error.hidden = true;
      const habitat = state.data?.habitats.get(state.habitat);
      const fallbackLabel = habitatButtons.find(button => button.dataset.habitat === state.habitat)?.textContent || 'Selected habitat';
      byId('habitat-title').textContent = valueText(habitat?.title) || fallbackLabel;
      if (!state.data) {
        const unavailable = state.phase === 'error';
        node('p', unavailable ? 'Dataset associations unavailable.' : 'Loading supplied dataset associations…', datasets, 'atlas-empty');
        node('p', unavailable ? 'Insight links unavailable.' : 'Loading supplied insight links…', insights, 'atlas-empty');
        byId('atlas-status').textContent = unavailable ? 'Atlas unavailable. No earlier results are being shown.' : 'Loading reviewed atlas…';
        if (unavailable) {
          error.hidden = false; node('span', 'The reviewed atlas could not be loaded. ', error);
          const retry = node('button', 'Retry', error); retry.type = 'button'; retry.addEventListener('click', load);
        }
        return;
      }
      for (const text of [habitat.context, habitat.intro, habitat.interior_context].flatMap(textLines)) node('p', text, context);
      const gravityLabel = GRAVITY_LABELS[habitat.gravity_context];
      if (gravityLabel) node('p', gravityLabel, context, 'gravity-context');
      if (state.habitat === 'pressurized_rover') {
        byId('habitat-title').textContent += state.world === 'moon' ? ' · Moon scenario' : ' · Mars scenario';
        const worldLines = textLines(habitat.world_contexts?.[state.world]);
        for (const text of worldLines.length ? worldLines : ['World-specific context was not supplied.']) node('p', text, context);
        const worldGravity = GRAVITY_LABELS[habitat.world_contexts?.[state.world]?.gravity_context];
        if (worldGravity) node('p', worldGravity, context, 'gravity-context');
      }
      details(context, 'Source gravity classification', [habitat.gravity_context, state.habitat === 'pressurized_rover' ? habitat.world_contexts?.[state.world]?.gravity_context : null]);
      details(context, 'Context limits', [habitat.limits]);
      const routes = state.data.routes.filter(item => item.habitat_id === state.habitat && (!state.fireType || item.fire_type_id === state.fireType));
      const immediate = new Set(refs(habitat.immediate_related_psi_ids));
      const selected = routes.flatMap(route => route.dataset_links).filter(item => state.fireType || immediate.has(item.dataset_id));
      const datasetIds = state.fireType ? unique(selected.map(item => item.dataset_id)) : [...immediate];
      const selectedInsights = state.fireType ? routes.flatMap(route => route.insight_links) : [];
      const states = unique(routes.flatMap(route => route.state_tag_ids));
      if (state.fireType && states.length) details(context, 'Secondary flame states', states.map(id => valueText(state.data.stateTags.get(id)?.title) || valueText(state.data.stateTags.get(id)?.label_en) || id));
      const gaps = unique(routes.flatMap(route => route.gap_ids));
      details(context, 'Evidence gaps', gaps.map(id => valueText(state.data.gaps.get(id)?.text) || valueText(state.data.gaps.get(id)?.text_en) || id));
      for (const id of datasetIds) {
        const item = state.data.datasets.get(id), relations = selected.filter(row => row.dataset_id === id);
        const card = node('article', null, datasets, 'atlas-card dataset-card'); card.setAttribute('data-dataset-id', id);
        const displayTitle = item ? valueText(item.short_name) || valueText(item.title) || id : 'Dataset details not supplied: ' + id;
        node('h3', displayTitle, card);
        const badges = node('div', null, card, 'relationship-badges');
        for (const relationship of unique(relations.map(row => row.relationship))) badge(relationship, badges);
        if (!relations.length) badge('unknown', badges);
        const copy = unique([item?.summary, ...relations.map(relation => relation.statement)].flatMap(textLines).map(text => text.trim()));
        const firstSentence = copy.shift();
        if (firstSentence) node('p', firstSentence, card, 'relation-statement');
        if (!relations.length) node('p', 'Applicability details were not supplied for this immediate association.', card, 'atlas-empty');
        link('NASA PSI dataset', sourceURL(item?.nasa_url, origin()), card, true);
        addCaseLinks({ deep_links: [...(Array.isArray(item?.deep_links) ? item.deep_links : []), ...relations.flatMap(row => Array.isArray(row.deep_links) ? row.deep_links : [])] }, card);
        details(card, 'Dataset details', [item?.title !== displayTitle ? item?.title : null, ...copy, item?.source_environment, item?.objective, item?.measurements, item?.limits]);
        evidenceButton(card, item ? valueText(item.title) || id : id, unique([...refs(item?.source_ids), ...relations.flatMap(row => row.source_ids)]), [item?.limits, ...relations.map(row => row.limits)]);
      }
      const insightIds = unique(selectedInsights.map(item => item.insight_id));
      for (const id of insightIds) {
        const item = state.data.insights.get(id), relations = selectedInsights.filter(row => row.insight_id === id);
        const card = node('article', null, insights, 'atlas-card insight-card'); card.setAttribute('data-insight-id', id);
        node('h3', item ? id + ' · ' + (valueText(item.title) || 'Supplied insight') : 'Insight details not supplied: ' + id, card);
        const badges = node('div', null, card, 'relationship-badges');
        for (const relationship of unique(relations.map(row => row.relationship))) badge(relationship, badges);
        if (item?.summary) node('p', valueText(item.summary), card);
        for (const relation of relations) {
          if (relation.statement) node('p', valueText(relation.statement), card, 'relation-statement');
        }
        addCaseLinks({ deep_links: [...(Array.isArray(item?.deep_links) ? item.deep_links : []), ...relations.flatMap(row => Array.isArray(row.deep_links) ? row.deep_links : [])] }, card);
        details(card, 'Evidence and limits', [item?.statement, item?.hypothesis, ...unique(relations.map(relation => relation.source_claim_class).filter(Boolean)).map(value => 'Source claim: ' + valueText(value)), item?.limits]);
        evidenceButton(card, item ? valueText(item.title) || id : id, unique([...refs(item?.source_ids), ...relations.flatMap(row => row.source_ids)]), [item?.limits, ...relations.map(row => row.limits)]);
      }
      if (!datasetIds.length) node('p', 'No dataset relationship was supplied for this selection.', datasets, 'atlas-empty');
      if (!insightIds.length) node('p', state.fireType ? 'No insight relationship was supplied for this selection.' : 'Choose a fire type to inspect its supplied insight links.', insights, 'atlas-empty');
      byId('atlas-status').textContent = datasetIds.length + ' dataset relationship' + (datasetIds.length === 1 ? '' : 's') + ' · ' + insightIds.length + ' insight link' + (insightIds.length === 1 ? '' : 's') + (state.invalid ? ' · Unrecognized URL selection replaced by the stated defaults.' : '');
    }
    function select(key, value) {
      const allowed = key === 'habitat' ? HABITATS : key === 'fireType' ? FIRE_TYPES : key === 'world' ? WORLDS : [];
      if (!allowed.includes(value)) return;
      state[key] = value;
      if (key === 'habitat') state.fireType = null;
      state.invalid = false; hideEvidence(false); updateURL(); render();
    }
    function keyboard(buttons, key, event) {
      const index = buttons.indexOf(event.currentTarget || event.target);
      let next = index;
      if (['ArrowRight', 'ArrowDown'].includes(event.key)) next = (index + 1) % buttons.length;
      else if (['ArrowLeft', 'ArrowUp'].includes(event.key)) next = (index + buttons.length - 1) % buttons.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = buttons.length - 1;
      else return;
      event.preventDefault(); buttons[next].focus(); select(key, key === 'habitat' ? buttons[next].dataset.habitat : buttons[next].dataset.fireType);
    }
    async function load() {
      if (state.destroyed) return;
      const serial = ++state.serial; state.controller?.abort();
      const Controller = win.AbortController || (typeof AbortController !== 'undefined' ? AbortController : null);
      state.controller = Controller ? new Controller() : null;
      state.data = null; state.phase = 'loading'; hideEvidence(false); render();
      try {
        const response = await fetcher(API, { cache: 'no-store', signal: state.controller?.signal, headers: { Accept: 'application/json' } });
        if (!response.ok) throw Error('Unavailable');
        const payload = await response.json();
        if (serial !== state.serial || state.destroyed) return;
        state.data = normalizePayload(payload); state.phase = 'ready'; updateURL(); render();
      } catch (_) {
        if (serial !== state.serial || state.destroyed) return;
        state.data = null; state.phase = 'error'; hideEvidence(false); render();
      }
    }
    let started = false;
    function start() {
      if (started) return Promise.resolve(); started = true;
      for (const button of habitatButtons) { button.addEventListener('click', () => { select('habitat', button.dataset.habitat); revealResearch(); }); button.addEventListener('keydown', event => keyboard(habitatButtons, 'habitat', event)); }
      for (const button of fireButtons) { button.addEventListener('click', () => select('fireType', button.dataset.fireType)); button.addEventListener('keydown', event => keyboard(fireButtons, 'fireType', event)); }
      worldControl.addEventListener('change', () => select('world', worldControl.value));
      byId('atlas-back-to-map')?.addEventListener('click', returnToMap);
      win.addEventListener('popstate', () => { Object.assign(state, urlState(win.location.href)); hideEvidence(false); render(); });
      doc.addEventListener('keydown', event => { if (event.key === 'Escape' && !byId('evidence-drawer').hidden) hideEvidence(true); });
      return load();
    }
    return Object.freeze({ start, load, select, getState: () => ({ habitat: state.habitat, fireType: state.fireType, world: state.world, phase: state.phase }), destroy: () => { state.destroyed = true; state.serial++; state.controller?.abort(); hideEvidence(false); } });
  }
  return Object.freeze({ createApp, normalizePayload, urlState, sourceURL, caseURL, HABITATS, FIRE_TYPES, WORLDS, RELATIONSHIPS });
});
