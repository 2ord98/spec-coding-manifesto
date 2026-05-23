# Feature Spec: RAG assistant per knowledge base tecnica

## Specification-Driven Coding header

- Project profile: `rag-knowledge-assistant`
- Utente primario: support engineer interno
- Problema specifico: rispondere a domande su runbook e incident postmortem con citazioni verificabili
- Non-obiettivi: niente modifica ticket, niente accesso write a sistemi di produzione
- Vincoli: ogni risposta deve citare documento e sezione

## Anti-genericity constraints

- Pattern da evitare: chatbot generico senza fonti
- Scelta distintiva: risposta sempre strutturata in “answer / evidence / uncertainty”
- Dati realistici: runbook, incident, FAQ interne
- Stack default esclusi: nessun vector DB scelto senza valutare corpus size

## Functional requirements

- FR-001: indicizzare documenti approvati.
- FR-002: rispondere solo con fonti recuperate.
- FR-003: dire “non so” se evidence insufficiente.
- FR-004: mostrare citazioni cliccabili.

## Acceptance criteria

- AC-001: 20 domande golden set con expected evidence.
- AC-002: out-of-scope rejection testato.
- AC-003: log query senza PII non necessaria.
