# RAG knowledge assistant / chat sui documenti

- Profile id: `rag-knowledge-assistant`
- Quando usarlo: Assistenti su documenti, knowledge base aziendali, manuali, corpus tecnici, supporto interno, ricerca semantica.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali fonti sono autorevoli e quali escluse?
- Quali domande devono ricevere “non so”?
- Serve risposta con citazioni obbligatorie?
- Quali metriche validano il retrieval?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- LlamaIndex/LangChain/Haystack secondo ecosistema
- Vector DB: pgvector, Qdrant, Weaviate, Milvus
- Reranking: cross-encoder o API dedicata se necessario
- UI: Next/SvelteKit/Streamlit per prototipi
- Eval: golden dataset + retrieval metrics

## Must-have spec fields

- Corpus inventory
- Chunking strategy
- Retrieval pipeline
- Citation policy
- Hallucination boundaries
- Evaluation set
- Privacy/data retention

## Anti-pattern da evitare

Non chiamare RAG una chat con embedding. Specifica corpus, chunking, retrieval, citazioni, limiti e valutazione.

## Acceptance gates

- Ogni risposta supportata cita fonti
- Query out-of-scope rifiutate correttamente
- Golden set con expected evidence
- Nessun dato sensibile indicizzato senza policy

## Prompt seed

```text
Stai costruendo un progetto di tipo `rag-knowledge-assistant`.
Prima di proporre stack o codice, completa intake, vincoli, non-obiettivi e anti-genericity constraints.
Poi scrivi spec, blueprint, plan e task usando i template Specification-Driven Coding.
Se una scelta tecnica è implicita, fermati e dichiarala come assunzione o domanda bloccante.
```

## Output minimo richiesto all’agente

- Spec con requisiti funzionali e non funzionali.
- Piano tecnico con stack motivato e alternativa scartata.
- Task atomici ordinati per dipendenza.
- Acceptance matrix.
- Audit anti-genericità.

## Blueprint consigliato

`blueprints/02-full-project-blueprint.md`; se usato con app builder, prima compilare `blueprints/01-ai-builder-master-blueprint.md`.

Il blueprint deve includere file/output contract, security/privacy frame, anti-genericity constraints e scorecard target.
