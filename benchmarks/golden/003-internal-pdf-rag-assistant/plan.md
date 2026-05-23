# Plan: internal PDF RAG assistant

## Slice 1: corpus and ingestion

Define approved PDF corpus inventory, extraction flow, metadata model, and re-ingestion triggers.

## Slice 2: chunking and indexing

Define chunking strategy, embedding path, vector index, and access-filter metadata.

## Slice 3: retrieval and answer policy

Implement retrieval, citation formatting, hallucination boundaries, refusal behavior, and unsupported-question handling.

## Slice 4: freshness and governance

Implement document versioning, stale-index handling, access-control rules, and privacy constraints.

## Slice 5: evaluation and audit

Create the evaluation set, expected evidence rules, scorecard checks, and failure-mode review.

## Stack rationale

Use grounded internal document retrieval and document-bound answer generation; reject generic chat defaults and internet fallback because the fixture requires evidence-backed answers from internal PDFs only.
