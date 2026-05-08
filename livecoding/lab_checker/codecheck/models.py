from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Candidate:
    candidate_id: str
    category: str
    prompt: str
    evidence: str
    snippet: str
    line_start: Optional[int]
    line_end: Optional[int]
    priority: int = 0
    execution_required: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def line_ref(self) -> str:
        if self.line_start is None:
            return "n/a"
        if self.line_end in (None, self.line_start):
            return str(self.line_start)
        return f"{self.line_start}-{self.line_end}"

    def to_prompt_dict(self) -> Dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "category": self.category,
            "prompt": self.prompt,
            "evidence": self.evidence,
            "line_ref": self.line_ref,
            "snippet": self.snippet,
            "priority": self.priority,
            "execution_required": self.execution_required,
            "metadata": self.metadata,
        }


@dataclass
class ExecutionResult:
    mode: str
    available: bool
    command: List[str]
    returncode: Optional[int]
    stdout: str
    stderr: str
    reason: str = ""


@dataclass
class AnalysisResult:
    target_path: Path
    source: str
    candidates: List[Candidate]
    execution_result: Optional[ExecutionResult]


@dataclass
class QuizQuestion:
    question_type: str
    prompt: str
    answer: str
    explanation: str
    candidate_id: str
    choices: List[str] = field(default_factory=list)


@dataclass
class QuizArtifacts:
    name: str
    qmd_path: Path
    html_path: Path
