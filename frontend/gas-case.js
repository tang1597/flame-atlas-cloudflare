(function () {
  'use strict';
  const ENDPOINT = '/api/case-studies/gas-isolation';
  const ROLE_LABELS = { guidance: 'Guidance', related_experiment: 'Related experiment', unknown: 'Unknown' };
  const STOP = new Set('a an and are as at be by can do does for from how i if in is it of on or our that the their then there these they this to was we what when where which with would your'.split(' '));
  const list = value => Array.isArray(value) ? value : [];
  const words = value => String(value || '').toLowerCase().match(/[\p{L}\p{N}]+/gu) || [];
  const tokens = value => [...new Set(words(value).filter(word => word.length > 1 && !STOP.has(word)))];
  const text = value => typeof value === 'string' ? value : '';

  function validatePayload(payload) {
    if (!payload || !Array.isArray(payload.conditions) || !payload.conditions.length || !Array.isArray(payload.sources)) {
      throw new Error('The case-evidence response is incomplete.');
    }
    const ids = new Set();
    for (const condition of payload.conditions) {
      if (!condition || !text(condition.id) || ids.has(condition.id) || !text(condition.title) || typeof condition.condition !== 'string') {
        throw new Error('A research branch has missing or duplicate source identity.');
      }
      ids.add(condition.id);
      for (const key of ['intervention_basis', 'secondary_risks', 'gaps', 'unknowns', 'not_established', 'source_ids', 'source_locators']) {
        if (!Array.isArray(condition[key])) throw new Error('A research branch is missing its evidence or uncertainty fields.');
      }
      if (condition.field_procedure !== null) throw new Error('This research page does not publish field-operating procedures.');
    }
    return payload;
  }

  function rankConditions(conditions, query, branch, order) {
    const terms = tokens(query);
    return conditions.map((condition, index) => {
      const title = condition.title.toLowerCase();
      const context = condition.condition.toLowerCase();
      const all = [condition.title, condition.condition, text(condition.evidence_grade),
        ...list(condition.intervention_basis).map(item => item.text),
        ...list(condition.secondary_risks).map(item => item.text),
        ...list(condition.gaps), ...list(condition.unknowns), ...list(condition.not_established)]
        .filter(value => typeof value === 'string').join(' ').toLowerCase();
      const matched = terms.filter(term => all.includes(term));
      const score = matched.reduce((sum, term) => sum + (title.includes(term) ? 4 : context.includes(term) ? 2 : 1), 0);
      return { condition, index, matched, score };
    }).filter(item => (!branch || item.condition.id === branch) && (!terms.length || item.matched.length))
      .sort((a, b) => order === 'source_order' ? a.index - b.index : b.score - a.score || a.index - b.index);
  }

  function sourceUrl(value, page, base, knownPdf) {
    if (!text(value) || /^[A-Za-z]:[\\/]/.test(value) || value.startsWith('\\\\')) return null;
    try {
      const url = new URL(value, base || 'http://localhost/');
      if (!['http:', 'https:'].includes(url.protocol)) return null;
      if ((knownPdf || /\.pdf$/i.test(url.pathname)) && Number.isInteger(Number(page)) && Number(page) > 0) url.hash = 'page=' + Number(page);
      return url.href;
    } catch (_) { return null; }
  }

  function start() {
    const $ = id => document.getElementById(id);
    const state = { payload: null, sourceCards: new Map(), sourceIndex: new Map() };
    const create = (tag, className, value) => {
      const node = document.createElement(tag);
      if (className) node.className = className;
      if (value !== undefined) node.textContent = String(value);
      return node;
    };
    const roleTag = role => create('span', 'gas-role gas-role-' + (role === 'related_experiment' ? 'related' : role === 'guidance' ? 'guidance' : 'unknown'), ROLE_LABELS[role] || ROLE_LABELS.unknown);
    function appendList(parent, values, emptyMessage) {
      const items = list(values).filter(value => typeof value === 'string' && value.trim());
      if (!items.length) { parent.append(create('p', 'small-note', emptyMessage || 'Not supplied by the reviewed case.')); return; }
      const ul = create('ul', 'gas-list');
      for (const item of items) ul.append(create('li', '', item));
      parent.append(ul);
    }
    function highlightSource(id) {
      const card = state.sourceCards.get(id);
      if (!card) return;
      $('gas-source-library').open = true;
      for (const item of state.sourceCards.values()) item.classList.remove('is-highlighted');
      card.classList.add('is-highlighted');
      card.focus({ preventScroll: true });
      card.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    function sourceChips(parent, ids) {
      for (const id of [...new Set(list(ids))]) {
        const card = state.sourceCards.get(id);
        if (!card) { parent.append(create('span', 'gas-role gas-role-unknown', 'Unknown source: ' + id)); continue; }
        const a = create('a', 'gas-source-link', id);
        a.href = '#' + card.id;
        a.setAttribute('aria-label', 'Show source card ' + id);
        a.addEventListener('click', event => { event.preventDefault(); highlightSource(id); });
        parent.append(a);
      }
    }
    function externalLink(parent, label, url) {
      if (!url) return;
      const a = create('a', '', label);
      a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer';
      parent.append(a);
    }
    function renderSources() {
      const host = $('gas-sources'); host.replaceChildren();
      state.sourceCards.clear(); state.sourceIndex.clear();
      const locators = new Map();
      for (const condition of state.payload.conditions) {
        for (const locator of condition.source_locators) {
          if (!locator || !locator.source_id) continue;
          if (!locators.has(locator.source_id)) locators.set(locator.source_id, []);
          locators.get(locator.source_id).push({ ...locator, branchTitle: condition.title });
        }
      }
      state.payload.sources.forEach((source, index) => {
        const card = create('article', 'gas-source-card');
        card.id = 'gas-source-' + (index + 1); card.tabIndex = -1;
        state.sourceCards.set(source.id, card); state.sourceIndex.set(source.id, source);
        card.append(roleTag(source.role), create('h3', '', source.title || 'Source title unknown'));
        card.append(create('p', '', [source.authority, source.id].filter(Boolean).join(' · ')));
        if (source.section) card.append(create('p', '', source.section));
        if (source.scope) card.append(create('p', '', source.scope));
        const links = create('div', 'gas-official-links');
        const official = sourceUrl(source.url, null, window.location.href);
        const reviewed = sourceUrl(source.local_pdf_url, source.pdf_page, window.location.href, true);
        externalLink(links, 'Official source ↗', official);
        if (reviewed && reviewed !== official) externalLink(links, 'Reviewed PDF ↗', reviewed);
        for (const link of list(source.direct_page_links)) {
          const pageUrl = reviewed
            ? sourceUrl(source.local_pdf_url, link.physical_pdf_page, window.location.href, true)
            : sourceUrl(link.url, null, window.location.href);
          externalLink(links, 'PDF page ' + link.physical_pdf_page + ' ↗', pageUrl);
        }
        if (!official && !reviewed) links.append(create('span', 'gas-role gas-role-unknown', 'Source link unknown'));
        card.append(links);
        const references = locators.get(source.id) || [];
        if (references.length) {
          const ul = create('ul', 'gas-locator-list');
          const seen = new Set();
          for (const locator of references) {
            const label = [locator.pdf_page ? 'PDF page ' + locator.pdf_page : '', locator.section, locator.locator].filter(Boolean).join(' · ');
            if (!label || seen.has(label)) continue;
            seen.add(label);
            const li = create('li');
            const pinned = list(source.direct_page_links).find(link => Number(link.physical_pdf_page) === Number(locator.pdf_page));
            const localPage = sourceUrl(source.local_pdf_url, locator.pdf_page, window.location.href, true);
            const url = localPage || sourceUrl(pinned ? pinned.url : source.url, locator.pdf_page, window.location.href);
            if (url && locator.pdf_page && (pinned || localPage || /\.pdf(?:[?#]|$)/i.test(url))) externalLink(li, label + ' ↗', url);
            else li.textContent = label;
            ul.append(li);
          }
          card.append(ul);
        }
        if (source.edition || source.sha256) {
          const details = create('details'); details.append(create('summary', '', 'Source edition'));
          if (source.edition) details.append(create('p', 'gas-source-edition', source.edition));
          if (source.sha256) details.append(create('p', 'gas-source-edition', 'SHA-256: ' + source.sha256));
          card.append(details);
        }
        host.append(card);
      });
      $('gas-source-count').textContent = '(' + state.payload.sources.length + ')';
    }
    function evidenceItems(parent, values) {
      if (!values.length) { parent.append(roleTag('unknown'), create('p', '', 'No source-bound statement supplied.')); return; }
      for (const item of values) {
        const row = create('div', 'gas-evidence-item');
        row.append(roleTag(item.role), create('p', '', item.text || 'Statement unknown'));
        const links = create('div', 'gas-source-links'); sourceChips(links, item.source_ids); row.append(links);
        parent.append(row);
      }
    }
    function column(label, open) {
      const details = create('details', 'gas-column'); details.open = open;
      const body = create('div', 'gas-column-body');
      details.append(create('summary', '', label), body);
      return { details, body };
    }
    function renderResults() {
      if (!state.payload) return;
      const query = $('gas-query').value.trim();
      const ranked = rankConditions(state.payload.conditions, query, $('gas-scenario').value, $('gas-sort').value);
      const host = $('gas-results'); host.replaceChildren();
      $('gas-status').textContent = ranked.length + ' of ' + state.payload.conditions.length + ' research branches' + (query ? ' · local text match' : ' · source order');
      if (!ranked.length) { host.append(create('p', 'gas-empty', 'No case text matches this search and branch filter. Try another term or clear the search. Unknown conditions remain unknown.')); return; }
      ranked.forEach((item, index) => {
        const condition = item.condition;
        const card = create('article', 'gas-case-card');
        const heading = create('div', 'gas-case-heading');
        heading.append(create('h3', '', condition.title), create('span', 'gas-unknown', 'Safety not assessed'));
        card.append(heading, create('p', 'gas-match', item.matched.length ? 'Text contains: ' + item.matched.join(', ') + '. Match is relevance only.' : 'Source order. This branch may overlap with other branches.'));
        if (text(condition.evidence_grade)) card.append(create('p', 'gas-grade', condition.evidence_grade.replace(/_/g, ' ')));
        const grid = create('div', 'gas-columns');
        const expand = index === 0;
        const conditions = column('Conditions', expand);
        conditions.body.append(create('p', '', condition.condition));
        if (condition.unknowns.length) { conditions.body.append(create('h4', '', 'Unknown scenario inputs')); appendList(conditions.body, condition.unknowns); }
        const intervention = column('Intervention basis', expand); evidenceItems(intervention.body, condition.intervention_basis);
        const risks = column('Secondary risks', expand); evidenceItems(risks.body, condition.secondary_risks);
        const gaps = column('Data gaps', expand); appendList(gaps.body, condition.gaps, 'No complete measurement set is established here.');
        if (condition.not_established.length) { gaps.body.append(create('h4', '', 'Not established')); appendList(gaps.body, condition.not_established); }
        grid.append(conditions.details, intervention.details, risks.details, gaps.details); card.append(grid);
        const sources = create('div', 'gas-case-sources'); sources.append(create('span', '', 'Sources')); sourceChips(sources, condition.source_ids); card.append(sources);
        host.append(card);
      });
    }
    function queryOptions() {
      const host = $('gas-next-options'); host.replaceChildren();
      for (const item of list(state.payload.next_options)) {
        const query = typeof item === 'string' ? item : text(item.query) || text(item.query_terms) || text(item.question) || text(item.label);
        const label = typeof item === 'string' ? item : text(item.label) || query;
        if (!query) continue;
        const button = create('button', '', label); button.type = 'button';
        button.addEventListener('click', () => { $('gas-query').value = query; $('gas-scenario').value = ''; renderResults(); });
        host.append(button);
      }
      host.hidden = !host.children.length;
    }
    function contextNotes() {
      const host = $('gas-input-content'); host.replaceChildren();
      const fields = list(state.payload.input_fields).map(item => typeof item === 'string' ? item : [item.label || item.name || item.id, item.description || item.question || item.role].filter(Boolean).join(': ')).filter(Boolean);
      appendList(host, fields); $('gas-input-notes').hidden = !fields.length;
      const limits = $('gas-limits-content'); limits.replaceChildren();
      const values = list(state.payload.limits).map(item => typeof item === 'string' ? item : text(item.text) || text(item.description)).filter(Boolean);
      appendList(limits, values); $('gas-limits').hidden = !values.length;
    }
    function relatedRecords() {
      const host = $('gas-related-content'); host.replaceChildren();
      for (const record of list(state.payload.related_records)) {
        const row = create('div', 'gas-evidence-item');
        row.append(roleTag(record.role), create('h3', '', record.title || 'Related record'));
        if (record.scope) row.append(create('p', '', record.scope));
        appendList(row, record.limits, 'A matched intervention test is not established by this record.');
        const links = create('div', 'gas-source-links'); sourceChips(links, record.source_ids); row.append(links);
        host.append(row);
      }
      $('gas-related').hidden = !host.children.length;
    }
    function setEnabled(value) {
      for (const id of ['gas-query', 'gas-search-button', 'gas-scenario', 'gas-sort', 'gas-clear']) $(id).disabled = !value;
    }
    async function load() {
      setEnabled(false); $('gas-error').hidden = true; $('gas-retry').hidden = true;
      $('gas-status').textContent = 'Loading reviewed cases…';
      try {
        const response = await fetch(ENDPOINT, { headers: { Accept: 'application/json' }, cache: 'no-store' });
        if (!response.ok) throw new Error('The case-evidence service is unavailable (HTTP ' + response.status + ').');
        state.payload = validatePayload(await response.json());
        $('gas-summary').textContent = text(state.payload.summary) || 'Explore source-bound intervention principles, secondary risks and missing evidence.';
        const select = $('gas-scenario'); select.replaceChildren();
        const all = create('option', '', 'All branches'); all.value = ''; select.append(all);
        for (const condition of state.payload.conditions) { const option = create('option', '', condition.title); option.value = condition.id; select.append(option); }
        renderSources(); contextNotes(); queryOptions(); relatedRecords(); setEnabled(true); renderResults();
      } catch (error) {
        state.payload = null; $('gas-results').replaceChildren(); $('gas-sources').replaceChildren();
        $('gas-status').textContent = 'Case evidence unavailable';
        $('gas-error').textContent = error.message + ' No replacement case or safety assessment has been generated.';
        $('gas-error').hidden = false; $('gas-retry').hidden = false;
      }
    }
    $('gas-search-form').addEventListener('submit', event => { event.preventDefault(); renderResults(); });
    $('gas-scenario').addEventListener('change', renderResults);
    $('gas-sort').addEventListener('change', renderResults);
    $('gas-clear').addEventListener('click', () => { $('gas-query').value = ''; $('gas-scenario').value = ''; $('gas-sort').value = 'text_match'; renderResults(); });
    $('gas-retry').addEventListener('click', load);
    load();
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { tokens, rankConditions, sourceUrl, validatePayload };
  if (typeof document !== 'undefined') start();
}());
