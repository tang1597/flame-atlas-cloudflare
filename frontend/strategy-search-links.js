/* Query-linked strategy navigation. No predictions or changes to study ranking. */
(function (global) {
  'use strict';
  const states = new Map();
  function node(tag, text, parent) {
    const el = document.createElement(tag);
    if (text != null) el.textContent = String(text);
    if (parent) parent.appendChild(el);
    return el;
  }
  function caseLink(id, query) {
    return 'strategies.html?' + new URLSearchParams({case: id, q: query}).toString();
  }
  function reset(root, state) {
    state.serial += 1;
    state.controller?.abort();
    state.controller = null;
    root.replaceChildren();
    root.hidden = true;
  }
  async function sync(input = {}) {
    const root = document.getElementById(input.targetId || 'strategy-search-links');
    if (!root) return;
    let state = states.get(root);
    if (!state) { state = {serial: 0, signature: '', controller: null}; states.set(root, state); }
    const query = typeof input.query === 'string' ? input.query.trim() : '';
    const pillar = typeof input.filters?.pillar === 'string' ? input.filters.pillar : '';
    if (input.phase !== 'ready' || !query) {
      state.signature = '';
      reset(root, state);
      return;
    }
    const signature = JSON.stringify([query, pillar]);
    if (state.signature === signature) return;
    reset(root, state);
    state.signature = signature;
    const serial = state.serial;
    state.controller = new AbortController();
    try {
      const response = await global.fetch('/api/fire-strategies?' + new URLSearchParams({q: query}), {cache: 'no-store', signal: state.controller.signal});
      if (!response.ok) return;
      const payload = await response.json();
      if (serial !== state.serial) return;
      if (!Array.isArray(payload.cases) || !Array.isArray(payload.matching_case_ids)) return;
      const outsideScope = payload.query_scope?.status === 'out_of_scope';
      const ids = new Set(outsideScope ? [] : payload.matching_case_ids);
      const matches = payload.cases.filter(item => {
        if (!item || typeof item.id !== 'string' || typeof item.title_en !== 'string' || !ids.has(item.id)) return false;
        const pillars = Array.isArray(item.pillar) ? item.pillar : [item.pillar];
        return !pillar || pillars.includes(pillar);
      });
      root.replaceChildren();
      node('h2', 'Related fire-safety strategies', root);
      const note = node('p', 'Catalog text matches for “' + query + '”. Priorities are supplied by the evidence review; test conditions remain case-specific.', root);
      note.className = 'small-note';
      if (!matches.length) {
        const message = outsideScope && typeof payload.query_scope.message === 'string' ? payload.query_scope.message : 'No reviewed strategy matches these terms and safety focus. This does not establish that the scenario is safe.';
        node('p', message, root).className = 'small-note';
      } else {
        const list = node('ul', null, root);
        for (const item of matches.slice(0, 3)) {
          const row = node('li', null, list);
          const link = node('a', item.title_en, row);
          link.href = caseLink(item.id, query);
          if (Number.isInteger(item.rank)) node('span', ' · Evidence priority ' + item.rank, row).className = 'small-note';
          const reason = Array.isArray(item.rank_reasons) ? item.rank_reasons.find(value => typeof value === 'string' && !/[\u3400-\u9fff]/.test(value)) : null;
          if (reason) node('p', reason, row).className = 'small-note';
        }
      }
      const all = node('a', 'Open fire-safety strategies →', root);
      all.href = 'strategies.html?' + new URLSearchParams({q: query}).toString();
      root.hidden = false;
    } catch (error) {
      if (serial === state.serial) { root.replaceChildren(); root.hidden = true; }
    }
  }
  global.FlameStrategySearchLinks = Object.freeze({sync});
})(typeof window !== 'undefined' ? window : globalThis);
