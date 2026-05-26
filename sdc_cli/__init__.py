"""Installable CLI wrapper for Specification-Driven Coding."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _cwd_and_parents() -> list[Path]:
    try:
        cwd = Path.cwd().resolve()
    except OSError:
        return []
    return [cwd, *cwd.parents]


def _candidate_roots(cwd_roots: list[Path] | None = None) -> list[Path]:
    if cwd_roots is None:
        cwd_roots = _cwd_and_parents()
    roots = [Path(__file__).resolve().parents[1], *cwd_roots]
    seen: set[Path] = set()
    unique = []
    for root in roots:
        resolved = root.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def _is_embedded_sdc_cli(sdc_dir: Path, cli_path: Path) -> bool:
    return (
        cli_path.is_file()
        and (sdc_dir / "pyproject.toml").is_file()
        and (sdc_dir / "AGENTS.md").is_file()
    )


def _find_tools_cli() -> Path:
    cwd_roots = _cwd_and_parents()
    for root in cwd_roots:
        sdc_dir = root / ".sdc"
        embedded = sdc_dir / "tools" / "sdc.py"
        # Consumer projects should prefer their embedded SDC checkout when present.
        if _is_embedded_sdc_cli(sdc_dir, embedded):
            return embedded

    for root in _candidate_roots(cwd_roots):
        path = root / "tools" / "sdc.py"
        if path.is_file():
            return path
    raise RuntimeError(
        "Cannot locate tools/sdc.py. Run this command from a project containing `.sdc/tools/sdc.py`, "
        "from the spec-coding-manifesto repository root, or from an editable checkout installed with "
        "`pip install -e .`."
    )


def _load_tools_cli():
    path = _find_tools_cli()
    spec = importlib.util.spec_from_file_location("_sdc_tools_cli", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load CLI module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = _load_tools_cli()
    return int(module.main())
