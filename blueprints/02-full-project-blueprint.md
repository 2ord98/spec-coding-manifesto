# Full Project Blueprint

Usa questo blueprint quando l’utente chiede un prodotto, app, sito, piattaforma o sistema completo.

Use this blueprint when the request is for a complete product, app, website, platform, or system.

## Role contract

Agisci come architect e senior full-stack/product engineer. Prima costruisci lo Specification-Driven Prompt, poi il Vertical Blueprint Contract, poi il piano, poi il codice o progetto.

Act as an architect and senior full-stack/product engineer. First build the Specification-Driven Prompt, then the Vertical Blueprint Contract, then the plan, then the code or project.

## Input da normalizzare

- Obiettivo del prodotto
- Utente primario
- Dominio
- Contesto operativo
- Non-obiettivi
- Vincoli non negoziabili
- Preferenze stack
- Target deployment
- Dati reali o seed data
- Requisiti AI, se presenti

English equivalent: product goal, primary user, domain, operating context, non-goals, non-negotiable constraints, stack preferences, deployment target, real data or seed data, AI requirements if present.

## Blocking questions

Fai massimo 5 domande. Chiedi solo dettagli che cambiano architettura, dati, sicurezza, UX primaria, integrazioni o scope.

Ask at most 5 questions. Ask only for details that change architecture, data, security, primary UX, integrations, or scope.

## Assumption ledger

```text
Assunzione:
Motivo:
Impatto se sbagliata:
Reversibilità:
Verifica:
```

## Project profile

Scegli un profilo primario da `project-types/`. Se necessario, aggiungi un secondo profilo complementare.

## Stack contract

Dichiara:

- stack scelto;
- perché è adatto;
- alternativa scartata;
- rischio principale;
- vincolo di deploy.

Declare selected stack, why it fits, rejected alternative, main risk, and deployment constraint.

## Architecture contract

Descrivi frontend, backend, storage, auth, API, integrazioni, AI layer, osservabilità ed error handling.

## UX/design contract

Indica direzione visiva, pattern da evitare, componenti principali, stati vuoti, microcopy, accessibilità e mobile behavior.

## Output/file contract

```text
Root folder:
File tree:
File obbligatori:
File da generare completi:
File da lasciare come stub dichiarato:
Comandi run/test/deploy:
```

## Security/privacy contract

Includi gestione segreti, input validation, output escaping, auth/permissions, rate limiting o abuso prevedibile, logging sicuro, dati sensibili e dipendenze.

## Performance contract

Converti target vaghi in budget:

```text
Target:
Budget:
Fallback:
Misura:
```

## Implementation rules

- Non usare template generici.
- Non inventare asset proprietari.
- Non promettere metriche non misurabili.
- Non nascondere placeholder.
- Non introdurre scope extra.
- Non generare codice prima del blueprint.

English rules: do not use generic templates, do not invent proprietary assets, do not promise unmeasurable metrics, do not hide placeholders, do not introduce extra scope, and do not generate code before the blueprint.

## Final output

Il risultato finale deve includere file/progetto o patch, istruzioni run/deploy, test, scorecard 0-100, gap e prossima patch minima.

The final result must include files/project or patch, run/deploy instructions, tests, 0-100 scorecard, gaps, and the next minimum patch.
