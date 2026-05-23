# Write vertical blueprint

Trasforma specification e project profile in un blueprint verticale pronto per il piano finale.

Transform the specification and project profile into a Vertical Blueprint ready for the final plan.

Pipeline ufficiale: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## Input richiesto

- richiesta utente normalizzata;
- project profile;
- spec;
- tool o app builder target;
- livello qualità.

English equivalent: normalized user request, project profile, specification, target tool or app builder, quality level.

## Output

Usa `blueprints/00-blueprint-contract.md` come struttura base e aggiungi dettagli specifici per dominio, stack e strumento.

Il blueprint deve venire prima di plan e tasks: un agente deve poterlo usare per decidere stack, file tree, confini, sicurezza, fallback, output contract e quality gates senza inventare decisioni importanti.

Use `blueprints/00-blueprint-contract.md` as the base structure and add domain-specific, stack-specific, and tool-specific details.

The blueprint must come before plan and tasks: an agent must be able to use it to decide stack, file tree, boundaries, security, fallback, output contract, and quality gates without inventing important decisions.
