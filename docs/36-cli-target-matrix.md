# CLI Target Matrix

## Purpose

Map Specification-Driven Coding handoff packets to supported execution targets.

## Matrix

| Target | Best for | Not best for | Required artifacts | Validation expectation | Output contract | Risk notes |
|---|---|---|---|---|---|---|
| generic | Model/tool-neutral handoff | Tool-specific automation | spec, blueprint, plan, tasks, scorecard | Report commands and evidence | Summary, changes, risks, scorecard | May need manual adaptation |
| codex | Repository edits and CLI validation | Unbounded product generation | workspace artifacts plus repo context | Run repo checks before final response | Minimal diff and changed files | Avoid broad refactors |
| claude-code | Long-context artifact reading | Silent file invention | full artifact chain | Plan before implementation | Assumptions and updated artifacts if drift appears | Verify file existence |
| cursor | Editor-scoped implementation | Large autonomous rewrites | artifacts plus project rules | Validate touched files | Changed-file summary | Prefer `.cursor/rules`; `.cursorrules` is legacy compatibility only |
| aider | Patch-oriented file edits | Ambiguous broad scope | explicit file boundaries | Small patch validation | Patch summary and residual risk | Ask before broad edits |
| gemini-cli | CLI-driven inspection and synthesis | Hidden assumptions | artifacts and command outputs | Separate facts from assumptions | Verified facts, assumptions, validation | Do not over-trust summaries |
| builder | App-builder execution packet | Generic SaaS/dashboard defaults | blueprint, file tree, UX states, scorecard | Anti-genericity gates | Build constraints and acceptance criteria | Require domain-fit proof |
| mcp | Tool-governed multi-agent work | Destructive automation | artifacts, permissions, scorecard | Approval gates and audit log | Tool plan, calls, evidence, risks | No destructive calls without approval |

## Operational situations

- Intake/spec clarification: `generic`, `claude-code`, `gemini-cli`
- Blueprint compilation: `codex`, `claude-code`, `generic`
- Implementation: `codex`, `cursor`, `aider`
- Code review: `codex`, `claude-code`, `gemini-cli`
- Refactor: `codex`, `aider`, `cursor`
- Debugging: `codex`, `aider`, `gemini-cli`
- Performance optimization: `codex`, `cursor`, `gemini-cli`
- Security audit: `codex`, `claude-code`, `mcp`
- Deployment/devops: `codex`, `gemini-cli`, `mcp`
- Frontend/UI: `cursor`, `builder`, `codex`
- AI/RAG work: `codex`, `claude-code`, `mcp`
- Multi-agent/MCP coordination: `mcp`, `generic`

## Quality gate

Every target must preserve the official pipeline and carry the decision matrix and scorecard forward.
