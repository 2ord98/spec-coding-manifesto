# Task e Project Modes

Specification-Driven Coding deve funzionare sia per modifiche piccole sia per progetti interi.

Pipeline ufficiale: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## Simple task mode

Usare quando la modifica è locale e non cambia contratti principali.

Template:

```markdown
# Simple Task Spec

## Intent

## Area impattata

## Assunzioni

## Patch plan

## Verifica

## Rischio
- Low / Medium / High
```

Regola: se una modifica locale impatta permessi, dati o deploy, promuovere a `feature`.

## Feature mode

Usare quando si aggiunge o modifica una funzionalità.

Output:

- spec breve;
- contratti modificati;
- task;
- test;
- retro-spec.

## Full project mode

Usare per generare un progetto nuovo o una porzione autonoma.

Output:

- spec completa;
- Vertical Blueprint Contract;
- file tree;
- piano tecnico;
- tasks;
- implementazione;
- scorecard.

## Multi-agent mode

Usare quando il sistema include più agenti o tool automatici.

Output:

- agent role cards;
- state machine;
- tool registry;
- permissions;
- approval gates;
- telemetry;
- failure modes;
- eval.
