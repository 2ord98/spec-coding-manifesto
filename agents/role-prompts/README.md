# Role Prompts

Role prompts are executable, domain-agnostic wrappers for agent behavior. They do not replace `AGENTS.md`, role cards, specifications, or Vertical Blueprints.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Available role prompts

- `startup-engineer.md` — Startup Engineer
- `codebase-auditor.md` — Codebase Auditor
- `debugging-engineer.md` — Debugging Engineer
- `performance-engineer.md` — Performance Engineer
- `architecture-refactorer.md` — Architecture Refactorer
- `systems-architect.md` — Systems Architect
- `multi-agent-team.md` — Multi-Agent Team
- `frontend-engineer.md` — Frontend Engineer
- `technical-lead.md` — Technical Lead
- `security-auditor.md` — Security Auditor
- `devops-engineer.md` — DevOps Engineer
- `ai-engineer.md` — AI Engineer
- `requirements-engineer.md` — Requirements Engineer

## Usage

Load one role prompt only after the relevant Specification-Driven Coding artifacts exist. Role prompts constrain behavior; they do not generate applications, bypass scorecards, or replace human engineering judgment.
