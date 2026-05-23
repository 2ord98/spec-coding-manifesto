# Sito marketing, portfolio o CMS leggero

- Profile id: `marketing-site-cms`
- Quando usarlo: Landing page, sito pubblico, portfolio, knowledge base, blog, documentazione o mini-sito prodotto.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Qual è il pubblico primario e quale azione deve compiere?
- Quale prova rende credibile la promessa?
- Il sito è statico, editoriale o richiede back-office?
- Quale identità visiva va evitata perché troppo generica?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Astro + Markdown/MDX + Tailwind per static-first
- SvelteKit o Nuxt per contenuti dinamici
- Next.js App Router se serve ecosistema React maturo
- Headless CMS: Sanity, Strapi, Directus o solo Git/MDX

## Must-have spec fields

- Information architecture esplicita
- SEO tecnico e contenuti canonici
- Accessibilità WCAG AA
- Performance budget e Core Web Vitals
- Design system minimale ma distintivo

## Anti-pattern da evitare

Non generare la solita landing SaaS con hero generico, card identiche e gradienti casuali. Prima definisci pubblico, promessa, tono, proof e funnel.

## Acceptance gates

- Ogni pagina ha scopo e CTA espliciti
- Il layout non usa componenti placeholder generici
- Il contenuto above-the-fold è specifico del dominio
- Lighthouse target: performance/accessibility/SEO >= 90 salvo vincoli motivati

## Prompt seed

```text
Stai costruendo un progetto di tipo `marketing-site-cms`.
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

`blueprints/01-ai-builder-master-blueprint.md` per app builder o `blueprints/02-full-project-blueprint.md` per codice completo. Per WordPress custom usare `blueprints/04-wordpress-custom-theme-blueprint.md`.

Il blueprint deve includere file/output contract, security/privacy frame, anti-genericity constraints e scorecard target.
