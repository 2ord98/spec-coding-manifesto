# Marketplace Submission Guidelines

## Purpose

Document how Specification-Driven Coding artifacts may map to tooling marketplaces and registries. This is research guidance only. No submission has been made in this cycle.

## Taxonomy

### Coding agents

Examples: Codex CLI, Claude Code, Aider, Gemini CLI.
Integration surface: repository instructions, adapter Markdown, role prompts, and deterministic handoff output.
Discovery: GitHub README, topics, and official docs.

### Editor plugins/extensions

Examples: Cursor Project Rules, VS Code Marketplace, JetBrains plugin marketplace, Windsurf.
Integration surface: rule files, extension manifest, plugin metadata.
Cursor recommendation: `.cursor/rules` Project Rules. `.cursorrules` is legacy compatibility only.

### MCP hosts

Examples: Claude Desktop, Cursor MCP, Zed, MCP-compatible clients.
Integration surface: MCP manifest, tool definitions, local command/server config.
Registries/directories: official MCP registry or published server registry if available, reference server repositories, and community directories such as mcp.so or Glama if still current.

### App builders / no-code AI platforms

Examples: Lovable, Bolt, v0, Replit Agents, Base44, Emergent.
Integration surface: repo import, template galleries, starter packs, system prompt ingestion.
[TO BE VERIFIED - no public submission policy confirmed in this repository]

### Skill / prompt registries

Examples: Anthropic skills if public submission exists, PromptHub, PromptLayer public registry, LangChain Hub if still current.
[TO BE VERIFIED - check official docs before submitting]

### Python package distribution

PyPI is future work. Current state: `pyproject.toml` exists, but no PyPI publish is part of this cycle.

## Per-marketplace checklist

### MCP Registry / MCP servers ecosystem

- Canonical discovery URL: [TO BE VERIFIED - check official docs before submitting]
- Expected artifact: working MCP server, README, license, security posture, no destructive default tool calls.
- Current SDC artifact: `extensions/mcp/SPEC.md` and `extensions/mcp/manifest.json`.
- Submission readiness: design only; runtime server TBD.

### Cursor ecosystem

- Current recommendation: `.cursor/rules` Project Rules.
- Legacy `.cursorrules`: compatibility only.
- Current SDC artifact: `plugins/cursor/README.md`.
- Submission readiness: partial.

### Claude Code / Anthropic ecosystem

- Convention: `CLAUDE.md`.
- Formal marketplace status: [TO BE VERIFIED - check official docs before submitting]
- Current SDC artifact: `plugins/claude-code/README.md`.

### VS Code Marketplace

- Publisher account required.
- `package.json` extension manifest required.
- `vsce` packaging/publishing commonly used.
- Status: [TO BE VERIFIED - requires vsce setup and publisher account]

### App builder template galleries

For Lovable, Bolt, v0, Replit, Base44, and Emergent: [TO BE VERIFIED - no public submission policy confirmed in this repository].
Fallback: use this repository as source-of-truth if the platform supports GitHub import.

### PyPI

- Possible package names: `spec-coding-manifesto`, `specification-driven-coding`, `sdc-cli`.
- Preferred future method: Trusted Publishing / OIDC from GitHub Actions if configured.
- Current state: planned, not this cycle.

## SDC Readiness Matrix

| Marketplace | SDC artifact ready | Format correct | Submission ready | Notes |
|---|---|---|---|---|
| MCP Registry / MCP catalogs | DESIGN ONLY | PARTIAL | NO | Runtime server not implemented |
| Cursor ecosystem | PARTIAL | PARTIAL | [TO BE VERIFIED] | Project Rules guidance exists |
| Claude Code ecosystem | PARTIAL | PARTIAL | [TO BE VERIFIED] | Adapter guidance exists |
| VS Code Marketplace | NO | NO | NO | Extension scaffold not in scope |
| App builder galleries | PARTIAL | PARTIAL | [TO BE VERIFIED] | GitHub import fallback only |
| Skill/prompt registries | PARTIAL | PARTIAL | [TO BE VERIFIED] | Skills exist, submission policies unknown |
| PyPI | NEAR-READY | PARTIAL | NO | Publish deferred |
