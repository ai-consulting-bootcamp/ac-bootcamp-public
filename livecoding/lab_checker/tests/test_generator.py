from pathlib import Path

import json

import pytest

from codecheck.generator import generate_quiz_questions
from codecheck.models import AnalysisResult, Candidate


class FakeResponse:
    def __init__(self, payload):
        self.output_text = json.dumps(payload)


class FakeClient:
    def __init__(self, payload):
        self.payload = payload
        self.responses = self

    def create(self, **kwargs):
        return FakeResponse(self.payload)


def _analysis():
    candidates = []
    for index in range(10):
        candidates.append(
            Candidate(
                candidate_id="candidate-{0}".format(index),
                category="function",
                prompt="Explain candidate {0}".format(index),
                evidence="evidence",
                snippet="print({0})".format(index),
                line_start=index + 1,
                line_end=index + 1,
                priority=10,
            )
        )
    return AnalysisResult(target_path=Path("sample.py"), source="print('x')", candidates=candidates, execution_result=None)


def test_generate_quiz_questions_validates_exact_count_and_mix():
    payload = {
        "questions": [
            {
                "candidate_id": "candidate-{0}".format(index),
                "question_type": "mcq" if index < 5 else "short-answer",
                "prompt": "Question {0}".format(index),
                "choices": ["A", "B", "C", "D"] if index < 5 else [],
                "answer": "Answer",
                "explanation": "Explanation",
            }
            for index in range(10)
        ]
    }
    questions = generate_quiz_questions(_analysis(), "quiz1", client=FakeClient(payload))
    assert len(questions) == 10


def test_generate_quiz_questions_rejects_invalid_mix():
    payload = {
        "questions": [
            {
                "candidate_id": "candidate-{0}".format(index),
                "question_type": "mcq",
                "prompt": "Question {0}".format(index),
                "choices": ["A", "B", "C", "D"],
                "answer": "Answer",
                "explanation": "Explanation",
            }
            for index in range(10)
        ]
    }
    with pytest.raises(ValueError):
        generate_quiz_questions(_analysis(), "quiz1", client=FakeClient(payload))
