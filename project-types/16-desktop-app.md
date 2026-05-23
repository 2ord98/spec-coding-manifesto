# Desktop app locale o hybrid

- Profile id: `desktop-app`
- Quando usarlo: App desktop con file locali, AI locale/remota, automazioni, editor, visual tool, app offline.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quali file locali legge/scrive?
- Deve funzionare offline?
- Quali OS supportare?
- Serve modello locale o API cloud?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Tauri + Svelte/React/Vue per app leggere
- Electron per ecosistema maturo
- PySide/PyQt per tool Python
- Avalonia/.NET MAUI per ecosistema .NET
- Local models via Ollama/llama.cpp se richiesto

## Must-have spec fields

- Local file permissions
- Install/update flow
- Offline behavior
- Privacy boundaries
- Crash recovery
- Packaging target OS

## Anti-pattern da evitare

Non trasformare ogni desktop app in Electron se local-first, performance o distribuzione sono centrali.

## Acceptance gates

- File operations sicure
- Installer/package documentato
- Stato salvato e recuperabile
- Nessun upload nascosto di file locali

## Prompt seed

```text
Stai costruendo un progetto di tipo `desktop-app`.
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
