# Developer tool, CLI, SDK, plugin o MCP server

- Profile id: `developer-tool-cli-mcp`
- Quando usarlo: Strumenti per sviluppatori, CLI, estensioni VS Code, plugin, SDK, server MCP, automazioni repo.

## Obiettivo del profilo

Guidare l’agente a costruire un progetto specifico per questa categoria, evitando default generici e decisioni implicite.

## Domande di intake obbligatorie

- Quale comando principale deve ricordare l’utente?
- Quali input arrivano da file/env/flag?
- Serve modalità dry-run?
- Quale piattaforma è target?

## Stack candidates

Non sono default automatici. L’agente deve scegliere e motivare.

- Python Typer/Rich o Node/TypeScript Commander
- Go/Rust per CLI single-binary
- MCP server TypeScript/Python
- VS Code extension TypeScript
- SDK con OpenAPI/Typed clients

## Must-have spec fields

- Command UX
- Config precedence
- Exit codes
- Dry-run mode
- Structured logs
- Docs/examples
- Compatibility matrix

## Anti-pattern da evitare

Non scrivere tool senza definire UX da terminale, errori, config, test e compatibilità OS.

## Acceptance gates

- Help CLI chiaro
- Errori leggibili e codici exit
- Test su casi edge
- Nessuna credenziale in log

## Prompt seed

```text
Stai costruendo un progetto di tipo `developer-tool-cli-mcp`.
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
