# Harness report: 001-builder-habit-dashboard

Generated: reproducible local harness run
Result: 19/19

| Check | Result | Detail |
|---|---:|---|
| fixture has raw-prompt.md | PASS | benchmarks/fixtures/001-builder-habit-dashboard/raw-prompt.md |
| fixture has sdc-prompt.md | PASS | benchmarks/fixtures/001-builder-habit-dashboard/sdc-prompt.md |
| fixture has expected.json | PASS | benchmarks/fixtures/001-builder-habit-dashboard/expected.json |
| sdc prompt is more constrained than raw prompt | PASS | raw=20 unique, sdc=167 unique |
| golden has intake.md | PASS | benchmarks/golden/001-builder-habit-dashboard/intake.md |
| golden has spec.md | PASS | benchmarks/golden/001-builder-habit-dashboard/spec.md |
| golden has blueprint.md | PASS | benchmarks/golden/001-builder-habit-dashboard/blueprint.md |
| golden has plan.md | PASS | benchmarks/golden/001-builder-habit-dashboard/plan.md |
| golden has tasks.md | PASS | benchmarks/golden/001-builder-habit-dashboard/tasks.md |
| golden has scorecard.md | PASS | benchmarks/golden/001-builder-habit-dashboard/scorecard.md |
| expected project_profile covered | PASS | covered |
| expected anti_genericity_constraints covered | PASS | covered |
| expected acceptance_criteria covered | PASS | covered |
| expected stack_rationale covered | PASS | covered |
| expected quality_gates covered | PASS | covered |
| scorecard includes anti-genericity | PASS | anti-genericity |
| scorecard includes domain fit | PASS | domain fit |
| scorecard includes risks | PASS | risks |
| scorecard includes next fixes | PASS | next fixes |

## Interpretation

This harness is structural and reproducible. It verifies fixture completeness, golden artifact coverage, and scorecard shape. It does not claim semantic product quality without human or agent review.
