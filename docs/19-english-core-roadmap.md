# English core roadmap

Specification-Driven Coding can remain culturally rooted in this repository while exposing an English-first or bilingual core for global adoption.

This roadmap does not require translating the whole repository at once. The preferred path is bilingual execution coverage: keep the original Italian voice where it matters, while making technical instructions readable by English-consuming agents.

## English-first candidates

- `README.md`
- `MANIFESTO.md`
- `AGENTS.md`
- `ai-adapters/GENERIC-AGENT.md`
- `ai-adapters/BUILDER-INGESTION.md`
- `docs/02-methodology.md`
- `docs/13-blueprint-compiler.md`
- `docs/14-vertical-blueprint-contracts.md`
- `docs/16-cross-tool-ingestion-matrix.md`
- `scorecards/`
- `blueprints/`

## Recommended sequence

1. Keep descriptive/manifesto files editorially controlled instead of mass-translating them.
2. Make the technical ingestion path bilingual: `AGENTS.md`, methodology, command model, blueprint contract, scorecards, prompts index, benchmark docs.
3. Translate or mirror only the operational sections of adapters, prompts, blueprints, skills, and scorecards.
4. Leave deeper narrative docs Italian-first until they are promoted to source-of-truth status.
5. Keep Italian commentary where it carries identity, but make execution rules available in English.

## Current bilingual core

- `docs/25-english-public-index.md`
- `README.md`
- `MANIFESTO.md`
- `CONTRIBUTING.md`
- `README.it.md`
- `MANIFESTO.it.md`
- `AGENTS.md`
- `docs/02-methodology.md`
- `docs/21-command-model.md`
- `blueprints/00-blueprint-contract.md`
- `blueprints/01-ai-builder-master-blueprint.md`
- `blueprints/02-full-project-blueprint.md`
- `prompts/README.md`
- `prompts/app-builder-ingestion.prompt.md`
- `prompts/builder-ingestion.prompt.md`
- `prompts/compile-to-builder-blueprint.prompt.md`
- `prompts/write-vertical-blueprint.prompt.md`
- `prompts/write-targeted-change-blueprint.prompt.md`
- `plugins/app-builder-usage.md`
- `plugins/toolkit-adapter.md`
- `scorecards/README.md`
- `scorecards/blueprint-scorecard.md`
- `scorecards/implementation-scorecard.md`
- `scorecards/specification-prompt-scorecard.md`
- `benchmarks/README.md`

## Translation rule

Do not translate by making the method generic. Preserve the core terms:

- Specification-Driven Coding
- Vertical Blueprint
- Project Profile
- Assumption Ledger
- Evaluation Scorecard
- anti-genericity

## Acceptance gate

An English-consuming agent should be able to ingest the repo and follow the official pipeline without relying on Italian-only instructions.

The public international core is now covered by `README.md`, `MANIFESTO.md`, `CONTRIBUTING.md`, and `docs/25-english-public-index.md`. Full translation of the deeper docs, prompts, blueprints, and plugins remains a roadmap item.
