# Claude Code adapter

Istruzioni per Claude Code quando usa questa repo.

Pipeline ufficiale:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

1. Leggi `AGENTS.md` e applica le regole root.
2. Usa come source of truth `README.md`, `docs/02-methodology.md`, `docs/04-prompt-construction-protocol.md`, `docs/13-blueprint-compiler.md`, `docs/14-vertical-blueprint-contracts.md`, `blueprints/` e `scorecards/`.
3. Per ogni richiesta, rileva la modalità: `simple-task`, `feature`, `full-project`, `multi-agent`.
4. Per progetti completi, genera prima `spec.md`, `blueprint.md`, `plan.md`, `tasks.md` e scorecard attesa.
5. Per modifiche piccole, usa `blueprints/12-targeted-change-blueprint.md` e produci patch minima.
6. Non assumere silenziosamente decisioni che cambiano architettura, sicurezza, dati, privacy o scope.
7. Non produrre codice sovra-commentato o astrazioni speculative.
8. Restituisci test, limiti, rischi residui e scorecard.
9. Aggiorna spec e blueprint se l’implementazione cambia direzione.
