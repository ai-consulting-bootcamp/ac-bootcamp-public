from __future__ import annotations

import json
import os
from typing import Iterable, List, Optional

from openai import OpenAI

from .models import AnalysisResult, QuizQuestion


DEFAULT_MODEL = "gpt-4.1"


def ensure_openai_credentials() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


def _build_prompt(analysis: AnalysisResult, quiz_name: str) -> str:
    candidates = [candidate.to_prompt_dict() for candidate in analysis.candidates]
    payload = json.dumps(candidates, indent=2)
    return f"""
You are creating a code-comprehension quiz for a single Python file.

Quiz name: {quiz_name}
Target file: {analysis.target_path.name}

Rules:
- Return valid JSON only.
- Return exactly 10 quiz items in a top-level object with key "questions".
- Use a mix of question types: at least 3 MCQ items and at least 3 short-answer items.
- Every question must reference one of the provided candidate_id values.
- Turn diagnostics and lint findings into questions instead of creating a separate review section.
- Keep answer explanations brief, concrete, and correct.
- Never mention code outside this file.
- Do not invent execution outcomes unless the linked candidate category is "execution" or "diagnostic" and includes execution evidence.

JSON shape:
{{
  "questions": [
    {{
      "candidate_id": "string",
      "question_type": "mcq" | "short-answer",
      "prompt": "string",
      "choices": ["A", "B", "C", "D"],  // required only for mcq
      "answer": "string",
      "explanation": "string"
    }}
  ]
}}

Candidate material:
{payload}
""".strip()


def _extract_text(response) -> str:
    if getattr(response, "output_text", None):
        return response.output_text
    return ""


def _validate_questions(raw_questions: Iterable[dict], analysis: AnalysisResult) -> List[QuizQuestion]:
    candidate_ids = {candidate.candidate_id for candidate in analysis.candidates}
    questions: List[QuizQuestion] = []
    for item in raw_questions:
        candidate_id = item.get("candidate_id", "")
        if candidate_id not in candidate_ids:
            raise ValueError(f"Unknown candidate_id returned by model: {candidate_id}")
        question_type = item.get("question_type")
        if question_type not in {"mcq", "short-answer"}:
            raise ValueError(f"Unsupported question_type: {question_type}")
        choices = item.get("choices") or []
        if question_type == "mcq" and len(choices) < 3:
            raise ValueError("MCQ items must include at least three choices.")
        questions.append(
            QuizQuestion(
                question_type=question_type,
                prompt=item.get("prompt", "").strip(),
                answer=item.get("answer", "").strip(),
                explanation=item.get("explanation", "").strip(),
                candidate_id=candidate_id,
                choices=choices,
            )
        )
    if len(questions) != 10:
        raise ValueError(f"Expected exactly 10 questions, received {len(questions)}.")
    counts = {kind: sum(question.question_type == kind for question in questions) for kind in {"mcq", "short-answer"}}
    if counts["mcq"] < 3 or counts["short-answer"] < 3:
        raise ValueError("Question set must mix MCQ and short-answer items.")
    return questions


def generate_quiz_questions(
    analysis: AnalysisResult,
    quiz_name: str,
    *,
    client: Optional[OpenAI] = None,
    model: str = DEFAULT_MODEL,
) -> List[QuizQuestion]:
    client = client or OpenAI()
    response = client.responses.create(
        model=model,
        input=_build_prompt(analysis, quiz_name),
    )
    text = _extract_text(response).strip()
    payload = json.loads(text)
    raw_questions = payload.get("questions") or []
    return _validate_questions(raw_questions, analysis)
