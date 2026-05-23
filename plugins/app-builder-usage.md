# Uso con AI app builder: Emergent, Manus, Lovable, Bolt, v0, Replit, Base44-style builder e simili

Questi tool sono potenti ma tendono a riempire i vuoti con default medi. Usa Specification-Driven Coding come pre-prompt e come sistema di compilazione della richiesta.

These tools are powerful, but they tend to fill missing information with average defaults. Use Specification-Driven Coding as a pre-prompt and request-compilation system.

## Regola principale

Non chiedere al builder di “fare l’app”. Chiedigli prima di trasformare la richiesta in un **builder-ready blueprint**.

## Main rule

Do not ask the builder to “make the app” directly. First ask it to transform the request into a **builder-ready blueprint**.

## Prompt da incollare prima della richiesta

```text
Prima di generare l’app, lavora in modalità Specification-Driven Coding.
Non trattare il mio messaggio come prompt finale.
Compila la richiesta in un builder-ready blueprint usando questa struttura:
1. role frame;
2. product frame;
3. domain frame;
4. architecture frame;
5. data frame;
6. security/privacy frame;
7. UX/motion frame, se applicabile;
8. file/output contract;
9. execution contract;
10. scorecard.

Se il mio prompt è troppo vago, fammi massimo 5 domande bloccanti.
Se puoi procedere con assunzioni sicure, dichiarale e continua.
Non usare template generici, seed data generici, layout generici o stack default se il dominio richiede scelte più specifiche.
```

## English pre-prompt

```text
Before generating the app, work in Specification-Driven Coding mode.
Do not treat my message as the final prompt.
Compile the request into a builder-ready blueprint using this structure:
1. role frame;
2. product frame;
3. domain frame;
4. architecture frame;
5. data frame;
6. security/privacy frame;
7. UX/motion frame, when applicable;
8. file/output contract;
9. execution contract;
10. scorecard.

If my prompt is too vague, ask at most 5 blocking questions.
If you can proceed with safe assumptions, declare them and continue.
Do not use generic templates, generic seed data, generic layouts, or default stacks when the domain requires more specific choices.
```

## Per landing e siti

Aggiungi sempre:

- pubblico;
- promessa;
- prova;
- CTA;
- tono;
- pattern visivi da evitare;
- contenuti reali minimi;
- performance budget.

## Per app full-stack

Aggiungi sempre:

- utenti/ruoli;
- modello dati;
- auth;
- permessi;
- flussi principali;
- seed data realistici;
- deploy target;
- test o acceptance checks.

## Per mobile

Aggiungi sempre:

- schermate;
- navigazione;
- offline/cache;
- permessi;
- notifiche;
- store readiness;
- device constraints.

## Per modifiche piccole

Usa `blueprints/12-targeted-change-blueprint.md`.

Il builder deve:

- identificare file o area da modificare;
- proporre patch minima;
- evitare refactor;
- dichiarare regressioni da evitare;
- restituire verifica.

## Per output finale

Richiedi sempre:

```markdown
# Delivery Scorecard

| Dimensione | Score | Evidenza | Rischio residuo | Azione minima |
|---|---:|---|---|---|
```

## Final output

Always require:

```markdown
# Delivery Scorecard

| Dimension | Score | Evidence | Residual risk | Minimum action |
|---|---:|---|---|---|
```
