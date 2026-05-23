"""Installable CLI wrapper for Specification-Driven Coding."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _candidate_roots() -> list[Path]:
    roots = [Path(__file__).resolve().parents[1], Path.cwd()]
    roots.extend(Path.cwd().parents)
    seen: set[Path] = set()
    unique = []
    for root in roots:
        resolved = root.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def _find_tools_cli() -> Path:
    for root in _candidate_roots():
        path = root / "tools" / "sdc.py"
        if path.exists():
            return path
    raise RuntimeError(
        "Cannot locate tools/sdc.py. Run this command from the spec-coding-manifesto repository root "
        "or install the repository in editable mode with `pip install -e .`."
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
