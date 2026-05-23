# Demos

## Purpose

This directory contains short, reproducible walkthroughs that show how Specification-Driven Coding turns a raw request into an artifact chain.

## Try It

```bash
python3 tools/sdc_demo.py list
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard --verbose
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard --format json
```

Installed or delegated CLI:

```bash
sdc demo run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli demo run --fixture 001-builder-habit-dashboard
```

## Official Pipeline

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

## Scope

These demos read existing files from `benchmarks/fixtures/` and `benchmarks/golden/`. They do not generate a real app, call external APIs, require an LLM, or prove semantic product superiority.

Primary demo fixture: `benchmarks/fixtures/001-builder-habit-dashboard`.

This demo proves reproducible artifact discipline and anti-genericity constraints. It does not prove universal product superiority without real builder comparison.

## Current Walkthroughs

- [001 builder habit dashboard](001-builder-habit-dashboard-walkthrough.md)
