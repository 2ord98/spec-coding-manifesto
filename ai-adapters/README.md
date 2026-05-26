# AI Adapters

Provider-specific and builder-specific instruction files live here so the repository root stays focused on `README.md`, `MANIFESTO.md`, and `AGENTS.md`.

`AGENTS.md` remains in the root because many coding agents use it as the default repository instruction file. `.github/copilot-instructions.md` remains under `.github/` because Copilot expects that path.

## Files

- `CODEX.md`: Codex adapter.
- `CLAUDE.md`: Claude Code adapter.
- `COPILOT.md`: human-readable Copilot adapter. The automatic Copilot instruction file remains `.github/copilot-instructions.md`.
- `GEMINI.md`: Gemini CLI adapter.
- `GROK.md`: Grok adapter.
- `WINDSURF.md`: Windsurf adapter.
- `GENERIC-AGENT.md`: generic LLM/coding-agent adapter.
- `BUILDER-INGESTION.md`: app-builder ingestion adapter.

## Handoff targets

Use `sdc handoff --target ...` to assemble target-specific execution packets for `generic`, `codex`, `claude-code`, `cursor`, `aider`, `gemini-cli`, `builder`, and `mcp`. Adapter files remain source-of-truth pointers; target plugin guidance lives in `plugins/<target>/README.md`.

## Rule

Adapters must point back to the source-of-truth documents instead of duplicating the manifesto:

- `README.md`
- `MANIFESTO.md`
- `AGENTS.md`
- `docs/02-methodology.md`
- `docs/12-builder-ingestion-protocol.md`
- `docs/14-vertical-blueprint-contracts.md`
- `docs/21-command-model.md`
- `docs/36-cli-target-matrix.md`
