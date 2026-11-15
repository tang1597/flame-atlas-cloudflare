"""Execute an explicit question plan against real, scene-eligible sources.

AI can choose retrieval questions and evidence IDs, never invent papers. Query
fusion is deterministic and independent of safety or numerical model scores.
"""
from copy import deepcopy


def retrieve_plan(bridge, query, search_queries, allowed_study_ids):
    queries = [query]
    if isinstance(search_queries, list):
        queries += [q.strip() for q in search_queries if isinstance(q, str) and 0 < len(q.strip()) <= 1000]
    queries = list(dict.fromkeys(queries))[:5]
    if len(queries) == 1:
        result = bridge.rank_documents(query, allowed_study_ids=allowed_study_ids, limit=100)
        return {**result, 'search_queries': queries, 'plan_executed': False}
    records, scores, first, hits = {}, {}, {}, {}
    for index, terms in enumerate(queries):
        ranked = bridge.rank_documents(terms, allowed_study_ids=allowed_study_ids, limit=100)
        for rank, row in enumerate(ranked.get('documents', []), 1):
            identifier = row['id']
            if identifier not in records:
                records[identifier] = deepcopy(row)
                first[identifier] = len(first)
                scores[identifier] = 0.0
                hits[identifier] = []
            scores[identifier] += (2.0 if index == 0 else 1.0) / (60 + rank)
            hits[identifier].append(index)
    ordered = sorted(records, key=lambda i: (-scores[i], first[i]))[:100]
    rows = []
    for rank, identifier in enumerate(ordered, 1):
        row = records[identifier]
        row.update(rank=rank, score=scores[identifier], plan_query_indices=hits[identifier])
        rows.append(row)
    return {'documents': rows, 'query': query, 'search_queries': queries,
            'search_mode': 'question_plan_source_retrieval', 'plan_executed': True,
            'ranking_method': 'Reciprocal-rank fusion of the interpreted question and explicit AI search plan; original question receives double weight. Scene study limits remain unchanged.',
            'training_performed': False, 'live_generation': False}


def order_sources(documents, preferred_ids, *, limit=12):
    """Promote only real candidate IDs; preserve remaining candidate order."""
    by_id = {d['id']: d for d in documents}
    ordered_ids = list(dict.fromkeys(i for i in preferred_ids if isinstance(i, str) and i in by_id))
    ordered_ids += [d['id'] for d in documents if d['id'] not in ordered_ids]
    result = [deepcopy(by_id[i]) for i in ordered_ids[:limit]]
    for rank, row in enumerate(result, 1):
        row['rank'] = rank
    return result
