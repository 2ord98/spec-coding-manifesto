# Stack Selection Matrix

Specification-Driven Coding non impone uno stack. Impone che lo stack sia motivato.

## Frontend

| Caso | Stack tipico | Quando evitarlo |
|---|---|---|
| Landing/static | Astro, SvelteKit, Nuxt | Se serve app state complesso |
| SaaS complesso | Next.js, Remix, Nuxt, SvelteKit | Se è solo sito statico |
| Dashboard interna | React/Vue/Svelte/Blazor | Se i dati non sono definiti |
| .NET ecosystem | Blazor + ASP.NET Core | Se il team non usa .NET |
| Mobile | Expo, Flutter, SwiftUI, Jetpack Compose | Se è solo prototipo web |

## Backend

| Caso | Stack tipico |
|---|---|
| API rapida AI/Python | FastAPI |
| Enterprise .NET | ASP.NET Core |
| Node ecosystem | NestJS/Hono/Express |
| Performance/CLI | Go/Rust |
| Workflow robusti | Temporal/Prefect/Dagster |

## Database

| Caso | Scelta |
|---|---|
| SaaS generale | Postgres |
| Search/vector | pgvector, Qdrant, Weaviate |
| Analytics | ClickHouse, BigQuery, DuckDB |
| Mobile realtime MVP | Firebase/Supabase |
| Graph/ontology | Neo4j, TypeDB, RDF/GraphQL layer |

## Regola

Ogni scelta deve includere:

- perché è adatta;
- alternativa scartata;
- rischio;
- costo di cambio futuro.
