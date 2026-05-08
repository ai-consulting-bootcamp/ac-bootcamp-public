from pathlib import Path

import pytest

from codecheck import cli
from codecheck.models import AnalysisResult, Candidate, QuizArtifacts, QuizQuestion


def _candidate(candidate_id: str, line_start: int) -> Candidate:
    return Candidate(
        candidate_id=candidate_id,
        category="function",
        prompt="Explain this code.",
        evidence="evidence",
        snippet="def sample():\n    return 1",
        line_start=line_start,
        line_end=line_start + 1,
        priority=10,
    )


def _questions(candidate_ids):
    questions = []
    for index, candidate_id in enumerate(candidate_ids):
        question_type = "mcq" if index % 2 == 0 else "short-answer"
        choices = ["A", "B", "C", "D"] if question_type == "mcq" else []
        questions.append(
            QuizQuestion(
                question_type=question_type,
                prompt="Question {0}".format(index),
                answer="Answer {0}".format(index),
                explanation="Explanation {0}".format(index),
                candidate_id=candidate_id,
                choices=choices,
            )
        )
    return questions


def test_build_parser_parses_flags():
    parser = cli.build_parser()
    args = parser.parse_args(["script.py", "-n", "quiz1", "--allow-unsafe-exec"])
    assert args.target == "script.py"
    assert args.name == "quiz1"
    assert args.allow_unsafe_exec is True


def test_run_rejects_missing_target():
    parser = cli.build_parser()
    args = parser.parse_args(["does-not-exist.py"])
    with pytest.raises(SystemExit) as exc_info:
        cli.run(args)
    assert "does not exist" in str(exc_info.value)


def test_run_generates_random_name_when_missing(monkeypatch, tmp_path):
    target = tmp_path / "example.py"
    target.write_text("print('ok')\n", encoding="utf-8")
    analysis = AnalysisResult(target_path=target, source=target.read_text(), candidates=[_candidate("c1", 1)] * 10, execution_result=None)

    monkeypatch.setattr(cli, "_check_prerequisites", lambda: [])
    monkeypatch.setattr(cli, "generate_quiz_name", lambda path: "generated-name")
    monkeypatch.setattr(cli, "analyze_target", lambda *args, **kwargs: analysis)
    monkeypatch.setattr(cli, "generate_quiz_questions", lambda *args, **kwargs: _questions(["c1"] * 10))

    captured = {}

    def fake_render(name, target_path, questions, candidate_map, output_dir):
        captured["name"] = name
        assert output_dir == Path.cwd()
        return QuizArtifacts(name=name, qmd_path=output_dir / "{0}.qmd".format(name), html_path=output_dir / "{0}.html".format(name))

    monkeypatch.setattr(cli, "write_and_render_quiz", fake_render)

    args = cli.build_parser().parse_args([str(target)])
    cli.run(args)
    assert captured["name"] == "generated-name"
