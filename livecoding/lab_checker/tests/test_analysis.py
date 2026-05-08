from pathlib import Path

from codecheck.analysis import analyze_target
from codecheck.models import Candidate, ExecutionResult


FIXTURES = Path(__file__).parent / "fixtures"


def test_analyze_target_emits_syntax_diagnostic():
    result = analyze_target(
        FIXTURES / "syntax_error.py",
        allow_unsafe_exec=False,
        python_executable="python",
    )
    candidate_ids = [candidate.candidate_id for candidate in result.candidates]
    assert "syntax-error" in candidate_ids
    syntax_candidate = next(candidate for candidate in result.candidates if candidate.candidate_id == "syntax-error")
    assert syntax_candidate.line_start == 1
    assert "def broken" in syntax_candidate.snippet


def test_analyze_target_collects_structure_and_line_refs(monkeypatch):
    monkeypatch.setattr("codecheck.analysis.collect_lint_candidates", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        "codecheck.analysis.execute_target",
        lambda *args, **kwargs: ExecutionResult(
            mode="sandboxed",
            available=True,
            command=["python"],
            returncode=0,
            stdout="5.0",
            stderr="",
        ),
    )

    result = analyze_target(
        FIXTURES / "sample_valid.py",
        allow_unsafe_exec=False,
        python_executable="python",
    )

    candidate_ids = [candidate.candidate_id for candidate in result.candidates]
    assert "module-summary" in candidate_ids
    assert "function-square" in candidate_ids
    assert "function-hypotenuse" in candidate_ids
    square = next(candidate for candidate in result.candidates if candidate.candidate_id == "function-square")
    assert square.line_start == 7
    assert square.line_end >= square.line_start
    assert "raise ValueError" in square.snippet


def test_analyze_target_turns_execution_failure_into_diagnostic(monkeypatch):
    monkeypatch.setattr("codecheck.analysis.collect_lint_candidates", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        "codecheck.analysis.execute_target",
        lambda *args, **kwargs: ExecutionResult(
            mode="sandboxed",
            available=True,
            command=["python"],
            returncode=1,
            stdout="",
            stderr="RuntimeError: boom",
        ),
    )

    result = analyze_target(
        FIXTURES / "sample_valid.py",
        allow_unsafe_exec=False,
        python_executable="python",
    )
    diagnostic = next(candidate for candidate in result.candidates if candidate.candidate_id == "execution-failure")
    assert "RuntimeError: boom" in diagnostic.evidence


def test_analyze_target_turns_missing_dependency_failure_into_diagnostic(monkeypatch, tmp_path):
    target = tmp_path / "missing_dep.py"
    target.write_text("import totally_missing_package\n", encoding="utf-8")
    monkeypatch.setattr("codecheck.analysis.collect_lint_candidates", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        "codecheck.analysis.execute_target",
        lambda *args, **kwargs: ExecutionResult(
            mode="sandboxed",
            available=True,
            command=["python"],
            returncode=1,
            stdout="",
            stderr="ModuleNotFoundError: No module named 'totally_missing_package'",
        ),
    )

    result = analyze_target(target, allow_unsafe_exec=False, python_executable="python")
    diagnostic = next(candidate for candidate in result.candidates if candidate.candidate_id == "execution-failure")
    assert "ModuleNotFoundError" in diagnostic.evidence
