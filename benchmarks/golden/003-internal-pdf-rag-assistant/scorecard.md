# Scorecard: internal PDF RAG assistant

| Area | Score | Evidence |
|---|---:|---|
| Spec adherence | 92 | Covers ingestion, chunking, embeddings, retrieval, citations, refusals, access control, freshness, and evaluation. |
| Anti-genericity | 93 | Rejects generic chatbot defaults and internet fallback; constrains the system to approved internal PDFs. |
| Domain fit | 90 | Models an internal document assistant rather than a public chat product. |
| Architecture | 90 | Grounded RAG pipeline matches the corpus and answer contract. |
| Security/privacy | 92 | Sensitive-document handling, access tags, minimum logging, and leakage prevention are explicit. |
| Groundedness/citations | 94 | Supported answers require document citations and unsupported answers must refuse. |
| Testability/eval | 90 | Evaluation set with expected evidence and refusal cases is required. |
| Risks | 78 | OCR quality, stale indexes, and access-tag errors remain residual risks. |
| Next fixes | 82 | Add retrieval metrics thresholds and document-version audit tooling after the first grounded baseline. |

## Result

Gate: PASS for benchmark fixture.
