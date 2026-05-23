# Continuous Specification Enforcement

## Purpose

Continuous Specification Enforcement keeps Specification-Driven Coding from becoming a one-time planning ritual. The specification, Vertical Blueprint, plan, tasks, implementation notes, exceptions, and scorecard remain a living contract while the project evolves.

Static specs are insufficient because implementation often changes scope, stack, data shape, UX, privacy behavior, or acceptance criteria after the first plan. Silent divergence turns specification-first work back into vibe coding.

## When To Use

Use enforcement:

- before implementation starts;
- after each meaningful implementation slice;
- before release;
- when code, tasks, or scorecards change;
- when an agent discovers that the contract is wrong or incomplete.

## Inputs

- `spec.md`
- `blueprint.md`
- `plan.md`
- `tasks.md`
- `scorecard.md`
- optional `intake.md`
- optional `artifact-manifest.json`
- optional `implementation-notes.md`
- optional `exceptions.md`
- implementation files when present

## Outputs

- PASS/WARN/FAIL structural enforcement result;
- 0-100 enforcement score;
- divergence list;
- required decision for each unresolved divergence;
- optional enforcement report.

## Divergence Types

- requirement drift;
- architecture drift;
- stack drift;
- data model drift;
- security/privacy drift;
- UX/domain drift;
- performance/fallback drift;
- test/acceptance drift;
- undocumented implementation drift.

## Decision Protocol

When divergence appears, the agent must:

1. Identify the divergence.
2. Classify severity.
3. Choose one allowed decision:
   - update specification;
   - update Vertical Blueprint;
   - fix implementation/artifact;
   - accept documented exception.
4. Record the reason.
5. Rerun the scorecard.
6. Block release if the divergence remains unresolved.

No silent divergence is allowed.

## Acceptance Gate

Release is allowed only when:

- required artifacts exist;
- plan, tasks, and scorecard structurally align with spec and blueprint;
- assumptions and non-goals remain visible;
- security/privacy and anti-genericity constraints are not bypassed;
- scorecard is fresh enough for the implementation state;
- every exception is documented.

## Tool Usage

```bash
python3 tools/sdc_enforce.py check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc_enforce.py check --path benchmarks/golden/001-builder-habit-dashboard --format json
python3 tools/sdc_enforce.py check --workspace examples/enforcement-smoke
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
```

## Limitations

The current tool is a structural enforcement gate. It checks artifact presence, term coverage, timestamps, task markers, and freshness risks. It does not prove true semantic correctness, product quality, code safety, or full requirement satisfaction.

Semantic review still requires human judgment, domain review, tests, and scorecards.
