"""Stdlib-only typed contracts for Specification-Driven Coding compile/handoff.

These dataclasses are DSPy-inspired structural contracts, not a DSPy dependency.
They do not call models, read files, write files, or assume repository paths.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ProfileSignature:
    """Input/output contract for a project profile module."""

    # Input space
    raw_request: str
    profile_id: str
    workspace_path: Path

    # Output space
    decision_matrix: list = field(default_factory=list)
    open_questions: list = field(default_factory=list)
    assumptions: list = field(default_factory=list)
    scorecard_target: Optional[str] = None

    def input_space(self) -> dict:
        return {
            "raw_request": self.raw_request,
            "profile_id": self.profile_id,
            "workspace_path": str(self.workspace_path),
        }

    def output_space(self) -> dict:
        return {
            "decision_matrix": self.decision_matrix,
            "open_questions": self.open_questions,
            "assumptions": self.assumptions,
            "scorecard_target": self.scorecard_target,
        }


@dataclass
class RolePromptSignature:
    """Input/output contract for a role-prompt assembly."""

    # Input space
    workspace_state: dict
    scope: str
    target_cli: str

    # Output space
    compiled_prompt: str = ""
    attachments: list = field(default_factory=list)
    target_instructions: str = ""

    def input_space(self) -> dict:
        return {
            "workspace_state": self.workspace_state,
            "scope": self.scope,
            "target_cli": self.target_cli,
        }

    def output_space(self) -> dict:
        return {
            "compiled_prompt": self.compiled_prompt,
            "attachments": self.attachments,
            "target_instructions": self.target_instructions,
        }


@dataclass
class DecisionAssertion:
    """DSPy-style assertion: validates output of compile against metric gates."""

    critical_section_filled: bool = False
    has_default_marker: bool = False
    ask_count: int = 0
    assumption_count: int = 0
    score_min: int = 80

    def passes(self) -> bool:
        return (
            self.critical_section_filled
            and self.has_default_marker
            and self.ask_count >= 3
            and self.assumption_count >= 2
        )

    def report(self) -> dict:
        return {
            "critical_section_filled": self.critical_section_filled,
            "has_default_marker": self.has_default_marker,
            "ask_count": self.ask_count,
            "assumption_count": self.assumption_count,
            "score_min": self.score_min,
            "passes": self.passes(),
        }
