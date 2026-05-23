# Toolkit Adapter

Specification-Driven Coding può funzionare come adapter concettuale per workflow specification-first esistenti.

Specification-Driven Coding can operate as a conceptual adapter for existing specification-first workflows.

## Sequenza

1. `specify init <project>`
2. Copia `AGENTS.md` nella root.
3. Copia `.specify/memory/constitution.md` o integra i suoi articoli.
4. Copia `.specify/templates/overrides/`.
5. Prima del comando di specification, usa `prompts/select-project-profile.prompt.md`.
6. Prima del comando di plan, usa il profilo progetto scelto.
7. Prima del comando di implementazione, usa `prompts/audit-before-implementation.prompt.md`.

## Sequence

1. Initialize the target project workflow.
2. Copy `AGENTS.md` into the root.
3. Copy `.specify/memory/constitution.md` or integrate its articles.
4. Copy `.specify/templates/overrides/`.
5. Before the specification command, use `prompts/select-project-profile.prompt.md`.
6. Before the plan command, use the selected project profile.
7. Before implementation, use `prompts/audit-before-implementation.prompt.md`.

## Differenza rispetto al workflow generico

Il focus non è solo avere una spec, ma impedire che la spec resti generica.

The focus is not merely having a specification. The focus is preventing that specification from remaining generic.
