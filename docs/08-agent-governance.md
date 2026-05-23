# Governance agentica

## Regola

Ogni agente deve essere progettato come componente con responsabilità limitata.

## Agent Card

```markdown
# Agent: <nome>

## Mandato

## Input ammessi

## Output richiesti

## Tool permessi

## Tool vietati

## Stop conditions

## Reviewer

## Quality gate
```

## Pattern consigliato

- Product Architect: chiarisce problema e scope.
- Requirements Engineer: produce spec verificabile.
- Blueprint Compiler: traduce spec e project profile in blueprint verticale eseguibile.
- UX Systems Designer: evita output generico.
- Platform Architect: sceglie stack e architettura.
- AI Systems Architect: gestisce RAG, agenti, modelli, eval.
- Security Reviewer: controlla permessi, dati, threat model.
- QA Evaluator: crea acceptance, test matrix e scorecard.
- Implementation Agent: scrive codice solo da task approvati.
- Release Manager: verifica deploy, rollback, changelog.

## Multi-agent construction

Nei sistemi multi-agente, nessun agente deve avere mandato vago come “fai tutto”.

Ogni agente deve avere:

- input ammessi;
- output verificabile;
- tool consentiti;
- memoria consentita;
- stop conditions;
- reviewer;
- audit log.

## Human-in-the-loop

Obbligatorio per:

- azioni distruttive;
- invio email o notifiche reali;
- pagamenti;
- pubblicazione contenuti;
- modifiche a sistemi fisici;
- accesso a dati sensibili;
- remediation security;
- decisioni legali, mediche o finanziarie.
