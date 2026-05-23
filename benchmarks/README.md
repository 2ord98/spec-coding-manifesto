# Benchmarks

## Purpose

This directory contains reproducible fixtures for checking whether Specification-Driven Coding artifacts preserve the official pipeline and anti-genericity constraints.

## Structure

- `fixtures/`: raw prompt, Specification-Driven Coding prompt, and expected contract fields.
- `golden/`: expected intake, specification, blueprint, plan, tasks, and scorecard artifacts.
- `reports/`: harness output written by `tools/sdc_harness.py`.

## Run

```bash
python3 tools/sdc_demo.py list
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_harness.py list
python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_harness.py run --fixture 002-b2b-leave-management
python3 tools/sdc_harness.py run --fixture 003-internal-pdf-rag-assistant
python3 tools/sdc_harness.py run --all
make harness
```

## Scope

The harness is structural and reproducible. It is useful as a gate, not as proof that any generated product is semantically superior.

The demo is explanatory and read-only. It shows the raw prompt -> artifact chain using existing fixture and golden files. It does not run the harness, generate a product, call external APIs, or require an LLM.

## Current fixtures

- `001-builder-habit-dashboard`: local-first private habit dashboard benchmark.
- `002-b2b-leave-management`: B2B leave management workflow with approval, calendar visibility, audit, and privacy constraints.
- `003-internal-pdf-rag-assistant`: internal PDF knowledge assistant with retrieval, citation, refusal, and access-control constraints.
