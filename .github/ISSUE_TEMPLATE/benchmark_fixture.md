# Benchmark Fixture Proposal

## Fixture ID

`000-domain-specific-name`

## Raw prompt

Paste the incomplete user request.

## Domain requirements

List the domain-specific concepts that must appear in intake, spec, blueprint, plan, tasks, and scorecard.

## Anti-genericity gates

What generic builder defaults must be rejected?

## Required validation

```bash
python3 tools/sdc_harness.py run --fixture <fixture-id>
python3 tools/sdc_harness.py run --all
```
