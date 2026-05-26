# Compile Engine Specification

## Purpose

Define `sdc compile` as a deterministic decision contract compiler for Specification-Driven Coding.

`sdc compile` lowers a raw request and profile-depth package into denser SDC artifacts. It does not generate application code, call models, select a final stack as an oracle, or replace engineering judgment.

## When to use

Use compile after `sdc init` has created a workspace and before asking a coding agent or builder to implement.

## Command contract

```bash
python3 tools/sdc.py compile --workspace <path>
python3 tools/sdc.py compile --workspace <path> --dry-run
python3 tools/sdc.py compile --workspace <path> --format json
python3 tools/sdc.py compile --workspace <path> --strict
python3 tools/sdc.py compile --workspace <path> --force
```

## Input signature

- `raw_request: str`
- `profile_metadata: ProjectProfileDepth`
- `workspace_path: Path`

## Output signature

- `intake.md`
- `spec.md`
- `blueprint.md`
- `plan.md`
- `tasks.md`
- `scorecard.md`
- `open_questions: list[str]`
- `assumptions: list[str]`
- `decision_matrix: list[Decision]`

## Artifact write policy

Default write behavior is conservative:

- write only empty or placeholder-only sections;
- preserve user-written non-placeholder content;
- never erase user-written content without `--force`;
- if a critical section cannot be resolved deterministically, write `[ASK: ...]` or `[ASSUMPTION: ...]`;
- never leave a critical section blank.

`--force` may overwrite scaffold/generated sections.

`--dry-run` prints the compile summary and writes nothing.

## Placeholder detection

A section is placeholder-only when it contains only heading text, scaffold labels, bullets without values, `[TITLE]`, empty tables, or generic scaffold fragments.

Non-placeholder content is preserved unless `--force` is passed.

## Section replacement policy

Compile may replace a complete artifact only when the file is scaffold-like or when `--force` is passed. Otherwise it should fill missing sections or append a compile-generated section without removing human content.

## `[ASK]` vs `[ASSUMPTION]`

Use `[ASK: ...]` for high-impact unknowns about scope, data, security, privacy, deployment, integration, or product behavior.

Use `[ASSUMPTION: ...]` for reversible defaults that allow planning to continue without pretending certainty.

## Strict mode

`--strict` fails when:

- more than 5 `[ASK]` questions are generated;
- a `DecisionAssertion` fails;
- required artifacts or profile-depth files are missing;
- critical sections are blank.

## No dependency rule

Compile is stdlib-only:

- no LLM calls;
- no API calls;
- no DSPy import;
- no external dependencies.

## Structural contracts

Compile uses `tools/sdc_signature.py`:

- `ProfileSignature` captures input/output spaces.
- `DecisionAssertion` checks that critical sections are filled, the default marker exists, and enough explicit uncertainty is surfaced.

This is DSPy-inspired, not DSPy-dependent.

## Quality gate

Compile passes only when artifacts become decision-bounded and non-skeletal without claiming semantic product correctness.

## Next artifact

The next planned phase is handoff: converting the compiled artifact chain into target-agent instructions without modifying files.
