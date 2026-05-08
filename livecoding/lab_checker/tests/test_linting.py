from codecheck.linting import dedupe_lint_findings
from codecheck.models import Candidate


def test_dedupe_lint_findings_prefers_higher_priority():
    low = Candidate(
        candidate_id="a",
        category="lint",
        prompt="prompt",
        evidence="Unused import",
        snippet="import os",
        line_start=1,
        line_end=1,
        priority=40,
        metadata={"code": "F401"},
    )
    high = Candidate(
        candidate_id="b",
        category="lint",
        prompt="prompt",
        evidence="Unused import",
        snippet="import os",
        line_start=1,
        line_end=1,
        priority=80,
        metadata={"code": "F401"},
    )
    deduped = dedupe_lint_findings([low, high])
    assert deduped == [high]
