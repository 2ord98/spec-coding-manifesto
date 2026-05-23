# Workflow automation, RPA e integrazioni

- Profile id: `workflow-automation-rpa`
- Quando usarlo: Automazioni tra tool, CRM, email, fogli, calendari, ticket, scraping consentito, ETL leggero, task ripetitivi.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quale evento avvia il workflow?
- Quali step possono fallire e come si recupera?
- Quali azioni richiedono approvazione?
- Quali dati attraversano sistemi terzi?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- n8n/Zapier/Make per workflow no/low-code
- Temporal/Prefect/Dagster per workflow software robusti
- Python/FastAPI worker
- Webhooks + queues + retries
- MCP tools per agenti

## Must-have spec fields

- Trigger map
- Step contracts
- Retries/timeouts
- Idempotency keys
- Secret handling
- Manual override
- Run history

## Anti-pattern da evitare

Non collegare tool senza specificare trigger, idempotenza, retry, autorizzazioni e rollback.

## Acceptance gates

- Ogni step ha input/output definiti
- Retry non duplica effetti
- Segreti non sono hardcoded
- Run log ispezionabile

## Prompt seed

```text
Stai costruendo un progetto di tipo `workflow-automation-rpa`.
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
