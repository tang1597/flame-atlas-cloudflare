import copy
import unittest
try:
    from .markdown_synthesis import select_notes, synthesize
except ImportError:
    from markdown_synthesis import select_notes, synthesize


DOCS = [{'id': 'paper-X', 'title': 'Synthetic PMMA test', 'doi': '10.9999/example',
         'study_ids': ['PSI-25'], 'abstract': 'Synthetic PMMA rods were tested with varying oxygen and flow.'}]
NOTES = [{'id': 'MD-synthetic', 'path': 'solid/PMMA.md', 'sha256': 'synthetic-digest', 'study_ids': ['PSI-25'],
          'text': 'Synthetic PMMA rods: oxygen delivery and heat loss jointly determine extinction. This is not an ignition threshold.'}]


def answer():
    return {'related': True,
        'environment': {'text': 'The relevant experiments varied oxygen and flow around PMMA rods.',
            'citation_ids': ['paper-X'], 'evidence_spans': [{'citation_id': 'paper-X', 'text': DOCS[0]['abstract']}]},
        'answer': {'text': 'The material response reflects oxygen delivery and heat loss together; the evidence does not establish an ignition threshold.',
            'citation_ids': ['MD-synthetic'], 'evidence_spans': [{'citation_id': 'MD-synthetic', 'text': NOTES[0]['text']}]},
        'preferred_document_ids': ['paper-X']}


class Service:
    def __init__(self, candidate): self.candidate = candidate; self.payload = None
    def _call(self, prompt, payload, *args): self.payload = payload; return self.candidate
    def status(self): return {'provider': 'openai_responses', 'model': 'gpt-6.1-sol'}


class MarkdownSummaryTests(unittest.TestCase):
    def test_openai_service_routes_summary_through_markdown_generation(self):
        try:
            from .ai_service import AIConfig, AIService
        except ImportError:
            from ai_service import AIConfig, AIService
        payloads = []
        def transport(request):
            payloads.append(request)
            return answer()
        service = AIService(AIConfig(base_url='https://api.openai.com/v1', model='gpt-6.1-sol',
            api_key='synthetic-key', provider='openai_responses'), transport=transport)
        result = service.summarize('PMMA extinction', DOCS, dataset_notes=NOTES)
        self.assertEqual(result['method'], 'openai_markdown_synthesis')
        self.assertIn('curated_dataset_markdown', str(payloads[0]))
        system_prompt = payloads[0]['messages'][0]['content']
        for instruction in ['2-3 concise English sentences total', 'at most 65 words across',
                            'at most 20 words', 'at most 45 words', 'give the direct answer first',
                            'Omit generic source cautions', 'operational safety certification',
                            'sorry this is not related']:
            self.assertIn(instruction, system_prompt)

    def test_notes_follow_matched_investigations_not_generic_word_overlap(self):
        wrong = {**NOTES[0], 'id': 'wrong', 'study_ids': ['PSI-69'], 'text': 'PMMA oxygen flow'}
        self.assertEqual([n['id'] for n in select_notes('PMMA oxygen', DOCS, [wrong, *NOTES])], ['MD-synthetic'])

    def test_markdown_reaches_api_and_generated_prose_retains_distinct_citations(self):
        service = Service(answer())
        result = synthesize(service, 'PMMA extinction', DOCS, NOTES)
        self.assertIn(NOTES[0]['text'], str(service.payload))
        self.assertEqual(result['method'], 'openai_markdown_synthesis')
        self.assertTrue(result['generated'])
        self.assertEqual(result['source_ids'], ['paper-X'])
        self.assertEqual(result['markdown_sources'][0]['path'], 'solid/PMMA.md')
        self.assertFalse(result['checks']['scientific_entailment_verified'])

    def test_invented_source_or_quote_is_rejected(self):
        for change in ['source', 'quote']:
            candidate = answer()
            if change == 'source': candidate['answer']['citation_ids'] = ['made-up']
            else: candidate['answer']['evidence_spans'][0]['text'] = 'This sentence does not exist in the source.'
            with self.subTest(change=change), self.assertRaises(ValueError):
                synthesize(Service(candidate), 'PMMA extinction', DOCS, NOTES)

    def test_new_numeric_threshold_and_safety_certification_are_rejected(self):
        for text in ['PMMA is safe.', 'The threshold is 99 kPa.']:
            candidate = answer(); candidate['answer']['text'] = text
            with self.subTest(text=text), self.assertRaises(ValueError):
                synthesize(Service(candidate), 'PMMA extinction', DOCS, NOTES)

    def test_supplying_markdown_but_ignoring_it_is_not_accepted(self):
        candidate = answer(); candidate['answer'] = copy.deepcopy(candidate['environment'])
        with self.assertRaisesRegex(ValueError, 'markdown_not_used'):
            synthesize(Service(candidate), 'PMMA extinction', DOCS, NOTES)


if __name__ == '__main__': unittest.main()
