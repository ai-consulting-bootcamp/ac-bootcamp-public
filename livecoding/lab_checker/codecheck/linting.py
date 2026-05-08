from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

from .models import Candidate


def ensure_lint_tools() -> List[str]:
    missing: List[str] = []
    for tool in ("ruff", "pylint"):
        if not shutil.which(tool):
            missing.append(tool)
    return missing


def _priority_for_severity(severity: str) -> int:
    order = {
        "fatal": 100,
        "error": 90,
        "warning": 70,
        "refactor": 50,
        "convention": 40,
        "info": 30,
    }
    return order.get(severity.lower(), 20)


def dedupe_lint_findings(candidates: List[Candidate]) -> List[Candidate]:
    unique: Dict[Tuple[str, str, str], Candidate] = {}
    for candidate in candidates:
        key = (
            candidate.line_ref,
            candidate.metadata.get("code", ""),
            candidate.evidence.lower(),
        )
        current = unique.get(key)
        if current is None or candidate.priority > current.priority:
            unique[key] = candidate
    return sorted(unique.values(), key=lambda item: (-item.priority, item.line_start or 0, item.candidate_id))


def _extract_snippet(source_lines: List[str], line: int, context: int = 2) -> Tuple[str, int, int]:
    start = max(1, line - context)
    end = min(len(source_lines), line + context)
    snippet = "\n".join(source_lines[start - 1 : end]).rstrip()
    return snippet, start, end


def _run_json_command(command: List[str]) -> List[dict]:
    completed = subprocess.run(command, capture_output=True, text=True)
    if not completed.stdout.strip():
        return []
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return []
    if isinstance(payload, list):
        return payload
    return []


def collect_lint_candidates(target_path: Path, source: str) -> List[Candidate]:
    lines = source.splitlines()
    findings: List[Candidate] = []

    for item in _run_json_command(["ruff", "check", "--output-format", "json", str(target_path)]):
        location = item.get("location") or {}
        line = int(location.get("row") or 1)
        snippet, start, end = _extract_snippet(lines, line)
        code = item.get("code") or "ruff"
        message = item.get("message") or "Ruff finding"
        findings.append(
            Candidate(
                candidate_id=f"ruff-{code.lower()}-{line}",
                category="lint",
                prompt=f"Identify and explain the improvement highlighted by Ruff ({code}).",
                evidence=message,
                snippet=snippet,
                line_start=start,
                line_end=end,
                priority=80,
                metadata={"tool": "ruff", "code": code},
            )
        )

    for item in _run_json_command(["pylint", "--output-format=json", str(target_path)]):
        line = int(item.get("line") or 1)
        snippet, start, end = _extract_snippet(lines, line)
        severity = item.get("type") or "warning"
        code = item.get("message-id") or item.get("symbol") or "pylint"
        message = item.get("message") or "Pylint finding"
        findings.append(
            Candidate(
                candidate_id=f"pylint-{code.lower()}-{line}",
                category="lint",
                prompt=f"Explain the code-quality issue reported by Pylint ({code}).",
                evidence=message,
                snippet=snippet,
                line_start=start,
                line_end=end,
                priority=_priority_for_severity(severity),
                metadata={"tool": "pylint", "code": code, "severity": severity},
            )
        )

    return dedupe_lint_findings(findings)
