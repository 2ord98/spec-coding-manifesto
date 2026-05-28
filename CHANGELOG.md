# Changelog

## [0.7.0] — 2026-05-28

### Added

- Formal decision ledger schema and template for decisions.jsonl.
- Formal capability boundary schema for capability-boundaries.json.
- Drift exception template and naming convention for future workspace exceptions.
- Failure mode catalogs for all 20 project profiles.
- Skill activation matrix for profile/phase/workspace-state driven skill selection.
- sdc compile now emits decisions.jsonl and capability-boundaries.json.
- Fixture 004 now validates formal ledger artifacts.
- Contract schema hardening documentation.

### Changed

- Profile depth now includes 7 required files per profile, including failure-modes.md.
- spec_lint.py validates decision ledgers, capability boundaries, exception template structure, failure-mode catalogs, and skill activation matrix.
- Compile now preserves existing formal ledgers unless --force is used.
- Formal ledger validation now rejects extra keys and malformed entries.
- Documentation now positions sdc verify as the next deterministic verification phase.

### Notes

- No sdc verify implementation is included in this release.
- No LLM or API calls are introduced.
- No PyPI publication.
- No runtime MCP server.
- No marketplace submission.
- The release remains deterministic and stdlib-only.

## [0.6.0] — 2026-05-27

### Added

- Python-first consumer workflow: `git clone ... .sdc` + `python3 .sdc/tools/sdc.py` requires only Python 3.11+ and Git.
- Profile depth metadata for all 20 project profiles (`stack-options.json`, `domain-dictionary.json`, `security-baseline.md`, `performance-budget.json`, `testing-contract.md`, `blueprint-template.md`).
- Deterministic `sdc compile`: stdlib-only artifact compiler, no LLM calls, fills decision boundaries using profile-depth metadata.
- `sdc handoff`: deterministic prompt assembler for 8 target CLI workflows (`generic`, `codex`, `claude-code`, `cursor`, `aider`, `gemini-cli`, `builder`, `mcp`).
- DSPy-inspired structural contracts: `ProfileSignature`, `RolePromptSignature`, `DecisionAssertion` in `tools/sdc_signature.py`.
- `compile_with_assertions()` runtime validation against metric gates.
- 13 domain-agnostic role prompts in `agents/role-prompts/`.
- CLI Target Matrix (`docs/36-cli-target-matrix.md`).
- Agentic protocol (`docs/37-agentic-protocol.md`).
- MCP integration design (`docs/38-mcp-integration.md`) — design only, no runtime server.
- Marketplace readiness guide (`docs/39-marketplace-submission-guidelines.md`).
- Structural fixture `004-compile-structural-validation`.
- No-empty-critical-sections enforcement gate.
- Anti-template charter and decision-space model docs.
- Migration guide from editable install.

### Changed

- Profile list now shows `depth: PASS/FAIL`.
- `spec_lint.py` extended with profile-depth, role-prompt, signature, handoff, MCP, and marketplace validation gates.
- README and MANIFESTO updated with Python-first onboarding, Before/After comparison, anti-template positioning, and CLI matrix guidance.

### Notes

- compile and handoff are deterministic and stdlib-only.
- No LLM or API calls are performed.
- No application domain is hardcoded in profile metadata or engine logic.
- No marketplace submission has been made.
- PyPI publication is planned for a future release.

## 0.5.0

- Added `extensions/catalog.json` and `extensions/README.md` for discoverable optional method modules.
- Added `presets/catalog.json` and `presets/README.md` for ready operational bundles built from existing profiles, blueprints, prompts, scorecards, fixtures and gates.
- Added CLI discovery commands for `sdc extension list` and `sdc preset list`, including JSON output.
- Extended `tools/spec_lint.py` to validate extension and preset catalog structure, paths, fixtures, profile IDs and registry language.
- Added GitHub/Copilot ecosystem files: path-specific Copilot instructions, PR template, issue templates, optional devcontainer, expanded Actions validation, and integration catalog entries.
- Added a read-only terminal demo command and walkthrough for the builder habit dashboard fixture.
- Added Continuous Specification Enforcement docs, scorecard, CLI tool, smoke example, and doctor integration.
- Updated public docs and contribution rules for controlled extension/preset contributions.
- No Git or ZIP actions are part of this release.

## 0.4.0

- Added the installable CLI wrapper through `sdc_cli` and the `sdc` console script.
- Promoted `README.md`, `MANIFESTO.md`, and `CONTRIBUTING.md` to English-first public entrypoints, with `.it.md` companions for the Italian versions.
- Added `integrations/catalog.json` and CLI discovery via `sdc integration list`.
- Expanded the benchmark harness from a single fixture to multiple domain-specific fixtures, including B2B leave management and internal PDF RAG evaluation.
- Added `python3 tools/sdc_harness.py run --all` and updated `make harness` to run every available fixture.
- Updated `doctor` to run all fixtures by default and added `doctor --quick` for the fixture-001 smoke path.
- Added `docs/25-english-public-index.md` for English-first public docs and Italian companion policy.
- Improved `sdc init` onboarding with positional project-name shorthand and clearer scaffold errors.
- No Git or ZIP actions are part of this release.

## 0.3.0

- Added `tools/sdc.py` command surface for command listing, prompt inspection, artifact manifest, branch naming, scaffold delegation, harness delegation and doctor checks.
- Added reproducible benchmark fixture harness with golden artifacts.
- Added raw-prompt vs Specification-Driven Coding case study.
- Extended scaffold output with raw request, intake and artifact manifest.
- Added Makefile and CI coverage for harness validation.
- Removed nominal dependency/framing around external specification toolkits; repository now presents an autonomous methodology and toolkit.

## 0.2.0

- Added Builder Ingestion Protocol.
- Added Vertical Blueprint Contracts.
- Added full-project, small-change, web, mobile, WordPress, RAG and multi-agent blueprints.
- Added scorecards for prompts, blueprints, implementation and multi-agent systems.
- Added model execution principles for assumptions, useful verbosity and evidence.
- Added blueprint scoring tool.

## 0.1.0

- Initial manifesto, project profiles, prompts, skills, agents and toolkit adapters.
