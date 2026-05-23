# IoT, edge AI, robotica o sistemi di controllo

- Profile id: `iot-edge-control`
- Quando usarlo: Telemetria, dispositivi, sensori, edge inference, controllo remoto, robotica, automazione fisica.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Il sistema legge solo o controlla attuatori?
- Quali comandi possono causare danni?
- Quale rete/hardware è disponibile?
- Cosa succede se connessione o modello falliscono?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- MQTT + FastAPI/Node/.NET backend
- Edge: Python, Rust, Go, C++ secondo hardware
- Grafana/Prometheus per telemetry
- OPC UA/Modbus se industriale
- TinyML/ONNX Runtime se inferenza edge

## Must-have spec fields

- Device registry
- Telemetry schema
- Command authorization
- Safety interlocks
- Offline/fail-safe modes
- Firmware/versioning
- Observability

## Anti-pattern da evitare

Non autorizzare azioni fisiche senza safety gate. Read-only prima, poi comandi con limiti, audit e fail-safe.

## Acceptance gates

- Comandi pericolosi richiedono conferma/autorizzazione
- Fail-safe definito
- Telemetria validata
- Nessun controllo fisico basato solo su output LLM

## Prompt seed

```text
Stai costruendo un progetto di tipo `iot-edge-control`.
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
