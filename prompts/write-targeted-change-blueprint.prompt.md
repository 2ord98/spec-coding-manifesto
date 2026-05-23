# Write targeted change blueprint

Usa questo prompt per bug fix, feature piccole o modifiche brownfield.

Use this prompt for bug fixes, small features, or brownfield changes.

## Regole

- Cambia solo ciò che serve.
- Non proporre refactor non richiesti.
- Non introdurre nuove dipendenze salvo necessità.
- Prima dichiara causa probabile e file coinvolti.
- Poi produci task minimo e verifica.

## Rules in English

- Change only what is required.
- Do not propose unrequested refactors.
- Do not introduce new dependencies unless necessary.
- First declare probable cause and involved files.
- Then produce the minimum task and validation.

## Output

```markdown
# Targeted Change Blueprint

## Obiettivo

## Causa probabile

## File da ispezionare

## File probabilmente da modificare

## Modifica minima proposta

## Regressioni da evitare

## Test/verifica

## Rollback

## Scorecard breve
```

English equivalent: goal, probable cause, files to inspect, files likely to change, proposed minimum change, regressions to avoid, test/validation, rollback, short scorecard.
