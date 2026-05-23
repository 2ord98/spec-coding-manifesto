# Intake: internal PDF RAG assistant

## Mode

`full-project`

## Project profile

Primary: `rag-knowledge-assistant`

## Blocking questions

None for this fixture. Corpus boundaries, access tiers, and deployment topology are treated as reversible assumptions.

## Reversible assumptions

- The first version serves authenticated internal employees only.
- The authoritative corpus is approved internal PDFs only.
- Responses require citations and must refuse unsupported answers.
- Sensitive documents may require audience-based filtering during retrieval.

## Non-goals

- General-purpose chatbot behavior.
- Anonymous upload or anonymous querying.
- Unsupported answers based on model prior knowledge.
- Indexing sensitive PDFs without explicit policy.
- Internet fallback or external browsing fallback.

## Anti-genericity constraints

- Must behave like a controlled internal knowledge assistant, not a generic public chatbot.
- Must specify ingestion, chunking, embeddings, vector index, retrieval, citations, freshness, and refusal behavior.
- Must treat privacy, access control, and sensitive-document handling as first-class requirements rather than optional hardening.
