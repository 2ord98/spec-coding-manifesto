---
applyTo: "tools/**/*.py,sdc_cli/**/*.py"
---

# Python CLI Instructions

Use Specification-Driven Coding as the repository method.

Use Python stdlib only. Do not add runtime dependencies.

Keep `tools/sdc.py` as a thin navigation, discovery, scaffold, harness, and validation surface. It must not generate complete products or bypass artifact gates.

Preserve direct script usage and installable CLI usage.

After CLI changes, run `python3 tools/spec_lint.py`, `python3 tools/sdc.py doctor --quick`, and the specific command being changed.

Do not add install/apply/fetch behavior for extensions or presets.
