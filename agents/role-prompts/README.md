# Role Prompts

Role prompts are executable, domain-agnostic wrappers for agent behavior. They do not replace `AGENTS.md`, role cards, specifications, or Vertical Blueprints.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Available role prompts

| Role file | Role | Handoff fit |
|---|---|---|
| `startup-engineer.md` | Startup Engineer | Small validated slices |
| `codebase-auditor.md` | Codebase Auditor | Review and drift detection |
| `debugging-engineer.md` | Debugging Engineer | Root-cause and fix loops |
| `performance-engineer.md` | Performance Engineer | Budget and optimization checks |
| `architecture-refactorer.md` | Architecture Refactorer | Behavior-preserving refactor |
| `systems-architect.md` | Systems Architect | Blueprint and architecture decisions |
| `multi-agent-team.md` | Multi-Agent Team | Governed multi-agent workflow |
| `frontend-engineer.md` | Frontend Engineer | UI implementation under constraints |
| `technical-lead.md` | Technical Lead | Scope, risk, and review gates |
| `security-auditor.md` | Security Auditor | Security/privacy review |
| `devops-engineer.md` | DevOps Engineer | Deployment and operational checks |
| `ai-engineer.md` | AI Engineer | AI/RAG/tooling work under artifacts |
| `requirements-engineer.md` | Requirements Engineer | Intake, clarification, assumptions |

## Usage

Load one role prompt only after the relevant Specification-Driven Coding artifacts exist. Role prompts constrain behavior; they do not generate applications, bypass scorecards, or replace human engineering judgment.

## Maturity sections

Every role prompt must include Signature, Mission, Role assumption, Mission goals, Deliverables, Guardrails, Failure modes, Scorecard focus, Compatible phases, Compatible target CLIs, and Abstract demonstrations.
