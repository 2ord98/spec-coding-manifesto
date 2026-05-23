# Harness roadmap

This roadmap defines how Specification-Driven Coding evolves from manifesto and kit into a benchmarkable methodology.

Official pipeline: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## Goal

Create a repeatable harness that compares whether agents and builders follow the methodology, not whether they merely produce plausible output.

The first executable harness is `tools/sdc_harness.py`. It checks fixed fixtures in `benchmarks/fixtures/` against golden artifacts in `benchmarks/golden/` and writes reports to `benchmarks/reports/`.

## Golden examples

- Store raw prompt fixtures by project type.
- Pair each fixture with expected intake, specification, project profile, Vertical Blueprint, plan, tasks, and scorecard.
- Include at least one full project, one targeted change, one app-builder prompt, one brownfield patch, one RAG system, and one multi-agent system.

## Expected artifacts

Each fixture should define:

- raw request;
- blocking questions or assumption ledger;
- expected project profile;
- expected anti-genericity constraints;
- expected Vertical Blueprint frames;
- expected plan slices;
- expected task shape;
- expected scorecard thresholds.

## Tests

- Structural tests: required files, sections, pipeline order, naming, internal links, provenance guard.
- Semantic tests: compare generated artifacts against expected contracts, non-goals, constraints, and acceptance criteria.
- Regression tests: rerun old fixtures when methodology docs, blueprints, prompts, or scorecards change.
- Link rot checks: verify external references in docs and publishing guide.
- Version drift checks: flag tool-specific docs that may have changed.
- Cross-agent comparison runs: run the same fixture through Codex, Claude Code, Gemini CLI, Copilot, Cursor, Windsurf, app builders, and a generic LLM.

## Scoring approach

Start with lightweight structural checks, then add rubric-based review. Do not treat keyword coverage as proof of quality. The current harness is intentionally structural: it checks fixture completeness, golden artifact coverage, and scorecard shape. The long-term target is artifact comparison against expected contracts plus human review for ambiguous product judgment.

The provenance guard should explicitly verify absence of authorship or private-prompt history language such as tool-created claims, hidden conversational origin, or repository-as-generated framing, while allowing legitimate tool references as ingestion or execution targets.

## Non-goals for now

- No heavy dependencies.
- No hosted benchmark service.
- No automatic claims about agent superiority.
- No hidden evaluation data until the fixture set is stable.
