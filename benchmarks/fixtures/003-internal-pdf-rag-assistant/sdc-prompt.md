# Specification-Driven Coding prompt fixture: internal PDF RAG assistant

Create an internal document question-answering assistant for employees who need grounded answers from approved company PDFs such as policy manuals, SOPs, onboarding guides, and compliance documents.

## Mode

`full-project` for an app-builder or coding-agent run.

## Project profile

Primary: `rag-knowledge-assistant`

Secondary: `internal-tooling-workbench` only if access control, ingestion operations, or admin workflows require a broader internal operations surface.

## Domain and user

The primary user is an authenticated internal employee asking questions about approved PDF documents. The system must behave like a controlled internal knowledge assistant, not a generic public chatbot.

## Non-goals

- No open-ended general chatbot persona.
- No answers based on world knowledge when the corpus does not support them.
- No public document upload by anonymous users.
- No indexing of sensitive PDFs without explicit policy and access controls.
- No silent answer synthesis without citations.

## Stack constraints

Use a RAG architecture with explicit ingestion, chunking, embeddings, vector index, retrieval, and answer-grounding rules. Do not pick a default chat stack without declaring corpus boundaries, retrieval strategy, and evaluation. Do not use internet search or external browsing as fallback.

## Knowledge and answer contract

The corpus is internal PDFs only. Responses must cite supporting document title plus section, page, or chunk reference. If the answer is unsupported, ambiguous, outdated, or outside the approved corpus, the system must refuse or say it does not know.

## Security and privacy

Treat the corpus as sensitive internal documentation. Enforce access control by document class or audience where needed. Do not leak sensitive text across roles. Store only the minimum metadata needed for ingestion, retrieval, audit, freshness, and versioning.

## Freshness and lifecycle

The system must define document versioning, re-ingestion behavior, stale index handling, and how superseded PDFs affect answers and citations.

## Acceptance criteria

- Internal PDFs can be ingested into a declared chunking and embedding pipeline.
- Retrieval uses a declared vector index or equivalent semantic retrieval store with rationale.
- Every supported answer includes citations to internal documents.
- Unsupported or out-of-scope questions are refused explicitly.
- Access control and privacy handling for sensitive documents are documented.
- Freshness, versioning, and stale-document behavior are defined.
- Output includes an evaluation set and a scorecard covering groundedness, citation accuracy, refusal behavior, privacy, and anti-genericity.
