from pathlib import Path

from codecheck.models import Candidate, QuizQuestion
from codecheck.quarto import build_qmd, write_and_render_quiz


def _candidate_map():
    return {
        "shared": Candidate(
            candidate_id="shared",
            category="function",
            prompt="Explain this code.",
            evidence="evidence",
            snippet="def sample():\n    return 1",
            line_start=1,
            line_end=2,
            priority=10,
        )
    }


def _questions():
    questions = []
    for index in range(10):
        question_type = "mcq" if index < 5 else "short-answer"
        questions.append(
            QuizQuestion(
                question_type=question_type,
                prompt="Question {0}".format(index + 1),
                answer="Answer {0}".format(index + 1),
                explanation="Explanation {0}".format(index + 1),
                candidate_id="shared",
                choices=["A", "B", "C", "D"] if question_type == "mcq" else [],
            )
        )
    return questions


def test_build_qmd_contains_question_and_answer_slides():
    qmd = build_qmd("quiz1", Path("sample.py"), _questions(), _candidate_map())
    assert qmd.count("## Question") == 10
    assert qmd.count("## Answer") == 10
    assert "- A" in qmd


def test_write_and_render_quiz_creates_qmd_and_html(tmp_path):
    artifacts = write_and_render_quiz(
        "quiz1",
        Path("sample.py"),
        _questions(),
        _candidate_map(),
        output_dir=tmp_path,
    )
    assert artifacts.qmd_path.exists()
    assert artifacts.html_path.exists()
