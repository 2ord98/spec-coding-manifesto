# Security, SecOps, compliance e audit agent

- Profile id: `security-secops-compliance-agent`
- Quando usarlo: Analisi log, triage alert, compliance evidence, vulnerability management, policy assistant, audit automation.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali sistemi legge e quali può modificare?
- Quali alert sono in scope?
- Quali azioni richiedono approvazione?
- Come si conserva evidenza per audit?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- SIEM/SOAR integrations
- Python/FastAPI workers
- OpenTelemetry/log pipelines
- RAG su policy e runbook
- Read-only first + approval for actions
- OPA/Rego o policy-as-code se utile

## Must-have spec fields

- Threat model
- Permission boundaries
- Evidence chain
- Human approval
- Runbooks
- Audit logs
- False positive handling

## Anti-pattern da evitare

Non permettere remediation automatica senza human approval, scope, blast-radius e rollback.

## Acceptance gates

- Accesso minimo e tracciato
- Remediation gated
- Evidenze esportabili
- False positive e escalation gestiti

## Prompt seed

```text
Stai costruendo un progetto di tipo `security-secops-compliance-agent`.
Prima di proporre stack o codice, completa intake, vincoli, non-obiettivi e anti-genericity constraints.
Poi scrivi spec, blueprint, plan e task usando i template Specification-Driven Coding.
Se una scelta tecnica è implicita, fermati e dichiarala come assunzione o domanda bloccante.
```

## Output minimo richiesto all’agente

- Spec con requisiti funzionali e non funzionali.
- Piano tecnico con stack motivato e alternativa scartata.
- Task atomici ordinati per dipendenza.
- Acceptance matrix.
- Audit anti-genericità.

## Blueprint consigliato

`blueprints/02-full-project-blueprint.md`; se usato con app builder, prima compilare `blueprints/01-ai-builder-master-blueprint.md`.

Il blueprint deve includere file/output contract, security/privacy frame, anti-genericity constraints e scorecard target.
