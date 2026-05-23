# Sistema multi-agente / control tower operativa

- Profile id: `multi-agent-control-system`
- Quando usarlo: Sistemi con più agenti specializzati, orchestration, knowledge graph/ontology, controllo operativo, decision support tipo “control tower”.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quale decisione o processo viene coordinato?
- Quali agenti servono davvero?
- Dove è obbligatorio human-in-the-loop?
- Quali tool sono read-only vs write-capable?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Orchestratore: LangGraph, CrewAI, Semantic Kernel, AutoGen o custom state machine
- Tool registry con MCP/API interne
- Knowledge graph: Neo4j/TypeDB/GraphQL federation se serve ontologia
- Eventing: Temporal/NATS/Kafka per workflow robusti
- UI: dashboard operativa con audit trail

## Must-have spec fields

- Agent role cards
- State machine
- Human approval gates
- Tool permissions
- Audit trail
- Rollback/compensation
- Telemetry e eval

## Anti-pattern da evitare

Non creare “agent swarm” senza controllo. Ogni agente deve avere ruolo, input, output, strumenti, limiti e reviewer.

## Acceptance gates

- Nessun agente ha permessi illimitati
- Ogni tool call è loggata
- Il sistema può spiegare perché ha agito
- Failure mode e stop conditions sono testati

## Prompt seed

```text
Stai costruendo un progetto di tipo `multi-agent-control-system`.
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

`blueprints/05-multi-agent-system-blueprint.md`.

Il blueprint deve includere file/output contract, security/privacy frame, anti-genericity constraints e scorecard target.
