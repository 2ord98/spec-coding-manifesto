# Browser extension / web augmentation

- Profile id: `browser-extension`
- Quando usarlo: Estensioni Chrome/Firefox, content scripts, side panel, automazione browser, annotazioni, assistenti web.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Su quali siti lavora?
- Quali dati legge o modifica nel DOM?
- Quali permessi sono indispensabili?
- Serve sync tra dispositivi?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Manifest V3
- TypeScript + Vite/Plasmo/WXT
- React/Vue/Svelte per popup/sidebar
- Storage extension APIs
- Backend opzionale per sync/auth

## Must-have spec fields

- Permission model
- Content script scope
- Data exfiltration policy
- UX popup/sidebar
- Cross-browser constraints
- Update strategy

## Anti-pattern da evitare

Non richiedere permessi larghi per comodità. Ogni permission deve essere minimizzata e giustificata.

## Acceptance gates

- Permissions minime
- Content script isolato
- No dati inviati senza consenso
- Test su domini target

## Prompt seed

```text
Stai costruendo un progetto di tipo `browser-extension`.
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
