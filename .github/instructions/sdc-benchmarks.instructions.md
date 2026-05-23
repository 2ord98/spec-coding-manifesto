---
applyTo: "benchmarks/**/*.md,benchmarks/**/*.json,case-studies/**/*.md"
---

# Benchmark Instructions

Use Specification-Driven Coding benchmark discipline.

Fixtures must include `raw-prompt.md`, `sdc-prompt.md`, `expected.json`, and matching golden artifacts.

Keep benchmarks structural and reproducible. Do not claim semantic proof of product quality.

Every fixture must strengthen anti-genericity, domain specificity, acceptance criteria, quality gates, and scorecard reporting.

Validate with `python3 tools/sdc_harness.py run --fixture <fixture-id>` or `python3 tools/sdc_harness.py run --all`.
