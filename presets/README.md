# Presets

The presets registry lists ready operational bundles for common Specification-Driven Coding usage modes.

Presets are discovery metadata only. They are not auto-applied, installed, fetched remotely, or materialized by the CLI.

## Catalog

- `catalog.json`: machine-readable list of core preset bundles.

Each preset points to existing project profiles, blueprints, prompts, scorecards, fixtures, and quality gates. Future contributors can propose new presets through `CONTRIBUTING.md`.

## Usage

```bash
python3 tools/sdc.py preset list
python3 tools/sdc.py preset list --format json
```

Use a preset to decide which repository files to load manually for a workflow. It is not a marketplace, package manager, or installer.
