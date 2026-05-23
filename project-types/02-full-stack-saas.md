# Full-stack SaaS / piattaforma web

- Profile id: `full-stack-saas`
- Quando usarlo: Applicazioni con utenti, auth, dati persistenti, dashboard, pagamenti, team, ruoli e workflow di business.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Chi paga, chi usa, chi amministra?
- Quali dati non possono mai diventare incoerenti?
- Quali azioni richiedono permessi o audit?
- Qual è il MVP reale, non la piattaforma completa?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Next.js/Remix + Postgres + Prisma/Drizzle
- SvelteKit + Supabase
- Vue/Nuxt + FastAPI o NestJS
- Blazor + ASP.NET Core + SQL Server/Postgres per ecosistema .NET

## Must-have spec fields

- RBAC/ABAC definito
- Modello dati con invarianti
- Audit log per azioni sensibili
- Migrazioni e seed realistici
- Test su flussi critici

## Anti-pattern da evitare

Non partire dal database o da componenti UI. Parti da attori, casi d’uso, regole dati, permessi e stato del dominio.

## Acceptance gates

- Auth e autorizzazione sono testate
- CRUD non è generico: riflette il dominio
- Il modello dati ha constraints espliciti
- Il piano include deploy, env vars e rollback

## Prompt seed

```text
Stai costruendo un progetto di tipo `full-stack-saas`.
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
