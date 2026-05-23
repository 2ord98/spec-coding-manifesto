# E-commerce, marketplace o booking platform

- Profile id: `ecommerce-marketplace`
- Quando usarlo: Cataloghi, checkout, pagamenti, prenotazioni, ordini, inventory, vendor, marketplace multi-tenant.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Cosa si vende e con quali varianti?
- Quali stati attraversa un ordine?
- Chi gestisce stock e fulfillment?
- Quali edge case di pagamento vanno gestiti?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Next.js/Remix + Stripe + Postgres
- Medusa/Commerce Layer/Shopify headless se serve commerce maturo
- Nuxt/SvelteKit per front-end differenziato
- Backend .NET/FastAPI/NestJS per logica custom

## Must-have spec fields

- Order lifecycle
- Payment state machine
- Inventory consistency
- Refund/cancel policy
- Tax/shipping assumptions
- Fraud/basic abuse controls

## Anti-pattern da evitare

Non generare shop generico. Specifica catalogo, regole prezzo, stock, tasse, fulfillment, resi e dispute.

## Acceptance gates

- Checkout testato end-to-end in sandbox
- Ordini e pagamenti hanno stati separati
- Inventory non va negativo salvo scelta esplicita
- Email/notifiche transazionali sono previste

## Prompt seed

```text
Stai costruendo un progetto di tipo `ecommerce-marketplace`.
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
