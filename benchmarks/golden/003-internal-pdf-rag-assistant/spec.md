# Specification: internal PDF RAG assistant

## Project profile

`rag-knowledge-assistant`

## User

Authenticated internal employee asking questions against approved company PDFs such as policies, SOPs, onboarding material, and compliance references.

## Problem

The user needs grounded answers from internal PDF documents with explicit citations, while unsupported or out-of-scope questions must be refused instead of answered from model prior knowledge.

The product must enforce `no silent answer synthesis without citations`, and it must `do not pick a default chat stack without declaring corpus boundaries, retrieval strategy, and evaluation`.

## Functional requirements

- Ingest approved internal PDFs into a declared processing pipeline.
- Extract text and metadata needed for retrieval, access control, freshness, and versioning.
- Chunk documents using an explicit strategy suitable for policy and procedural content.
- Generate embeddings and store them in a declared vector index or equivalent semantic retrieval store.
- Retrieve supporting evidence for user questions and include citations in every supported answer.
- Refuse when evidence is missing, conflicting, stale, restricted, or out of scope.
- Respect document-level or audience-level access controls for sensitive documents.
- Define document freshness, superseded-version handling, and re-ingestion behavior.
- Define an evaluation set with expected answers and expected evidence.

## Non-goals

- No generic conversational assistant persona.
- No web search fallback.
- No unsupported answer synthesis without corpus evidence.
- No indexing of sensitive documents without declared policy.

## Acceptance criteria

- `internal PDFs can be ingested into a declared chunking and embedding pipeline`.
- `retrieval uses a declared vector index or equivalent semantic retrieval store with rationale`.
- `every supported answer includes citations to internal documents`.
- `unsupported or out-of-scope questions are refused explicitly`.
- Access control and privacy handling are documented for sensitive documents.
- Freshness, versioning, and stale-document behavior are defined.
- Evaluation set and scorecard cover groundedness, citation accuracy, refusal behavior, privacy, and anti-genericity.
- The stack rationale explicitly states `RAG architecture with explicit ingestion, chunking, embeddings, vector index, retrieval, and answer-grounding rules`.
- The stack rationale explicitly states `internet search or external browsing fallback was rejected`.
