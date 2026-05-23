# Case study: raw prompt vs Specification-Driven Coding builder prompt

## Purpose

Show a reproducible comparison between a vague builder prompt and a Specification-Driven Coding artifact package without relying on paid external tools.

## Scenario

Build a lightweight habit tracking dashboard for solo users.

## Inputs

- Raw prompt: `benchmarks/fixtures/001-builder-habit-dashboard/raw-prompt.md`
- Specification-Driven Coding prompt: `benchmarks/fixtures/001-builder-habit-dashboard/sdc-prompt.md`
- Golden artifacts: `benchmarks/golden/001-builder-habit-dashboard/`

## Execution conditions

- Same builder or coding agent for both runs.
- Same timebox.
- No paid services unless explicitly required by the prompt.
- No hidden evaluator.
- Score both outputs with the same rubric.

## Expected difference

The raw prompt is intentionally underspecified. It is likely to produce a generic dashboard, unclear persistence, weak privacy posture, and untested empty/error states.

The Specification-Driven Coding prompt constrains domain, user, non-goals, stack rationale, privacy, UX states, acceptance criteria, and scorecard output before implementation.

## Replit/MCP note

Replit offers an MCP server for creating apps from prompts, but it requires OAuth and a Replit account. This repo therefore ships a local reproducible harness first. A manual Replit run can use the same two prompt files and record outputs in this case study.

## Rubric

| Area | Weight | Raw expected risk | SDC expected improvement |
|---|---:|---|---|
| Intent clarity | 10 | Vague habit tracking goal | User, domain, and non-goals explicit |
| Requirement coverage | 15 | Missing edit/delete/error details | Acceptance criteria define workflows |
| Non-goals respected | 10 | May add social/auth defaults | Social/auth/analytics constrained |
| Stack rationale | 10 | May choose heavy default stack | Local-first rationale required |
| Security/privacy | 15 | Habit sensitivity may be ignored | Sensitive local data constraint |
| UX/error states | 10 | Generic cards and happy path | Empty/error/undo states required |
| Testability | 10 | Few verifiable checks | Explicit scorecard and acceptance |
| Anti-genericity | 10 | Dashboard clone risk | Domain-specific constraints |
| Maintainability | 5 | Architecture may be implicit | Artifact chain preserves intent |
| Reproducibility | 5 | Prompt alone is hard to audit | Fixture/golden harness is repeatable |

## Local validation

```bash
python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard
```

## Limitation

This case study proves reproducible artifact discipline, not universal product superiority. Real builder comparisons must attach raw and SDC outputs produced by the same tool under the same conditions.
