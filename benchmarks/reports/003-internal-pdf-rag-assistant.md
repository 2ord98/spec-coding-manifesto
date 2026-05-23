# Harness report: 003-internal-pdf-rag-assistant

Generated: reproducible local harness run
Result: 19/19

| Check | Result | Detail |
|---|---:|---|
| fixture has raw-prompt.md | PASS | benchmarks/fixtures/003-internal-pdf-rag-assistant/raw-prompt.md |
| fixture has sdc-prompt.md | PASS | benchmarks/fixtures/003-internal-pdf-rag-assistant/sdc-prompt.md |
| fixture has expected.json | PASS | benchmarks/fixtures/003-internal-pdf-rag-assistant/expected.json |
| sdc prompt is more constrained than raw prompt | PASS | raw=23 unique, sdc=192 unique |
| golden has intake.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/intake.md |
| golden has spec.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/spec.md |
| golden has blueprint.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/blueprint.md |
| golden has plan.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/plan.md |
| golden has tasks.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/tasks.md |
| golden has scorecard.md | PASS | benchmarks/golden/003-internal-pdf-rag-assistant/scorecard.md |
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
