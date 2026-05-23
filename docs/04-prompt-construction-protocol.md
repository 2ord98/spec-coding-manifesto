# Protocollo di costruzione del prompt

Specification-Driven Coding considera il prompt non come messaggio, ma come artefatto compilabile.

## Obiettivo

La repo deve essere data in pasto a un modello, coding agent o app builder affinché trasformi qualunque richiesta in uno **Specification-Driven Prompt**.

Il risultato non deve essere “un prompt più bello”. Deve essere un prompt capace di produrre software specifico, testabile e meno generico.

## Da prompt grezzo a prompt costruibile

### Prompt grezzo

```text
Fammi una piattaforma tipo dashboard con AI per analizzare documenti.
```

### Specification-Driven Prompt

```text
Costruisci un MVP web per un team operations che carica PDF contrattuali e vuole estrarre parti, date, importi, clausole di rinnovo e rischi.
Utente primario: operations manager non tecnico.
Vincolo: ogni campo estratto deve mostrare pagina, frase sorgente e confidence.
Stack preferito: SvelteKit + FastAPI + Postgres; motiva alternative se non adeguate.
Non-obiettivi: niente firma digitale, niente gestione legale completa.
Safety: se confidence < 0.75 manda in review umana.
Acceptance: 10 documenti test, output JSON validato, UI review queue, audit log.
Scorecard finale obbligatoria.
```

## Struttura canonica

1. **Intento**: cosa deve esistere.
2. **Utente**: chi usa davvero il sistema.
3. **Contesto**: dominio, ambiente, vincoli.
4. **Non-obiettivi**: cosa non costruire.
5. **Profilo progetto**: uno dei `project-types/`.
6. **Stack preference**: scelta o spazio decisionale.
7. **Dati**: input, output, persistenza, privacy.
8. **Azioni**: ciò che il sistema può fare.
9. **Design direction**: non estetica generica, ma direzione coerente col dominio.
10. **Rischi**: failure mode e mitigazioni.
11. **Output contract**: file, patch, artefatti o prodotto attesi.
12. **Acceptance**: come si verifica che funziona.
13. **Scorecard**: come si valuta il risultato.

## Domande buone

Una domanda è buona se cambia almeno una delle seguenti cose:

- architettura;
- modello dati;
- permessi;
- UX primaria;
- integrazioni;
- costo;
- sicurezza;
- test;
- deploy.

## Domande cattive

Sono cattive le domande che rimandano decisioni deducibili, chiedono preferenze cosmetiche premature o bloccano il lavoro su dettagli reversibili.

## Assumption ledger

Quando manca un dettaglio non bloccante, l’agente deve dichiarare:

```text
Assunzione:
Motivo:
Impatto se sbagliata:
Reversibilità: alta / media / bassa
Verifica:
```

## Output minimo del prompt costruibile

```markdown
# Specification-Driven Prompt

## Intento normalizzato

## Project profile scelto

## Utente primario

## Dominio e contesto

## Non-obiettivi

## Vincoli non negoziabili

## Assumption ledger

## Stack direction

## Design/product direction

## Output contract

## Acceptance criteria

## Scorecard richiesta
```

## Regola

L’agente deve prima migliorare il prompt, poi scrivere specification, poi blueprint, poi pianificare, poi implementare.
