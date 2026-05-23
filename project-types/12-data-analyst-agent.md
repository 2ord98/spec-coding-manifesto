# AI data analyst, text-to-SQL e BI agentica

- Profile id: `data-analyst-agent`
- Quando usarlo: Agenti che interrogano database, producono report, generano SQL, analizzano dati, spiegano metriche.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali tabelle sono interrogabili?
- Quali metriche sono ufficiali?
- Quali dati sensibili vanno mascherati?
- Serve generare report ricorrenti?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Text-to-SQL con schema grounding
- DB read-only role
- DuckDB/Postgres/BigQuery/Snowflake
- Python notebooks/Streamlit per analisi
- Semantic layer: dbt metrics/Cube/LookML se disponibile

## Must-have spec fields

- Read-only credentials
- Schema catalog
- Metric definitions
- Query limits
- PII redaction
- Result explanation
- SQL trace

## Anti-pattern da evitare

Non dare all’agente accesso write al database. Non generare SQL senza schema, limiti, explain e guardrail.

## Acceptance gates

- SQL visibile e revisionabile
- Query cost/limit applicati
- Metriche usano definizioni approvate
- Il sistema segnala dati insufficienti

## Prompt seed

```text
Stai costruendo un progetto di tipo `data-analyst-agent`.
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
