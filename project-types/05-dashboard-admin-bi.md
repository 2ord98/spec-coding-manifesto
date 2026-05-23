# Dashboard, admin panel e BI operativa

- Profile id: `dashboard-admin-bi`
- Quando usarlo: Pannelli interni, controllo operativo, reporting, metriche, workflow admin, monitoraggio prodotto.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali decisioni deve supportare la dashboard?
- Quali metriche sono leading vs lagging?
- Chi può vedere/modificare cosa?
- Quanto devono essere freschi i dati?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- React + TanStack Table/Query + Recharts
- Vue + Pinia + ECharts
- SvelteKit + server actions
- Blazor + MudBlazor/Radzen per ambienti .NET
- Backend analytics: Postgres/ClickHouse/BigQuery secondo scala

## Must-have spec fields

- Metric definitions
- Filtri e permessi
- Drill-down e export
- Freshness dei dati
- Empty/error/loading state
- Audit per azioni admin

## Anti-pattern da evitare

Non creare dashboard decorative. Ogni grafico deve guidare una decisione o un’azione.

## Acceptance gates

- Ogni widget ha definizione metrica
- Nessun grafico senza decisione associata
- Export e filtri sono specificati
- Le query pesanti hanno strategia performance

## Prompt seed

```text
Stai costruendo un progetto di tipo `dashboard-admin-bi`.
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
