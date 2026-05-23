# Vertical Blueprint: internal PDF RAG assistant

## Role contract

Act as an AI systems builder implementing only the specified internal PDF RAG assistant. Do not silently add public-chat defaults, internet search, or unsupported answer behavior.

## Product/domain intent

A controlled internal knowledge assistant that answers employee questions from approved company PDFs with citations, refusals, and document-aware access boundaries.

## Project profile

`rag-knowledge-assistant`

## Stack contract

Use a RAG stack with explicit ingestion, chunking, embeddings, semantic retrieval, citation enforcement, and evaluation. The stack rationale is `grounded internal document retrieval`: it satisfies the fixture because the corpus is internal PDFs and every supported answer must be traceable to source evidence.

Rejected default: generic chat assistant without retrieval contract. Reason: generic chatbot defaults were rejected because the fixture requires corpus boundaries, citations, refusal behavior, privacy controls, and evaluation evidence.

Rejected default: internet or public-search fallback. Reason: the assistant is restricted to approved internal PDFs.

## Architecture contract

- Corpus: approved internal PDFs only, with document inventory and classification.
- Ingestion: PDF extraction, metadata capture, version identifier, access tags, and re-ingestion path.
- Chunking: explicit chunk size and overlap chosen for policy and SOP paragraphs rather than arbitrary defaults.
- Retrieval: embeddings plus vector index with optional metadata filtering for access control.
- Answering: retrieve evidence first, then answer only from supported chunks with citations.
- Refusal path: respond with uncertainty or refusal when evidence is absent, stale, conflicting, or restricted.
- Freshness: superseded PDFs trigger re-indexing and older versions must not be cited as current unless explicitly requested.
- Evaluation: golden set with expected answer behavior and expected evidence.

## UX contract

Avoid generic chatbot framing. The interface and answer format must emphasize approved documents, evidence-backed answers, refusal when unsupported, and visible source references.

## Security/privacy contract

Internal PDFs are sensitive. Enforce access control by document class or audience, prevent leakage across roles, minimize stored metadata, and log only what is required for audit and troubleshooting.

## Quality gates

- Groundedness gate passes.
- Citation accuracy gate passes.
- Refusal behavior gate passes.
- Privacy and access-control gate passes.
- Freshness/versioning gate passes.
- Evaluation-set gate passes.
- Anti-genericity gate passes.
