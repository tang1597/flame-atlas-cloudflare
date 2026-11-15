/* Source-context renderer only. No retrieval, classification or numerical inference. */
(function (global) {
  'use strict';
  const SCHEMA = 'iss-fire-context-v1';
  const POLICY = 'This panel does not classify an experiment as controlled/uncontrolled from a numeric slider or model result.';
  const KINDS = Object.freeze({ official_requirement: 'Official requirement', reviewer_synthesis: 'Reviewer synthesis', not_defined: 'Not defined' });
  const doc = global.document || (typeof document !== 'undefined' ? document : null);
  const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
  const own = (value, key) => object(value) && Object.prototype.hasOwnProperty.call(value, key);
  const array = value => Array.isArray(value) ? value : value === null || value === undefined ? [] : [value];
  function first(value, keys) { for (const key of keys) if (own(value, key)) return value[key]; return undefined; }
  function safeString(value, key = '') {
    if (value === null || value === undefined || value === '') return 'Not supplied';
    if (typeof value === 'number') return Number.isFinite(value) ? String(value) : 'Non-finite value not displayed';
    if (typeof value === 'boolean') return value ? 'true' : 'false';
    if (typeof value !== 'string') return 'Unstructured value';
    if (/https?:\/\/[^/\s]*@/i.test(value)) return 'Credential-bearing URL withheld';
    if (/path|local_file|filename/i.test(key) || /(?:(?:^|[\s"'(])[a-z]:[\\/]|file:\/\/|\\\\[^\\\s]+\\)/i.test(value) || /^(?:\/|\.\.?\/|~\/)/.test(value)) return 'Local path withheld';
    return value;
  }
  const quoteKey = key => /quote|source_sentence|source_sentences|excerpt|cited.?sentence/i.test(key);
  function publicValue(value, key = '', depth = 0) {
    if (depth > 6) return 'Nested detail omitted';
    if (Array.isArray(value)) return value.map(item => publicValue(item, key, depth + 1));
    if (object(value)) return Object.fromEntries(Object.entries(value).filter(([name]) => !quoteKey(name)).map(([name, item]) => [name, publicValue(item, name, depth + 1)]));
    return typeof value === 'string' ? safeString(value, key) : typeof value === 'number' && !Number.isFinite(value) ? 'Non-finite value not displayed' : value;
  }
  function text(value) { return object(value) || Array.isArray(value) ? JSON.stringify(publicValue(value), null, 2) : safeString(value); }
  function node(tag, className, value, parent) {
    const element = doc.createElement(tag); if (className) element.className = className;
    if (value !== undefined && value !== null) element.textContent = String(value);
    if (parent) parent.append(element); return element;
  }
  function container(value) {
    const root = typeof value === 'string' && doc ? doc.querySelector(value) : value;
    if (!root || typeof root.replaceChildren !== 'function') throw new TypeError('Supply a DOM container for ISS fire context.'); return root;
  }
  function base(value) {
    const root = container(value); root.replaceChildren(); root.classList.add('iss-context'); root.setAttribute('aria-label', 'ISS fire-safety source context');
    node('h3', 'iss-heading', 'ISS fire-safety context', root);
    const note = node('p', 'iss-policy-note', POLICY, root); note.setAttribute('role', 'note'); return root;
  }
  function clear(value, reason) {
    const root = base(value); const message = typeof reason === 'string' && reason.trim() ? safeString(reason) : 'ISS fire-context source statements are pending. No official definition or requirement is inferred.';
    const status = node('p', 'iss-status iss-pending', message, root); status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
    return { status: 'pending', items: 0, documents: 0, displayedSentences: 0, withheldSentences: 0 };
  }
  function safeURL(value) {
    if (typeof value !== 'string' || !/^https?:\/\//i.test(value)) return null;
    try { const url = new URL(value); return ['http:', 'https:'].includes(url.protocol) && !url.username && !url.password ? url.href : null; } catch (_) { return null; }
  }
  function sourceId(source) { const id = first(source, ['id', 'source_id', 'document_id']); return typeof id === 'string' ? id : null; }
  function sourceSha(source) { const value = first(source, ['sha256', 'source_sha256', 'pdf_sha256', 'file_sha256', 'sha']); return typeof value === 'string' && /^[a-f0-9]{64}$/i.test(value) ? value.toLowerCase() : null; }
  function sourceEdition(source) { const value = first(source, ['edition', 'source_edition', 'source_version', 'source_version_id', 'version_id']); return typeof value === 'string' && value.trim() ? value : null; }
  function pages(value) {
    const field = first(value, ['pdf_page', 'physical_pdf_page', 'physicalPdfPage', 'physical_pdf_pages']);
    const values = array(field); return values.length && values.every(page => Number.isSafeInteger(page) && page > 0) ? [...new Set(values)] : [];
  }
  function sourceKey(source) { return JSON.stringify([sourceId(source), sourceSha(source), sourceEdition(source), first(source, ['title', 'name']), first(source, ['url', 'source_url', 'nasa_url'])]); }
  function sourceObjects(value) { return array(value).filter(object); }
  function additional(parent, value, excluded) {
    if (!object(value)) return;
    const fields = Object.fromEntries(Object.entries(value).filter(([key]) => !excluded.has(key) && !quoteKey(key)));
    if (!Object.keys(fields).length) return;
    const details = node('details', 'iss-details iss-additional', null, parent); node('summary', '', 'Additional supplied fields · uninterpreted', details); node('pre', '', JSON.stringify(publicValue(fields), null, 2), details);
  }
  function sourceCard(parent, source) {
    const details = node('details', 'iss-source iss-details', null, parent);
    const title = first(source, ['title', 'name']); node('summary', '', 'Source · ' + (typeof title === 'string' && title.trim() ? safeString(title) : 'Title not supplied'), details);
    node('p', 'iss-source-version', 'Edition / version: ' + safeString(sourceEdition(source)), details);
    const sha = sourceSha(source); node('p', 'iss-source-sha', 'SHA-256: ' + (sha || 'Not supplied as a valid 64-hex SHA'), details);
    const physical = pages(source); node('p', 'iss-source-page', 'Physical PDF page: ' + (physical.length ? physical.join(', ') : 'Not supplied as a positive integer'), details);
    for (const key of ['section', 'locator']) if (own(source, key)) node('p', 'iss-source-location', key.charAt(0).toUpperCase() + key.slice(1) + ': ' + text(source[key]), details);
    const links = node('div', 'iss-source-links', null, details);
    const url = safeURL(first(source, ['url', 'source_url', 'nasa_url']));
    if (url) { const link = node('a', 'iss-source-link', 'Open public source ↗', links); link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; }
    else node('p', 'iss-source-missing', 'Public HTTP(S) source URL not supplied.', links);
    if (typeof source.doi === 'string' && source.doi.trim()) {
      const raw = /^10\.\d{4,9}\/\S+$/i.test(source.doi) ? 'https://doi.org/' + source.doi : source.doi;
      const doi = safeURL(raw); if (doi) { const link = node('a', 'iss-source-link', 'DOI ↗', links); link.href = doi; link.target = '_blank'; link.rel = 'noopener noreferrer'; }
    }
    if (sourceId(source)) node('p', 'iss-source-id', 'Supplied source ID: ' + safeString(sourceId(source)), details);
    additional(details, source, new Set(['id', 'source_id', 'document_id', 'title', 'name', 'edition', 'source_edition', 'source_version', 'source_version_id', 'version_id', 'sha256', 'source_sha256', 'pdf_sha256', 'file_sha256', 'sha', 'pdf_page', 'physical_pdf_page', 'physicalPdfPage', 'physical_pdf_pages', 'url', 'source_url', 'nasa_url', 'doi', 'section', 'locator']));
  }
  function associatedSources(item, documents, byId) {
    const result = [], unresolved = [];
    const inline = first(item, ['source', 'sources']);
    for (const entry of array(inline)) {
      if (object(entry)) result.push(entry);
      else if (typeof entry === 'string' && byId.has(entry)) result.push(byId.get(entry));
      else if (typeof entry === 'string' && safeURL(entry)) result.push({ url: entry });
      else if (entry !== null && entry !== undefined) unresolved.push(entry);
    }
    const refs = first(item, ['source_ids', 'document_ids']);
    for (const id of [...array(refs), ...array(first(item, ['source_id', 'document_id']))]) {
      if (typeof id === 'string' && byId.has(id)) result.push(byId.get(id)); else if (id !== null && id !== undefined) unresolved.push(id);
    }
    const seen = new Set(); return { sources: result.filter(source => { const key = sourceKey(source); if (seen.has(key)) return false; seen.add(key); return true; }), unresolved };
  }
  function showFields(parent, title, value, className) {
    const values = array(value); if (!values.length) return;
    const details = node('details', 'iss-details ' + className, null, parent); node('summary', '', title, details);
    const list = node('ul', 'iss-field-list', null, details); values.forEach(entry => node('li', '', text(entry), list));
  }
  function quoteVerified(quote) {
    const flags = ['verified', 'current_contiguous_whitespace_only_match'];
    if (flags.some(key => own(quote, key) && quote[key] !== true)) return false;
    const status = typeof quote.verification_status === 'string' ? quote.verification_status.trim().toLowerCase() : null;
    if (own(quote, 'verification_status') && status !== 'verified') return false;
    return flags.some(key => quote[key] === true) || status === 'verified';
  }
  function paperGroups(sources) {
    const parents = sources.map((_, index) => index), aliases = new Map();
    function root(index) { while (parents[index] !== index) { parents[index] = parents[parents[index]]; index = parents[index]; } return index; }
    sources.forEach((source, index) => {
      const doi = typeof source.doi === 'string' ? source.doi.trim().replace(/^https?:\/\/(?:dx\.)?doi\.org\//i, '').replace(/^doi:\s*/i, '').toLowerCase() : '';
      const keys = [typeof source.work_id === 'string' && source.work_id.trim() ? 'work:' + source.work_id.trim().toLowerCase() : '', typeof source.paper_id === 'string' && source.paper_id.trim() ? 'paper:' + source.paper_id.trim().toLowerCase() : '', doi ? 'doi:' + doi : '', sourceSha(source) ? 'sha:' + sourceSha(source) : ''].filter(Boolean);
      for (const key of keys) { if (aliases.has(key)) parents[root(index)] = root(aliases.get(key)); else aliases.set(key, index); }
    });
    return new Map(sources.map((source, index) => [source, root(index)]));
  }
  function quotes(parent, entries, sources, quoteState) {
    for (const quote of entries) {
      quoteState.supplied++;
      if (!object(quote) || typeof quote.text !== 'string' || !quote.text.trim() || !quoteVerified(quote)) continue;
      const quoteSha = sourceSha(quote), id = first(quote, ['source_id', 'document_id']);
      const candidates = sources.filter(source => quoteSha && sourceSha(source) === quoteSha && (id === undefined || id === null || sourceId(source) === id));
      const seenSources = new Map(candidates.map(source => [sourceKey(source), source])); if (seenSources.size !== 1) continue;
      const source = [...seenSources.values()][0], edition = sourceEdition(source), quoteEdition = sourceEdition(quote), title = first(source, ['title', 'name']);
      if (!edition || (quoteEdition !== null && quoteEdition !== edition) || typeof title !== 'string' || !title.trim() || !pages(quote).length) continue;
      const words = quote.text.trim().split(/\s+/u).length;
      const identity = 'paper-group:' + quoteState.groups.get(source), duplicate = identity + '|' + quote.text.trim().replace(/\s+/gu, ' ');
      if (quoteState.seen.has(duplicate)) continue;
      if (words > 25 || (quoteState.budget.get(identity) || 0) + words > 25) continue;
      if (safeString(quote.text) !== quote.text) continue;
      quoteState.seen.add(duplicate); quoteState.budget.set(identity, (quoteState.budget.get(identity) || 0) + words); quoteState.displayed++;
      const block = node('blockquote', 'iss-quote', null, parent); node('p', '', quote.text + (quote.is_fragment === true || quote.isFragment === true ? ' [Excerpt]' : ''), block);
      node('cite', 'iss-quote-source', safeString(title) + ' · ' + safeString(edition) + ' · physical PDF p' + pages(quote).join(', ') + (typeof quote.locator === 'string' ? ' · ' + safeString(quote.locator) : ''), block);
    }
  }
  function render(value, payload) {
    if (!object(payload)) return clear(value, 'ISS fire context is pending or unavailable. No earlier statements are retained.');
    if (payload.schema_version !== SCHEMA) return clear(value, 'ISS fire context is unavailable: the supplied envelope does not match iss-fire-context-v1.');
    if (payload.error || ['error', 'unavailable', 'failed'].includes(payload.status)) return clear(value, 'ISS fire context is unavailable for this response. No earlier statements are retained.');
    const root = base(value), issues = [];
    node('p', 'iss-attribution-note', 'Attribution labels reflect the supplied statements. Summaries are not presented as verbatim quotations or compliance certification.', root);
    if (typeof payload.summary === 'string' && payload.summary.trim()) node('p', 'iss-summary', safeString(payload.summary), root);
    if (own(payload, 'status')) node('p', 'iss-status', 'Supplied status: ' + text(payload.status), root);
    const documents = sourceObjects(payload.documents), byId = new Map();
    documents.forEach(source => { const id = sourceId(source); if (id && !byId.has(id)) byId.set(id, source); else if (id) issues.push('Duplicate source ID supplied; no title-based resolution was attempted.'); });
    const allSources = [...documents];
    for (const key of ['principles', 'classification_context']) for (const entry of array(payload[key])) if (object(entry)) allSources.push(...associatedSources(entry, documents, byId).sources);
    const quoteState = { supplied: 0, displayed: 0, budget: new Map(), seen: new Set(), groups: paperGroups(allSources) }; let itemCount = 0;
    for (const [key, title] of [['principles', 'Source-linked principles'], ['classification_context', 'Classification context']]) {
      const section = node('section', 'iss-statement-group', null, root); node('h3', 'iss-group-heading', title, section);
      if (!Array.isArray(payload[key]) || !payload[key].length) { node('p', 'iss-pending', 'No ' + title.toLowerCase() + ' statements are supplied in this response.', section); if (payload[key] != null && !Array.isArray(payload[key])) { issues.push(key + ' is not an array.'); showFields(section, 'Unstructured supplied field · attribution pending', payload[key], 'iss-unstructured'); } continue; }
      for (const entry of payload[key]) {
        const item = object(entry) ? entry : { text: entry }; itemCount++;
        const card = node('article', 'iss-item', null, section); if (typeof item.id === 'string') card.dataset.issItemId = item.id;
        const kind = first(item, ['kind', 'type']), label = typeof kind === 'string' && own(KINDS, kind) ? KINDS[kind] : 'Attribution pending';
        node('p', 'iss-kind', label, card);
        if (label === 'Attribution pending' && kind !== undefined) node('p', 'iss-raw-kind', 'Supplied attribution: ' + text(kind), card);
        const heading = first(item, ['title', 'label']); if (typeof heading === 'string' && heading.trim()) node('h4', 'iss-item-title', safeString(heading), card);
        const content = first(item, ['text', 'statement', 'summary', 'description']);
        if (typeof content === 'string' && content.trim()) {
          if (content.length > 350) { const details = node('details', 'iss-details iss-long-summary', null, card); node('summary', '', 'Read supplied summary', details); node('p', 'iss-item-text', safeString(content), details); }
          else node('p', 'iss-item-text', safeString(content), card);
        } else { node('p', 'iss-pending', 'Statement text is not supplied as a string.', card); if (content !== undefined && content !== null) showFields(card, 'Unstructured supplied content · uninterpreted', content, 'iss-unstructured'); }
        showFields(card, 'Conditions / applicability supplied', item.conditions, 'iss-conditions'); showFields(card, 'Limits supplied', item.limits, 'iss-limits');
        const bound = associatedSources(item, documents, byId); bound.sources.forEach(source => sourceCard(card, source));
        if (!bound.sources.length) node('p', 'iss-source-missing', 'A statement-specific source binding has not been supplied.', card);
        if (bound.unresolved.length) showFields(card, 'Unresolved source references', bound.unresolved, 'iss-source-missing');
        quotes(card, array(first(item, ['source_sentence', 'source_sentences'])), bound.sources, quoteState);
        additional(card, item, new Set(['id', 'title', 'label', 'kind', 'type', 'text', 'statement', 'summary', 'description', 'conditions', 'limits', 'source', 'sources', 'source_id', 'source_ids', 'document_id', 'document_ids']));
      }
    }
    const references = node('details', 'iss-documents iss-details', null, root); node('summary', '', 'Source documents supplied (' + documents.length + ')', references);
    if (!documents.length) node('p', 'iss-pending', 'Source documents are not supplied in this response.', references);
    documents.forEach(source => { sourceCard(references, source); quotes(references, array(first(source, ['source_sentence', 'source_sentences'])), [source], quoteState); });
    showFields(root, 'Panel limits supplied', payload.limits, 'iss-panel-limits'); showFields(root, 'Warnings supplied', payload.warnings, 'iss-warnings');
    if (quoteState.supplied > quoteState.displayed) node('p', 'iss-quote-status', 'Unverified, ambiguous, repeated or over-budget source sentences are withheld. No summary is substituted as a quotation.', root);
    if (issues.length) showFields(root, 'Supplied-data format notes', issues, 'iss-warnings');
    additional(root, payload, new Set(['schema_version', 'summary', 'status', 'documents', 'principles', 'classification_context', 'limits', 'warnings']));
    if (!itemCount) { const message = node('p', 'iss-status iss-pending', 'No ISS fire-context statements are available in this response. No controlled/uncontrolled definition is inferred.', root); message.setAttribute('role', 'status'); message.setAttribute('aria-live', 'polite'); }
    return { status: itemCount ? 'rendered' : 'pending', items: itemCount, documents: documents.length, displayedSentences: quoteState.displayed, withheldSentences: quoteState.supplied - quoteState.displayed, issues };
  }
  global.FlameSafetyISS = Object.freeze({ render, clear });
})(typeof window !== 'undefined' ? window : globalThis);
