# End-To-End Walkthrough

## Purpose

Show how Specification-Driven Coding converts a vague raw prompt into a structured artifact chain and scorecard without generating a real app.

## Raw Prompt

Fixture: `benchmarks/fixtures/001-builder-habit-dashboard`

```text
Build a small app where people can track habits and see progress. Make it clean and easy to use.
```

## Specification-Driven Coding Prompt Summary

The Specification-Driven Coding version adds a full-project mode, `dashboard-admin-bi` project profile, solo-user domain, local-first stack preference, non-goals, privacy constraints, anti-genericity constraints, acceptance criteria, and scorecard requirement.

## Artifact Chain

Official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

The fixture maps this into:

- `benchmarks/golden/001-builder-habit-dashboard/intake.md`
- `benchmarks/golden/001-builder-habit-dashboard/spec.md`
- `benchmarks/golden/001-builder-habit-dashboard/blueprint.md`
- `benchmarks/golden/001-builder-habit-dashboard/plan.md`
- `benchmarks/golden/001-builder-habit-dashboard/tasks.md`
- `benchmarks/golden/001-builder-habit-dashboard/scorecard.md`

## Difference From The Raw Prompt

The raw prompt asks for a clean habit app. The artifact chain forces decisions about:

- project profile;
- local-first stack rationale;
- rejected backend defaults;
- non-goals;
- sensitive personal routine data;
- concrete habit workflows;
- acceptance criteria;
- scorecard risks.

## Run The Demo

```bash
python3 tools/sdc_demo.py list
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard --format markdown
sdc demo run --fixture 001-builder-habit-dashboard
```

## Run The Harness

```bash
python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_harness.py run --all
```

## Run Continuous Enforcement

```bash
python3 tools/sdc_enforce.py check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
```

## Honest Limitation

This walkthrough proves artifact discipline and anti-genericity checks. It does not prove universal product superiority without real builder comparison, real implementation, tests, and human review.
