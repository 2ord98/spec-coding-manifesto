# Harness report: 004-compile-structural-validation

Generated: reproducible local harness run
Result: 33/33

| Check | Result | Detail |
|---|---:|---|
| expected has critical_sections_filled | PASS | critical_sections_filled |
| expected has has_default_marker | PASS | has_default_marker |
| expected has ask_count_min | PASS | ask_count_min |
| expected has assumption_count_min | PASS | assumption_count_min |
| expected has score_min | PASS | score_min |
| expected has required_sections | PASS | required_sections |
| expected has forbidden_empty_sections | PASS | forbidden_empty_sections |
| expected has default_marker_text | PASS | default_marker_text |
| fixture has raw-request.md | PASS | benchmarks/fixtures/004-compile-structural-validation/raw-request.md |
| fixture has expected.json | PASS | benchmarks/fixtures/004-compile-structural-validation/expected.json |
| golden has raw-request.md | PASS | benchmarks/golden/004-compile-structural-validation/raw-request.md |
| golden has intake.md | PASS | benchmarks/golden/004-compile-structural-validation/intake.md |
| golden has spec.md | PASS | benchmarks/golden/004-compile-structural-validation/spec.md |
| golden has project-profile.md | PASS | benchmarks/golden/004-compile-structural-validation/project-profile.md |
| golden has blueprint.md | PASS | benchmarks/golden/004-compile-structural-validation/blueprint.md |
| golden has plan.md | PASS | benchmarks/golden/004-compile-structural-validation/plan.md |
| golden has tasks.md | PASS | benchmarks/golden/004-compile-structural-validation/tasks.md |
| golden has scorecard.md | PASS | benchmarks/golden/004-compile-structural-validation/scorecard.md |
| golden has artifact-manifest.json | PASS | benchmarks/golden/004-compile-structural-validation/artifact-manifest.json |
| compile command exits 0 | PASS | exit 0 |
| compile output is JSON | PASS | parsed |
| required sections present | PASS | covered |
| forbidden empty sections | PASS | none |
| default marker present | PASS | [DEFAULT — review and override if needed] |
| DecisionAssertion passes | PASS | {"ask_count": 21, "assumption_count": 15, "critical_section_filled": true, "has_default_marker": true, "passes": true, "score_min": 80} |
| ask threshold | PASS | 21 |
| assumption threshold | PASS | 15 |
| security baseline included | PASS | Security Baseline |
| performance budget included | PASS | startup_or_first_response |
| testing contract included | PASS | Testing Contract |
| scorecard exists | PASS | scorecard.md |
| blueprint score threshold | PASS | 100/100 |
| json includes assertion report | PASS | assertion |

## Interpretation

This harness is structural and reproducible. It verifies fixture completeness, golden artifact coverage, and scorecard shape. It does not claim semantic product quality without human or agent review.
