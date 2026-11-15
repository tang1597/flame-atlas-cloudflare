(function () {
  'use strict';
  const API = '/api/fire-strategies';
  const ROLES = { observed: 'Observed data', author: 'Author conclusion', physical: 'Physical inference', product: 'Product hypothesis', guidance: 'Official guidance', model: 'Model inference', unknown: 'Evidence type unknown' };
  const COLORS = ['#356d50', '#557d9a', '#a0733e', '#806295', '#987057'];
  const arr = value => Array.isArray(value) ? value : [];
  const str = value => typeof value === 'string' ? value : '';
  const readable = value => {
    if (typeof value === 'string') return value;
    if (!value || typeof value !== 'object') return '';
    return str(value.summary_en) || str(value.text_en) || str(value.text) || str(value.statement) || str(value.summary) || str(value.description_en) || str(value.description) || str(value.claim);
  };
  const sourceIds = item => arr(item && item.source_ids).length ? item.source_ids : item && item.source_id ? [item.source_id] : [];
  const englishText = value => { const result = readable(value); return /[\u3400-\u9fff]/.test(result) ? '' : result; };
  const locatorText = value => {
    if (typeof value === 'string') return value;
    if (!value || typeof value !== 'object') return '';
    return [value.pdf_page ? 'PDF page ' + value.pdf_page : '', value.section, value.figure ? 'Figure ' + value.figure : '', value.sheet, value.row ? 'Row ' + value.row : '', arr(value.cells).join(', ')].filter(Boolean).join(' · ');
  };
  function editorialScore(item) {
    const value = item.evidence_score;
    if (typeof value === 'string') return value.trim();
    const score = Number.isFinite(value) ? value : value && Number.isFinite(value.total) ? value.total : value && Number.isFinite(value.score) ? value.score : null;
    if (score === null) return '';
    const maximum = value && typeof value === 'object' && Number.isFinite(value.max) ? value.max : Number.isFinite(item.evidence_score_max) ? item.evidence_score_max : Number.isFinite(item.score_max) ? item.score_max : null;
    return String(score) + (maximum !== null ? '/' + maximum : '');
  }
  function roleOf(item) {
    const kind = str(item && (item.kind || item.role || item.type || item.evidence_type)).toLowerCase().replace(/[\s-]+/g, '_');
    if (['observed', 'observed_data', 'observation', 'measured', 'measurement', 'direct_measurement', 'source_measurement', 'source_reduced', 'source_reduced_measurement', 'source_analyzed_experimental_measurement'].includes(kind)) return 'observed';
    if (['author_conclusion', 'author_interpretation', 'author_inference'].includes(kind)) return 'author';
    if (['physical_inference', 'reviewer_inference'].includes(kind)) return 'physical';
    if (['product_hypothesis', 'hypothesis', 'proposal'].includes(kind)) return 'product';
    if (kind === 'official_guidance') return 'guidance';
    if (kind === 'model_inference') return 'model';
    return 'unknown';
  }
  function sourceUrl(value, page, base, knownPdf) {
    if (!str(value) || /^[A-Za-z]:[\\/]/.test(value) || value.startsWith('\\\\')) return null;
    try {
      const u = new URL(value, base || 'http://localhost/');
      if (!['http:', 'https:'].includes(u.protocol)) return null;
      if ((knownPdf || /\.pdf$/i.test(u.pathname)) && Number.isInteger(Number(page)) && Number(page) > 0) u.hash = 'page=' + Number(page);
      return u.href;
    } catch (_) { return null; }
  }
  function pageUrl(source, page, base) {
    const local = sourceUrl(source.local_pdf_url, page, base, true);
    if (local) return local;
    const explicit = arr(source.direct_page_links).find(link => Number(link.physical_pdf_page || link.pdf_page) === Number(page));
    const result = sourceUrl(explicit ? explicit.url : source.url || source.official_url, explicit ? null : page, base);
    if (page && !explicit && result && !/\.pdf(?:[?#]|$)/i.test(result)) return null;
    return result;
  }
  function validateCatalog(data) {
    if (!data || !Array.isArray(data.cases) || !Array.isArray(data.sources) || !str(data.schema_version)) throw new Error('The reviewed strategy catalog is incomplete.');
    if (/synthetic|example_only|mock/i.test(str(data.status))) throw new Error('Synthetic examples are not a reviewed strategy catalog.');
    const ids = new Set();
    for (const item of data.cases) {
      if (!item || !str(item.id) || ids.has(item.id) || !str(item.title_en)) throw new Error('A strategy case has missing or duplicate identity.');
      ids.add(item.id);
      if (!Array.isArray(item.evidence)) throw new Error('A case is missing its evidence records.');
    }
    if (data.cases.length && !ids.has(data.selected_case_id)) throw new Error('The supplied selected case is not in this catalog.');
    if (data.matching_case_ids !== undefined && (!Array.isArray(data.matching_case_ids) || data.matching_case_ids.some(id => !ids.has(id)))) throw new Error('A query match references an unavailable case.');
    return data;
  }
  function visibleCases(data, query) {
    if (data.query_scope && data.query_scope.status === 'out_of_scope') return [];
    if (!query) return data.cases;
    if (!Array.isArray(data.matching_case_ids)) throw new Error('The query response does not identify its authored-text matches.');
    const matches = new Set(data.matching_case_ids); return data.cases.filter(item => matches.has(item.id));
  }
  function chartReadiness(item, sources) {
    if (!item.chart) return { ok: false, reason: 'No numeric observed series is supplied for this case. The sourced observation table and data gaps remain below.' };
    const c = item.chart;
    const xtype = c.x_type || 'linear';
    if (!['linear', 'ordinal', 'categorical'].includes(xtype) || !str(c.title) || !str(c.x_label) || !str(c.y_label) || (xtype === 'linear' && typeof c.x_unit !== 'string') || typeof c.y_unit !== 'string' || !arr(c.series).length) return { ok: false, reason: 'Observed chart labels, axis definition or units are incomplete. No graph has been drawn.' };
    const evidence = new Map(item.evidence.map(e => [e.id, e]));
    const knownSources = new Set(sources.map(s => s.id));
    let points = 0;
    for (const series of c.series) {
      if (!str(series.id) || !str(series.label) || !str(series.investigation_id) || !str(series.trial_id) || !arr(series.points).length) return { ok: false, reason: 'A series is missing its trial identity or observed points. No graph has been drawn.' };
      for (const p of series.points) {
        const e = evidence.get(p.evidence_id);
        const locator = e && (locatorText(e.locator) || locatorText(e.source_locator) || arr(e.source_locators).length);
        const xvalid = xtype === 'categorical' ? Boolean(str(p.x).trim()) : Number.isFinite(p.x);
        if (!xvalid || !Number.isFinite(p.y) || !e || roleOf(e) !== 'observed' || !locator || !sourceIds(e).some(id => knownSources.has(id))) return { ok: false, reason: 'A supplied point lacks a defined category or finite observed value, an observed-evidence role or a source locator. No graph has been drawn.' };
        points++;
      }
    }
    return { ok: true, chart: c, pointCount: points, xType: xtype };
  }
  function start() {
    const $ = id => document.getElementById(id);
    const state = { data: null, selected: null, visible: [], explicitUnmatched: false, request: 0, cards: new Map(), sources: new Map() };
    const create = (tag, cls, value) => { const n = document.createElement(tag); if (cls) n.className = cls; if (value !== undefined) n.textContent = String(value); return n; };
    const tag = role => create('span', 'evidence-role role-' + role, ROLES[role]);
    function lines(host, values, fallback) {
      const items = arr(values).map(readable).filter(Boolean);
      if (!items.length) { if (fallback) host.append(create('p', 'small-note', fallback)); return; }
      const ul = create('ul', 'case-list'); for (const item of items) ul.append(create('li', '', item)); host.append(ul);
    }
    function sources(host, ids) {
      for (const id of [...new Set(arr(ids))]) {
        const card = state.cards.get(id);
        if (!card) { host.append(create('span', 'evidence-role role-unknown', 'Source not supplied: ' + id)); continue; }
        const a = create('a', 'source-chip', id); a.href = '#' + card.id;
        a.addEventListener('click', event => { event.preventDefault(); $('strategy-source-library').open = true; for (const c of state.cards.values()) c.classList.remove('is-highlighted'); card.classList.add('is-highlighted'); card.focus({ preventScroll: true }); card.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
        host.append(a);
      }
    }
    function link(host, label, url) { if (!url) return; const a = create('a', '', label); a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer'; host.append(a); }
    function renderSources() {
      const host = $('strategy-sources'); host.replaceChildren(); state.cards.clear(); state.sources.clear();
      const citations = new Map();
      const addCitation = (id, locator) => { if (!id || !locatorText(locator)) return; if (!citations.has(id)) citations.set(id, []); const values = citations.get(id); if (!values.some(value => locatorText(value) === locatorText(locator))) values.push(locator); };
      for (const item of state.data.cases) {
        for (const e of item.evidence) for (const id of sourceIds(e)) addCitation(id, e.source_locator || e.locator);
        for (const reference of arr(item.literature)) if (reference && typeof reference === 'object') addCitation(reference.source_id || reference.id, reference.source_locator || reference.locator);
      }
      state.data.sources.forEach((s, i) => {
        const card = create('article', 'source-card'); card.id = 'strategy-source-' + (i + 1); card.tabIndex = -1; state.cards.set(s.id, card); state.sources.set(s.id, s);
        card.append(create('h3', '', s.title || 'Source title unknown'));
        if (s.role || s.kind) card.append(create('p', 'small-note', 'Source role: ' + str(s.role || s.kind).replace(/_/g, ' ')));
        if (s.authority || s.authors) card.append(create('p', '', s.authority || arr(s.authors).join(', ')));
        if (s.scope) card.append(create('p', '', s.scope));
        const links = create('div', 'source-links'); link(links, 'Official source ↗', sourceUrl(s.url || s.official_url || s.doi_url, null, window.location.href));
        const page = s.pdf_page || s.physical_page;
        if (s.local_pdf_url) link(links, 'Reviewed PDF ↗', pageUrl(s, page, window.location.href));
        const cited = citations.get(s.id) || [];
        const pages = [...new Set([page, ...arr(s.pdf_pages), ...arr(s.direct_page_links).map(x => x.physical_pdf_page || x.pdf_page), ...cited.map(locator => locator && locator.pdf_page)].filter(x => Number.isInteger(x) && x > 0))];
        for (const p of pages) link(links, 'PDF page ' + p + ' ↗', pageUrl(s, p, window.location.href));
        card.append(links);
        if (s.section || s.locator || s.source_locator) card.append(create('p', '', s.section || locatorText(s.locator || s.source_locator)));
        if (s.access) card.append(create('p', '', s.access));
        if (s.edition || s.sha256) { const detail = create('details'); detail.append(create('summary', '', 'Source edition')); if (s.edition) detail.append(create('p', '', s.edition)); if (s.sha256) detail.append(create('p', '', 'SHA-256: ' + s.sha256)); card.append(detail); }
        if (cited.length) { const detail = create('details'); detail.append(create('summary', '', 'Cited source locators (' + cited.length + ')')); const ul = create('ul', 'case-list'); for (const locator of cited) { const li = create('li', '', locatorText(locator)); if (locator.pdf_page) { const links = create('div', 'source-links'); link(links, 'Open PDF page ' + locator.pdf_page + ' ↗', pageUrl(s, locator.pdf_page, window.location.href)); li.append(links); } ul.append(li); } detail.append(ul); card.append(detail); }
        host.append(card);
      });
      $('strategy-source-count').textContent = '(' + state.data.sources.length + ')'; $('strategy-source-library').hidden = !state.data.sources.length;
    }
    function renderPriorities() {
      const host = $('priority-list'); host.replaceChildren();
      if (!state.visible.length) { host.append(create('p', 'empty', 'No reviewed strategies match this query.')); return; }
      for (const item of state.visible) {
        const row = create('article', 'priority-item');
        const button = create('button', 'priority-button'); button.type = 'button'; button.setAttribute('aria-pressed', String(item.id === state.selected));
        button.append(create('span', 'priority-number', Number.isFinite(item.rank) ? item.rank : '?'), create('span', 'priority-name', item.title_en));
        button.addEventListener('click', () => { state.selected = item.id; state.explicitUnmatched = false; renderPriorities(); renderCase(); updateLocation(); });
        row.append(button, create('p', 'priority-meta', [Array.isArray(item.pillar) ? item.pillar.join(' / ') : item.pillar, arr(item.investigations).map(x => typeof x === 'string' ? x : x.id || x.study_id || x.title).filter(Boolean).join(', ')].filter(Boolean).join(' · ')));
        if (editorialScore(item)) row.append(create('p', 'priority-meta', 'Editorial evidence score: ' + editorialScore(item)));
        const why = create('details'); why.append(create('summary', '', 'Why this priority')); lines(why, item.rank_reasons, 'Priority reasons were not separately supplied.'); row.append(why); host.append(row);
      }
    }
    function section(host, title, role) { const s = create('section', 'case-section'); if (role) s.append(tag(role)); s.append(create('h3', '', title)); host.append(s); return s; }
    function observationTable(host, evidence) {
      const observations = evidence.filter(e => roleOf(e) === 'observed');
      if (!observations.length) { host.append(create('p', 'data-gap', 'No separately typed observation records are supplied. Unknowns have not been converted to zero.')); return; }
      const wrap = create('div', 'table-wrap'), table = create('table', 'observation-table'), head = create('thead'), tr = create('tr');
      for (const name of ['Observation', 'Source value', 'Locator / source']) tr.append(create('th', '', name)); head.append(tr); table.append(head);
      const body = create('tbody');
      for (const e of observations) {
        const row = create('tr'); row.append(create('td', '', readable(e) || e.label || e.id));
        const value = e.value === null || e.value === undefined ? 'Unknown / see source observation' : typeof e.value === 'number' && !Number.isFinite(e.value) ? 'Unknown' : String(e.value);
        row.append(create('td', '', [value, str(e.unit)].filter(Boolean).join(' ')));
        const origin = create('td', '', locatorText(e.locator || e.source_locator) || 'Locator not supplied'); const chips = create('div', 'source-chips'); sources(chips, sourceIds(e)); origin.append(chips); row.append(origin); body.append(row);
      }
      table.append(body); wrap.append(table); host.append(wrap);
    }
    function plot(host, readiness) {
      if (!readiness.ok) { host.append(create('p', 'data-gap', readiness.reason)); return; }
      const c = readiness.chart, points = c.series.flatMap(s => s.points);
      const discrete = readiness.xType !== 'linear';
      const categories = [...new Set(points.map(p => p.x))];
      let xmin = discrete ? 0 : Math.min(...points.map(p => p.x)), xmax = discrete ? categories.length - 1 : Math.max(...points.map(p => p.x)), ymin = Math.min(...points.map(p => p.y)), ymax = Math.max(...points.map(p => p.y));
      const xp = discrete ? .35 : (xmax - xmin) * .06 || Math.max(Math.abs(xmin) * .06, .5), yp = (ymax - ymin) * .08 || Math.max(Math.abs(ymin) * .08, .5); xmin -= xp; xmax += xp; ymin -= yp; ymax += yp;
      const W = 760, H = 365, left = 72, right = 24, top = 35, bottom = 63, width = W - left - right, height = H - top - bottom;
      const sx = x => left + ((discrete ? categories.indexOf(x) : x) - xmin) / (xmax - xmin) * width, sy = y => top + height - (y - ymin) / (ymax - ymin) * height;
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); svg.classList.add('observed-chart'); svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', c.title + '. Source-bound observations only.');
      function el(name, attrs, value) { const n = document.createElementNS('http://www.w3.org/2000/svg', name); for (const [key, val] of Object.entries(attrs)) n.setAttribute(key, String(val)); if (value !== undefined) n.textContent = String(value); svg.append(n); return n; }
      el('title', {}, c.title); el('text', { x: left, y: 17 }, c.title);
      const fmt = n => Number(n.toPrecision(4)).toString();
      for (let i = 0; i <= 4; i++) { const y = ymin + (ymax - ymin) * i / 4; el('line', { x1: left, x2: left + width, y1: sy(y), y2: sy(y), class: 'chart-grid' }); el('text', { x: left - 10, y: sy(y) + 4, 'text-anchor': 'end' }, fmt(y)); }
      if (discrete) {
        for (const x of categories) { const labels = [...new Set(points.filter(p => p.x === x).map(p => p.label).filter(Boolean))]; const label = readiness.xType === 'categorical' ? x : labels.length === 1 ? labels[0] : String(x); el('text', { x: sx(x), y: top + height + 21, 'text-anchor': 'middle' }, label); }
      } else {
        for (let i = 0; i <= 4; i++) { const x = xmin + (xmax - xmin) * i / 4; el('line', { x1: sx(x), x2: sx(x), y1: top, y2: top + height, class: 'chart-grid' }); el('text', { x: sx(x), y: top + height + 21, 'text-anchor': 'middle' }, fmt(x)); }
      }
      el('line', { x1: left, x2: left + width, y1: top + height, y2: top + height, class: 'chart-axis' }); el('line', { x1: left, x2: left, y1: top, y2: top + height, class: 'chart-axis' });
      el('text', { x: left + width / 2, y: H - 10, 'text-anchor': 'middle' }, c.x_label + (c.x_unit ? ' (' + c.x_unit + ')' : ''));
      el('text', { transform: 'translate(18,' + (top + height / 2) + ') rotate(-90)', 'text-anchor': 'middle' }, c.y_label + (c.y_unit ? ' (' + c.y_unit + ')' : ''));
      c.series.forEach((series, index) => { for (const p of series.points) { const circle = el('circle', { cx: sx(p.x), cy: sy(p.y), r: 3.4, fill: COLORS[index % COLORS.length], opacity: .85 }); const title = document.createElementNS('http://www.w3.org/2000/svg', 'title'); title.textContent = [series.label, series.trial_id, p.label, p.x + ', ' + p.y, p.evidence_id].filter(Boolean).join(' · '); circle.append(title); } });
      const wrap = create('div', 'chart-wrap'); wrap.append(svg); host.append(wrap);
      const legend = create('div', 'chart-legend'); c.series.forEach((s, i) => { const label = create('span'); const dot = create('span', 'legend-dot'); dot.style.backgroundColor = COLORS[i % COLORS.length]; label.append(dot, document.createTextNode(s.label + ' · ' + s.trial_id)); legend.append(label); }); host.append(legend);
      host.append(create('p', 'chart-caption', readiness.pointCount + ' supplied source-bound observations. Series retain supplied record identities; sampling fractions are not independent experiments. No smoothing, fitted curve or model interpolation.'));
      if (readiness.xType === 'categorical') host.append(create('p', 'chart-caption', 'Shared-generation / fraction context: separate sampling-fraction series do not imply separate fires. The source caption below defines their grouping.'));
      if (c.x_definition) host.append(create('p', 'chart-caption', c.x_definition));
      if (c.y_definition) host.append(create('p', 'chart-caption', 'Measurement definition: ' + c.y_definition));
      if (c.caption) host.append(create('p', 'chart-caption', c.caption));
    }
    function roleStatements(host, evidence, role, fallback) {
      const items = evidence.filter(e => roleOf(e) === role);
      if (!items.length) { host.append(create('p', 'small-note', fallback)); return; }
      for (const item of items) { const row = create('div', 'evidence-item'); row.append(create('p', '', readable(item) || 'Statement not supplied')); const chips = create('div', 'source-chips'); sources(chips, sourceIds(item)); row.append(chips); host.append(row); }
    }
    function experimentalConditions(host, evidence) {
      const detail = create('details', 'disclosure'); detail.append(create('summary', '', 'Experimental conditions and measurement roles'));
      const body = create('div');
      const show = value => value === null || value === undefined ? 'Unknown' : typeof value === 'number' ? Number.isFinite(value) ? String(value) : 'Unknown' : typeof value === 'boolean' ? String(value) + ' (as supplied)' : typeof value === 'string' ? value : Array.isArray(value) ? value.map(show).join('; ') : Object.entries(value).map(([key, item]) => key.replace(/_/g, ' ') + ': ' + show(item)).join('; ') || 'Not separately supplied';
      for (const e of evidence.filter(x => roleOf(x) === 'observed')) {
        const row = create('div', 'evidence-item'); row.append(create('h4', '', [e.investigation_id, e.trial_id, e.label || e.id].filter(Boolean).join(' · ')));
        row.append(create('p', 'small-note', 'Measurement role: ' + (str(e.measurement_kind).replace(/_/g, ' ') || 'unknown')));
        if (e.denominator) row.append(create('p', 'small-note', 'Source denominator: ' + e.denominator));
        const values = e.conditions && typeof e.conditions === 'object' ? Object.entries(e.conditions).map(([key, value]) => key.replace(/_/g, ' ') + ': ' + show(value)) : [];
        lines(row, values, 'Case-bound conditions were not separately supplied.'); lines(row, e.limits); body.append(row);
      }
      if (!body.children.length) body.append(create('p', 'small-note', 'No separately typed experimental conditions are supplied.'));
      detail.append(body); host.append(detail);
    }
    function renderCase() {
      const host = $('selected-case'); host.replaceChildren();
      const item = state.data.cases.find(c => c.id === state.selected);
      if (!item) { host.append(create('p', 'empty', 'Select a reviewed case from the supplied priorities. No case has been substituted.')); return; }
      const flagship = item.id === state.data.selected_case_id;
      const selectionReason = flagship ? readable(state.data.selection && (state.data.selection.reason || state.data.selection.reason_en)) || readable(state.data.selection) || str(state.data.main_selection && state.data.main_selection.selection_reason) : '';
      if (flagship) host.append(create('p', 'eyebrow', 'Featured case'));
      const heading = create('h2', '', item.title_en); heading.id = 'case-title'; host.append(heading, create('p', 'case-meta', [Array.isArray(item.pillar) ? item.pillar.join(' / ') : item.pillar, Number.isFinite(item.rank) ? 'Supplied priority ' + item.rank : 'Priority unknown'].filter(Boolean).join(' · ')));
      if (flagship) host.append(create('p', 'selection-reason', 'Featured for its published Earth comparison.'));
      if (state.explicitUnmatched) host.append(create('p', 'data-gap', 'Opened through an explicit case link. This case is not among the supplied matches for the current query.'));
      if (item.summary_en) host.append(create('p', 'case-summary', item.summary_en));
      if (editorialScore(item) || item.score_breakdown || item.ranking_basis || selectionReason) {
        const detail = create('details', 'disclosure'); detail.append(create('summary', '', 'Editorial evidence score and basis'));
        const body = create('div');
        if (editorialScore(item)) body.append(create('p', 'editorial-score', 'Supplied editorial score: ' + editorialScore(item)));
        if (readable(state.data.ranking_method)) body.append(create('p', '', readable(state.data.ranking_method)));
        if (selectionReason) body.append(create('p', '', selectionReason));
        body.append(create('p', 'small-note', 'An editorial evidence/completeness score, not a probability, predicted effectiveness or safety verdict. No score has been recalculated here.'));
        if (readable(item.ranking_basis)) body.append(create('p', '', readable(item.ranking_basis)));
        const entries = Array.isArray(item.score_breakdown) ? item.score_breakdown.map(entry => [entry.label || entry.name || entry.id, entry]) : item.score_breakdown && typeof item.score_breakdown === 'object' ? Object.entries(item.score_breakdown) : [];
        const breakdown = entries.map(([label, value]) => {
          const supplied = Number.isFinite(value) || typeof value === 'string' ? String(value) : editorialScore({ evidence_score: value });
          return [str(label).replace(/_/g, ' '), supplied, readable(value)].filter(Boolean).join(' · ');
        });
        lines(body, breakdown); detail.append(body); host.append(detail);
      }
      const observed = section(host, 'NASA observations', 'observed'); plot(observed, chartReadiness(item, state.data.sources));
      const table = create('details', 'disclosure'); table.append(create('summary', '', 'Sourced observation records')); const tableBody = create('div'); observationTable(tableBody, item.evidence); table.append(tableBody); observed.append(table);
      experimentalConditions(host, item.evidence);
      const statements = [...item.evidence, ...arr(item.supported_claims).filter(x => x && typeof x === 'object')];
      const authors = create('details', 'disclosure'); authors.append(create('summary', '', 'Author conclusions')); const authorBody = create('div'); authorBody.append(tag('author')); roleStatements(authorBody, statements, 'author', 'No separate author-conclusion statement is supplied. Observations are not silently relabeled as author conclusions.'); authors.append(authorBody); host.append(authors);
      const other = item.evidence.filter(e => ['guidance', 'model', 'unknown'].includes(roleOf(e)));
      if (other.length) { const detail = create('details', 'disclosure'); detail.append(create('summary', '', 'Other evidence and attribution')); const body = create('div'); for (const e of other) { const row = create('div', 'evidence-item'); row.append(tag(roleOf(e)), create('p', '', readable(e) || 'Statement not separately supplied')); const chips = create('div', 'source-chips'); sources(chips, sourceIds(e)); row.append(chips); body.append(row); } detail.append(body); host.append(detail); }
      const earth = section(host, 'Earth comparison'); const comparison = item.earth_comparison;
      if (comparison && typeof comparison === 'object' && !Array.isArray(comparison)) {
        earth.append(create('p', 'earth-state', 'Comparison status: ' + str(comparison.kind || comparison.status || comparison.match_status || 'unknown').replace(/_/g, ' ')));
        if (readable(comparison)) earth.append(create('p', '', readable(comparison)));
        const columns = create('div', 'comparison-grid');
        for (const [label, values] of [['Reported similarities', comparison.same_conditions || comparison.similarities || comparison.matched_conditions], ['Differences and unknowns', comparison.different_conditions || comparison.differences || comparison.unmatched_conditions]]) { const col = create('div'); col.append(create('h4', '', label)); lines(col, values, 'Not separately supplied.'); columns.append(col); }
        earth.append(columns); const chips = create('div', 'source-chips'); sources(chips, sourceIds(comparison)); earth.append(chips);
        lines(earth, comparison.limits);
      } else earth.append(create('p', '', readable(comparison) || 'No matched Earth comparator is established by this case.'));
      const strategy = section(host, 'Strategy to investigate', 'physical'); strategy.append(create('p', '', readable(item.strategy) || 'A separate strategy statement has not been supplied.')); roleStatements(strategy, statements, 'physical', 'No separate physical-inference statement is supplied.');
      const product = section(host, 'Product concept to test', 'product'); product.append(create('p', '', readable(item.product_concept) || 'No product concept supplied.'), create('p', 'small-note', 'A concept is not a demonstrated product, purchasing recommendation or validated safety measure.'));
      if (arr(item.related_concepts).length) {
        const related = create('details', 'disclosure'); related.append(create('summary', '', 'Related concepts · separate source cases (' + item.related_concepts.length + ')'));
        const body = create('div'); body.append(create('p', 'small-note', 'Each concept keeps its own source-case identity. Its measurements are not added to the selected-case graph.'));
        for (const concept of item.related_concepts) {
          const row = create('article', 'related-concept'); row.append(create('h4', '', concept.title_en || 'Related concept'));
          row.append(create('p', 'source-case-id', 'Source case: ' + (concept.source_case_id || 'unknown')));
          if (concept.summary_en) row.append(create('p', '', concept.summary_en));
          const copy = concept.english_copy || {};
          const strategyText = englishText(concept.strategy_en || copy.strategy || concept.strategy);
          if (strategyText) row.append(tag('physical'), create('p', '', strategyText));
          else if (readable(concept.strategy)) row.append(create('p', 'small-note', 'Detailed source strategy is in the source language; reviewed English copy is pending. The available English summary remains above.'));
          const product = concept.product_concept_en || copy.product_concept || concept.product_concept;
          if (typeof product === 'string' && englishText(product)) row.append(tag('product'), create('p', '', product));
          else if (product && typeof product === 'object') {
            row.append(tag('product'));
            if (product.name_en) row.append(create('h4', '', product.name_en));
            for (const field of ['summary_en', 'description_en', 'proposed_function_en', 'maturity', 'status', 'source_support']) if (englishText(product[field])) row.append(create('p', '', englishText(product[field])));
            const rawFunctions = arr(product.proposed_functions_en || product.proposed_functions);
            const functions = rawFunctions.map(englishText).filter(Boolean); lines(row, functions);
            if (rawFunctions.some(value => readable(value) && !englishText(value))) row.append(create('p', 'small-note', 'Some detailed product functions remain in the source language; reviewed English copy is pending.'));
            if (englishText(product.proposed_function)) row.append(create('p', '', englishText(product.proposed_function)));
            if (readable(product.proposed_function) && !englishText(product.proposed_function)) row.append(create('p', 'small-note', 'Detailed product function is in the source language; reviewed English copy is pending.'));
          }
          row.append(create('h5', '', 'Not established / limitations'), create('p', 'small-note', 'These are limits or unsupported claims, not demonstrated product outcomes.'));
          lines(row, concept.limits); const links = create('div', 'source-chips'); sources(links, concept.source_ids); row.append(links); body.append(row);
        }
        related.append(body); product.append(related);
      }
      const validation = create('details', 'disclosure'); validation.append(create('summary', '', 'What needs validation')); const validationBody = create('div'); lines(validationBody, item.next_validation, 'Validation requirements are not supplied.'); validation.append(validationBody); host.append(validation);
      const limits = create('details', 'disclosure'); limits.append(create('summary', '', 'Supported claims and limits')); const limitsBody = create('div'); limitsBody.append(create('p', '', 'Product effectiveness is not established. Research priority is not a safety-confidence score, equipment approval or permission for field use.'), create('h4', '', 'Supplied supported claims')); lines(limitsBody, item.supported_claims, 'Not supplied.'); limitsBody.append(create('h4', '', 'Not established')); lines(limitsBody, item.unsupported_claims, 'No independent safety or effectiveness claim is established.'); limits.append(limitsBody); host.append(limits);
      const literature = section(host, 'Literature and original sources');
      const refs = [...arr(item.literature).map(x => typeof x === 'string' ? x : x.source_id || x.id), ...item.evidence.flatMap(sourceIds)].filter(Boolean);
      const chips = create('div', 'source-chips'); sources(chips, refs); literature.append(chips);
      if (!refs.length) literature.append(create('p', 'data-gap', 'No source identity is supplied for this case.'));
      const papers = create('details', 'disclosure'); papers.append(create('summary', '', 'Source summaries and exact locators')); const paperBody = create('div');
      for (const reference of arr(item.literature).filter(x => x && typeof x === 'object')) {
        const row = create('div', 'evidence-item'), s = state.sources.get(reference.source_id || reference.id);
        row.append(create('h4', '', reference.title || s && s.title || 'Source title unknown'));
        if (reference.paraphrase) row.append(create('p', '', reference.paraphrase));
        const locator = reference.source_locator || reference.locator;
        if (locatorText(locator)) row.append(create('p', 'small-note', locatorText(locator)));
        const links = create('div', 'source-links');
        if (s && locator && locator.pdf_page) link(links, 'Open cited PDF page ' + locator.pdf_page + ' ↗', pageUrl(s, locator.pdf_page, window.location.href));
        link(links, 'Official source ↗', sourceUrl(reference.url || s && s.url, null, window.location.href)); row.append(links); paperBody.append(row);
      }
      if (paperBody.children.length) { papers.append(paperBody); literature.append(papers); }
    }
    function updateLocation() {
      if (!window.history || !window.history.replaceState) return;
      const u = new URL(window.location.href); if (state.selected) u.searchParams.set('case', state.selected); else u.searchParams.delete('case'); const query = $('strategy-query').value.trim(); if (query) u.searchParams.set('q', query); else u.searchParams.delete('q'); window.history.replaceState(null, '', u.href);
    }
    async function load(initial) {
      const request = ++state.request; $('strategy-search-button').disabled = true; $('strategy-error').hidden = true; $('strategy-retry').hidden = true; $('strategy-scope-message').hidden = true; $('strategy-status').textContent = 'Loading reviewed priorities…';
      const query = $('strategy-query').value.trim();
      try {
        const response = await fetch(API + (query ? '?q=' + encodeURIComponent(query) : ''), { headers: { Accept: 'application/json' }, cache: 'no-store' });
        if (!response.ok) throw new Error('The reviewed strategy service is unavailable (HTTP ' + response.status + ').');
        const data = validateCatalog(await response.json()); if (request !== state.request) return;
        state.data = data;
        $('strategy-review-status').hidden = !(data.preview === true || /pending|draft/i.test(str(data.status)));
        const outOfScope = data.query_scope && data.query_scope.status === 'out_of_scope';
        $('strategy-scope-message').hidden = !outOfScope;
        $('strategy-scope-message').textContent = outOfScope ? str(data.query_scope.message) || 'The supplied catalog classifies this query as out of scope. No strategy match is supplied.' : '';
        state.visible = visibleCases(data, query);
        const requested = initial ? new URL(window.location.href).searchParams.get('case') : null;
        const visibleIds = new Set(state.visible.map(c => c.id));
        state.selected = !state.visible.length ? null : requested ? data.cases.some(c => c.id === requested) ? requested : null : visibleIds.has(state.selected) ? state.selected : visibleIds.has(data.selected_case_id) ? data.selected_case_id : null;
        state.explicitUnmatched = Boolean(requested && state.selected && !visibleIds.has(state.selected));
        $('ranking-method').textContent = 'Prioritized by source completeness and fire-safety relevance.';
        renderSources(); renderPriorities(); renderCase(); $('strategy-query').disabled = false; $('strategy-search-button').disabled = false;
        $('strategy-status').textContent = state.visible.length + (query ? ' supplied query matches' : ' supplied research priorities') + (query ? ' · query: ' + query : '') + (requested && !state.selected && state.visible.length ? ' · requested case not found' : '');
        updateLocation();
      } catch (error) {
        if (request !== state.request) return;
        state.data = null; state.selected = null; $('priority-list').replaceChildren(); $('selected-case').replaceChildren(create('p', 'empty', 'No case or experimental graph has been substituted.')); $('strategy-sources').replaceChildren(); $('strategy-source-library').hidden = true;
        $('strategy-review-status').hidden = true;
        $('strategy-scope-message').hidden = true;
        $('strategy-status').textContent = 'Reviewed priorities unavailable'; $('strategy-error').textContent = error.message; $('strategy-error').hidden = false; $('strategy-retry').hidden = false; $('strategy-query').disabled = false; $('strategy-search-button').disabled = false;
      }
    }
    $('strategy-search-form').addEventListener('submit', event => { event.preventDefault(); load(false); }); $('strategy-retry').addEventListener('click', () => load(false));
    $('strategy-query').value = new URL(window.location.href).searchParams.get('q') || ''; load(true);
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { validateCatalog, visibleCases, editorialScore, roleOf, chartReadiness, sourceUrl, pageUrl, locatorText };
  if (typeof document !== 'undefined') start();
}());
