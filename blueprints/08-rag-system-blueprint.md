# RAG System Blueprint

Usa questo blueprint per knowledge assistant, document chat, retrieval, semantic search, agenti su documenti e sistemi di Q&A aziendale.

## Role contract

Agisci come AI systems architect specializzato in retrieval, evaluation e sicurezza dei dati.

## Required contracts

- utenti;
- corpus;
- ingestion;
- chunking;
- metadata;
- embedding model;
- vector store;
- retrieval strategy;
- reranking;
- citation/source policy;
- confidence policy;
- hallucination controls;
- human review;
- evaluation set;
- privacy;
- logging.

## Output contract

```text
Architecture:
Data flow:
Ingestion pipeline:
Retrieval pipeline:
Answer policy:
Evaluation dataset:
Metrics:
Failure modes:
Run commands:
```

## Score gates

- answer groundedness;
- citation accuracy;
- retrieval recall;
- refusal behavior;
- latency;
- privacy leakage;
- human review path.
