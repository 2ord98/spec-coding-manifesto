# Demo Walkthrough: 001 Builder Habit Dashboard

## Purpose

Show, in under 30 seconds from the terminal, why Specification-Driven Coding changes the quality of an AI-builder request before any app is generated.

## Raw Prompt

Source: `benchmarks/fixtures/001-builder-habit-dashboard/raw-prompt.md`

```text
Build a small app where people can track habits and see progress. Make it clean and easy to use.
```

## Risk Of Generic Builder Output

The raw prompt is useful but underspecified. A builder can satisfy it with a generic dashboard, generic cards, generic progress bars, unnecessary accounts, default backend services, social streak mechanics, or placeholder copy.

None of those choices are malicious. They are typical defaults when intent is incomplete.

## Specification-Driven Coding Transformation

Source: `benchmarks/fixtures/001-builder-habit-dashboard/sdc-prompt.md`

The Specification-Driven Coding prompt converts the vague request into:

- a `full-project` mode;
- primary project profile `dashboard-admin-bi`;
- solo-user habit tracking domain;
- non-goals such as no social sharing, no leaderboard, no paid analytics, and no automatic health advice;
- local-first stack preference;
- privacy and security constraints for sensitive routine data;
- acceptance criteria for create, complete, edit, delete, weekly progress, explicit states, and scorecard output.

## Artifact Chain

The fixture uses the official pipeline:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Artifacts:

- `benchmarks/golden/001-builder-habit-dashboard/intake.md`
- `benchmarks/golden/001-builder-habit-dashboard/spec.md`
- `benchmarks/golden/001-builder-habit-dashboard/blueprint.md`
- `benchmarks/golden/001-builder-habit-dashboard/plan.md`
- `benchmarks/golden/001-builder-habit-dashboard/tasks.md`
- `benchmarks/golden/001-builder-habit-dashboard/scorecard.md`

## Vertical Blueprint

The Vertical Blueprint narrows the build:

- local-first frontend with browser storage or equivalent local persistence;
- no silent auth, social, analytics, or cloud persistence;
- habit model with name, cadence, completions, created timestamp, and archived flag;
- views for today, weekly progress, habit editor, and empty/error fallback;
- privacy gate, testability gate, and anti-genericity gate.

## Plan And Tasks

The plan slices the work into domain model, core workflow, progress view, states/recovery, and validation. The task list contains 10 concrete implementation tasks, including local storage, today view, habit editing, weekly progress, undo/reset, keyboard navigation, privacy note, and scorecard review.

## Final Scorecard

Source: `benchmarks/golden/001-builder-habit-dashboard/scorecard.md`

The scorecard returns a passing benchmark gate and evaluates spec adherence, anti-genericity, domain fit, architecture, privacy, performance, testability, risks, and next fixes.

## What This Proves

This demo proves reproducible artifact discipline and anti-genericity constraints.

It shows that the same raw prompt can be transformed into a more specific execution contract before code or app generation starts.

## What This Does Not Prove

It does not prove universal product superiority without real builder comparison.

It does not prove semantic quality of a finished app.

It does not call an LLM, generate code, deploy software, or replace human review.

## Run

```bash
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard --verbose
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard --format json
```
