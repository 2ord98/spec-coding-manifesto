# Compile user request to Specification-Driven Coding blueprint

Usa questa repo come sorgente di verità.

Compito: trasformare la richiesta utente in un blueprint operativo per coding agent o app builder.

Use this repository as the source of truth.

Task: transform the user request into an operational blueprint for a coding agent or app builder.

## Regole

- Non trattare il messaggio utente come prompt finale.
- Non generare codice prima del blueprint.
- Se mancano dati bloccanti, fai massimo 5 domande.
- Se mancano dati non bloccanti, dichiara assunzioni provvisorie.
- Usa un project profile da `project-types/`.
- Usa un blueprint da `blueprints/`.
- Includi scorecard target.

## Rules in English

- Do not treat the user message as the final prompt.
- Do not generate code before the blueprint.
- If blocking data is missing, ask at most 5 questions.
- If non-blocking data is missing, declare provisional assumptions.
- Use a project profile from `project-types/`.
- Use a blueprint from `blueprints/`.
- Include a target scorecard.

## Output

```markdown
# Specification-Driven Coding Blueprint

## Intento normalizzato

## Modalità

## Project profile

## Domande bloccanti

## Assunzioni provvisorie

## Non-obiettivi

## Anti-genericity constraints

## Blueprint scelto

## Builder-ready prompt

## Acceptance criteria

## Scorecard target
```

English equivalent: normalized intent, mode, project profile, blocking questions, provisional assumptions, non-goals, anti-genericity constraints, selected blueprint, builder-ready prompt, acceptance criteria, target scorecard.
