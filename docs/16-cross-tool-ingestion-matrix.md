# Cross-tool ingestion matrix

Specification-Driven Coding should be easy to ingest by agents, app builders, and generic LLM workflows without duplicating the manifesto in every adapter.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

| Tool / builder | Best file to ingest first | Secondary files | Best use case | Known limits | Required output contract | Evaluation requirement |
|---|---|---|---|---|---|---|
| Generic LLM | `ai-adapters/GENERIC-AGENT.md` | `README.md`, `docs/02-methodology.md`, `blueprints/`, `scorecards/` | Single-shot reasoning, prompt rewriting, spec drafting | May not inspect repo automatically | Intake, assumptions, spec, blueprint, scorecard | Explicit scorecard and residual risks |
| Codex | `AGENTS.md` | `ai-adapters/CODEX.md`, `docs/13-blueprint-compiler.md`, `blueprints/` | Coding agent work, repo edits, validation loops | Needs clear file scope and approval gates | Patch or files plus validation and scorecard | Run local checks before delivery |
| Claude Code | `AGENTS.md` | `ai-adapters/CLAUDE.md`, `docs/02-methodology.md`, `skills/specification-driven-coding/SKILL.md` | Long-form coding sessions and skill-driven workflows | Long memories can dilute rules | Spec, blueprint, plan, tasks, changed files | Scorecard and retro-spec when behavior changes |
| Cursor | `AGENTS.md` | `plugins/cursor-rules.md`, `.cursor/rules` if present | Editor agent work and scoped repo changes | Rules may be scoped or manually invoked | Minimal patch or blueprint-driven task list | Validation plus changed-file summary |
| Copilot | `.github/copilot-instructions.md` | `ai-adapters/COPILOT.md`, `.github/prompts/` | Chat, code review, prompt files, small implementation tasks | Custom instructions are not deterministic | Short repository-specific output contract | State confidence, tests, and scorecard when applicable |
| Gemini CLI | `ai-adapters/GEMINI.md` | `AGENTS.md`, `docs/02-methodology.md`, `blueprints/` | CLI-driven analysis, scaffolding, code work | Context loading depends on CLI mode | Intake through scorecard or minimal patch | Validation command output summary |
| Grok | `AGENTS.md` | `ai-adapters/GROK.md`, `ai-adapters/GENERIC-AGENT.md`, `docs/00-online-panorama.md` | Research-assisted planning and critique | Live claims require verification | Source-grounded assumptions and blueprint | Separate verified facts from assumptions |
| Windsurf | `AGENTS.md` | `ai-adapters/WINDSURF.md`, `.windsurf/rules/` if used | Cascade workspace edits and rules-based workflows | Memories are less durable than rules | Blueprint-first plan or targeted patch | Validation and scorecard |
| Emergent | `ai-adapters/BUILDER-INGESTION.md` | `docs/12-builder-ingestion-protocol.md`, `blueprints/01-ai-builder-master-blueprint.md` | Prompt-to-product builds | Stack/file control may be partial | Builder Execution Packet and delivery scorecard | Score output against blueprint |
| Manus | `ai-adapters/BUILDER-INGESTION.md` | `docs/13-blueprint-compiler.md`, `blueprints/` | App/mobile builder workflows | May abstract file tree details | Product spec, blueprint, acceptance gates | Scorecard plus known gaps |
| Base44-style builder | `ai-adapters/BUILDER-INGESTION.md` | `ai-adapters/GENERIC-AGENT.md`, `blueprints/01-ai-builder-master-blueprint.md` | App-builder prompts and execution packets | Tool behavior may vary by environment | Builder-ready blueprint | Final gap list and scorecard |
| Lovable | `ai-adapters/BUILDER-INGESTION.md` | `plugins/app-builder-usage.md`, `prompts/app-builder-ingestion.prompt.md` | Web app generation from structured prompts | Can default to familiar UI patterns | Domain-specific UX/data/file contract | Anti-genericity score and acceptance checks |
| Bolt | `ai-adapters/BUILDER-INGESTION.md` | `blueprints/06-web-product-blueprint.md`, `scorecards/implementation-scorecard.md` | Fast web prototypes and MVP slices | Runtime/deploy constraints need explicit bounds | File tree, run commands, tests | Smoke test and scorecard |
| v0 | `ai-adapters/BUILDER-INGESTION.md` | `docs/06-anti-sameness-design.md`, `blueprints/06-web-product-blueprint.md` | UI generation and interface slices | Backend/data behavior may be out of scope | UX contract, states, responsive behavior | Design/domain fit score |
| Replit | `ai-adapters/BUILDER-INGESTION.md` | `docs/12-builder-ingestion-protocol.md`, `blueprints/02-full-project-blueprint.md` | Runnable prototypes and full-stack demos | Must make secrets/deploy assumptions explicit | Run/test/deploy contract | Executed checks and scorecard |
| MCP-enabled agent | `ai-adapters/GENERIC-AGENT.md` | `plugins/mcp-tooling.md`, `docs/08-agent-governance.md` | Tool-calling workflows and governed automation | Tool permissions can create real-world risk | Tool registry, permissions, approval gates | Audit log and scorecard |

Keep adapters short. The source of truth remains the methodology, profiles, blueprints, and scorecards.
