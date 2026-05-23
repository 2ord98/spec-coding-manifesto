# Backend API, microservizi e sistemi server

- Profile id: `backend-api-microservices`
- Quando usarlo: API REST/GraphQL/gRPC, servizi backend, job worker, webhook handler, sistemi multi-servizio.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali sono i confini del servizio?
- Quali endpoint sono pubblici, privati o interni?
- Quali operazioni devono essere idempotenti?
- Quali SLA o limiti di carico valgono?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- FastAPI + SQLAlchemy + Postgres
- ASP.NET Core Minimal APIs + EF Core + SQL Server/Postgres
- NestJS + Prisma/TypeORM
- Go + Chi/Fiber + sqlc
- Message broker: RabbitMQ, Kafka, NATS se giustificato

## Must-have spec fields

- OpenAPI/contratti
- Idempotenza per webhook e comandi
- Observability minima
- Rate limit e auth
- Migrazioni DB
- Health checks

## Anti-pattern da evitare

Non introdurre microservizi senza bisogno. Prima definisci boundary, contratti, carico, failure mode e ownership.

## Acceptance gates

- OpenAPI aggiornata e coerente
- Error model standardizzato
- Test di contratto per endpoint critici
- Nessun servizio/broker aggiunto senza rationale

## Prompt seed

```text
Stai costruendo un progetto di tipo `backend-api-microservices`.
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
