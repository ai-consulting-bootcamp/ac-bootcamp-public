from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import List, Optional

from .analysis import analyze_target
from .generator import ensure_openai_credentials, generate_quiz_questions
from .linting import ensure_lint_tools
from .models import QuizArtifacts
from .naming import generate_quiz_name
from .quarto import write_and_render_quiz


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m codecheck")
    parser.add_argument("target", help="Python file to analyze.")
    parser.add_argument("-n", "--name", help="Quiz artifact name.")
    parser.add_argument(
        "--allow-unsafe-exec",
        action="store_true",
        help="Allow direct local execution when the sandbox is unavailable.",
    )
    return parser


def _check_prerequisites() -> List[str]:
    errors: List[str] = []
    if shutil.which("quarto") is None:
        errors.append("Quarto is required but was not found on PATH.")
    if not ensure_openai_credentials():
        errors.append("OPENAI_API_KEY is required.")
    missing_lint_tools = ensure_lint_tools()
    if missing_lint_tools:
        tools = ", ".join(missing_lint_tools)
        errors.append(f"Required lint tools are missing from PATH: {tools}.")
    return errors


def run(args: argparse.Namespace) -> QuizArtifacts:
    target_path = Path(args.target).expanduser().resolve()
    if not target_path.exists():
        raise SystemExit(f"Target file does not exist: {target_path}")
    if target_path.suffix != ".py":
        raise SystemExit(f"Target file must be a Python file: {target_path}")

    errors = _check_prerequisites()
    if errors:
        raise SystemExit("\n".join(errors))

    quiz_name = args.name or generate_quiz_name(target_path)
    analysis = analyze_target(
        target_path,
        allow_unsafe_exec=args.allow_unsafe_exec,
        python_executable=sys.executable,
    )
    questions = generate_quiz_questions(analysis, quiz_name)
    artifacts = write_and_render_quiz(
        quiz_name,
        target_path,
        questions,
        {candidate.candidate_id: candidate for candidate in analysis.candidates},
        output_dir=Path.cwd(),
    )
    print(artifacts.qmd_path)
    print(artifacts.html_path)
    return artifacts


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    run(args)
    return 0
