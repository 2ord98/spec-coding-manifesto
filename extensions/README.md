# Extensions

The extensions registry lists optional, internal modules that extend Specification-Driven Coding.

Extensions are discoverable metadata only. They are not auto-installed, fetched remotely, materialized into projects, or applied by the CLI.

## Catalog

- `catalog.json`: machine-readable list of core/internal extension examples.

The catalog starts with repository-owned examples only. External extensions may be proposed later through `CONTRIBUTING.md`, but every proposal must preserve anti-genericity, scorecards, security, and the official pipeline:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

## Usage

```bash
python3 tools/sdc.py extension list
python3 tools/sdc.py extension list --format json
```

Use the catalog to decide which files to load manually for a specific workflow. It is not a marketplace, package manager, or installer.
