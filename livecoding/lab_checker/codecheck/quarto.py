from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Dict, List

from .models import Candidate, QuizArtifacts, QuizQuestion


def _render_choice_block(choices: List[str]) -> str:
    if not choices:
        return ""
    return "\n".join(f"- {choice}" for choice in choices)


def build_qmd(
    quiz_name: str, target_path: Path, questions: List[QuizQuestion], candidate_map: Dict[str, Candidate]
) -> str:
    parts = [
        "---",
        f"title: \"{quiz_name}\"",
        "format:",
        "  revealjs:",
        "    theme: simple",
        "slide-number: true",
        "execute:",
        "  enabled: false",
        "---",
        "",
    ]

    for index, question in enumerate(questions, start=1):
        candidate = candidate_map[question.candidate_id]
        parts.extend(
            [
                f"## Question {index}",
                "",
                f"**Type:** {question.question_type}",
                "",
                question.prompt,
                "",
                f"**Lines:** {candidate.line_ref}",
                "",
                "```python",
                candidate.snippet,
                "```",
                "",
            ]
        )
        choice_block = _render_choice_block(question.choices)
        if choice_block:
            parts.extend([choice_block, ""])
        parts.extend(
            [
                "---",
                "",
                f"## Answer {index}",
                "",
                f"**Correct answer:** {question.answer}",
                "",
                question.explanation,
                "",
                f"**Source:** `{target_path.name}` lines {candidate.line_ref}",
                "",
                "---",
                "",
            ]
        )

    return "\n".join(parts).rstrip() + "\n"


def write_and_render_quiz(
    quiz_name: str,
    target_path: Path,
    questions: List[QuizQuestion],
    candidate_map: Dict[str, Candidate],
    *,
    output_dir: Path,
) -> QuizArtifacts:
    qmd_path = output_dir / f"{quiz_name}.qmd"
    html_path = output_dir / f"{quiz_name}.html"
    qmd_path.write_text(build_qmd(quiz_name, target_path, questions, candidate_map), encoding="utf-8")
    quarto_home = output_dir / ".quarto-home"
    cache_dir = quarto_home / "cache"
    data_dir = quarto_home / "data"
    config_dir = quarto_home / "config"
    for directory in (cache_dir, data_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["HOME"] = str(quarto_home)
    env["XDG_CACHE_HOME"] = str(cache_dir)
    env["XDG_DATA_HOME"] = str(data_dir)
    env["XDG_CONFIG_HOME"] = str(config_dir)
    subprocess.run(
        ["quarto", "render", str(qmd_path), "--to", "revealjs", "--output", html_path.name],
        cwd=output_dir,
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )
    return QuizArtifacts(name=quiz_name, qmd_path=qmd_path, html_path=html_path)
