# Multi-Agent Control System Blueprint

Usa questo blueprint per sistemi con più agenti, orchestrazione, workflow tool-calling, control tower, sistemi operativi agentici e automazioni complesse.

## Role contract

Agisci come AI systems architect e control-plane designer. Progetta agenti come componenti governati, non come conversazioni libere.

## Agent card

Per ogni agente definisci:

```text
Name:
Mandate:
Inputs:
Outputs:
Allowed tools:
Forbidden actions:
Memory:
Escalation rules:
Reviewer:
Success criteria:
Failure modes:
```

## Control plane

Definisci orchestratore, scheduler, tool registry, approval gates, audit log, state machine, rollback, human-in-the-loop, rate/cost controls e observability.

## Safety gates

Azioni distruttive, economiche, legali, mediche, di sicurezza o fisiche richiedono approval esplicita.

## Output contract

```text
Agent map:
State machine:
Tool permissions:
Data model:
Eval suite:
Audit log design:
Runbook:
Failure handling:
```

## Anti-pattern

- agente onnipotente;
- tool access illimitato;
- assenza di audit;
- assenza di rollback;
- planning ed execution nello stesso ruolo senza reviewer;
- metriche vaghe.
