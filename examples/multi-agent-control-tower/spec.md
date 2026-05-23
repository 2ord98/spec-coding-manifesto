# Feature Spec: Control tower multi-agente per operazioni interne

## Specification-Driven Coding header

- Project profile: `multi-agent-control-system`
- Utente primario: operations lead
- Problema specifico: coordinare analisi, triage e raccomandazioni operative senza azioni write automatiche
- Non-obiettivi: nessuna remediation automatica in produzione
- Vincoli: tool read-only di default; human approval per azioni sensibili

## Agent roles

- Triage Agent: classifica evento.
- Research Agent: raccoglie evidenza.
- Recommendation Agent: propone azione.
- Reviewer Agent: verifica policy e rischi.

## Functional requirements

- FR-001: creare caso operativo da evento.
- FR-002: raccogliere evidenza da fonti autorizzate.
- FR-003: proporre azione con rationale.
- FR-004: richiedere approvazione umana prima di eseguire tool write.

## Acceptance criteria

- AC-001: ogni tool call è loggata.
- AC-002: sistema può spiegare decisione.
- AC-003: stop condition testata per evidenza insufficiente.
