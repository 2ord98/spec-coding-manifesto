# Plugins e adapter

Questa cartella contiene guide di adattamento per usare Specification-Driven Coding con tool e workflow diversi.

Pipeline ufficiale: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

- `toolkit-adapter.md`: adapter di compatibilità per workflow specification-first.
- `agents-md.md`: uso con repository che leggono `AGENTS.md`.
- `app-builder-usage.md`: uso con app builder prompt-to-product.
- `cursor-rules.md`: uso con regole e contesto editoriale.
- `claude-code-skills.md`: uso con skill e agenti di coding.
- `mcp-tooling.md`: uso con MCP/tooling governato.
- `claude-code/README.md`: target-specific handoff guidance for Claude Code.
- `codex/README.md`: target-specific handoff guidance for Codex.
- `cursor/README.md`: target-specific handoff guidance for Cursor Project Rules.
- `aider/README.md`: target-specific handoff guidance for Aider.
- `gemini/README.md`: target-specific handoff guidance for Gemini CLI.
- `generic/README.md`: fallback target-specific handoff guidance.
- `builder/README.md`: app-builder execution packet guidance.

`sdc handoff` uses target-specific guidance to produce deterministic execution packets. Plugins remain documentation and adapter guidance only; they do not install, apply, fetch, or execute remote code.

Regola: gli adapter non sono sorgente di verità autonoma. Devono sempre rispettare manifesto, costituzione, project profile, blueprint e scorecard.
