from __future__ import annotations

import ast
import io
import tokenize
from pathlib import Path
from typing import List, Optional, Tuple

from .execution import execute_target
from .linting import collect_lint_candidates
from .models import AnalysisResult, Candidate


def _clip_snippet(lines: List[str], start: int, end: int, max_lines: int = 24) -> Tuple[str, int, int]:
    start = max(1, start)
    end = min(len(lines), end)
    window = lines[start - 1 : end]
    if len(window) > max_lines:
        window = window[:max_lines]
        end = start + max_lines - 1
    snippet = "\n".join(window).rstrip()
    return snippet, start, end


def _source_segment(
    source: str, lines: List[str], node: ast.AST, fallback_span: int = 8
) -> Tuple[str, Optional[int], Optional[int]]:
    start = getattr(node, "lineno", None)
    end = getattr(node, "end_lineno", start)
    if start is None:
        return "", None, None
    if end is None:
        end = min(len(lines), start + fallback_span)
    return _clip_snippet(lines, start, end)


def _make_module_summary(tree: ast.AST, lines: List[str]) -> Candidate:
    functions = sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in ast.walk(tree))
    classes = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
    imports = sum(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree))
    snippet, start, end = _clip_snippet(lines, 1, min(len(lines), 20))
    return Candidate(
        candidate_id="module-summary",
        category="structure",
        prompt="Summarize the overall structure and responsibilities of this Python file.",
        evidence=f"The file contains {functions} function(s), {classes} class(es), and {imports} import statement(s).",
        snippet=snippet,
        line_start=start,
        line_end=end,
        priority=20,
    )


def _safe_unparse(node: ast.AST) -> str:
    if hasattr(ast, "unparse"):
        return ast.unparse(node)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return "{0}.{1}".format(_safe_unparse(node.value), node.attr)
    return type(node).__name__


def _collect_ast_candidates(tree: ast.Module, source: str, lines: List[str]) -> List[Candidate]:
    candidates = [_make_module_summary(tree, lines)]

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            snippet, start, end = _source_segment(source, lines, node, fallback_span=2)
            imported = ast.get_source_segment(source, node) or "import statement"
            candidates.append(
                Candidate(
                    candidate_id=f"import-{start}",
                    category="imports",
                    prompt="Explain what dependency or symbol is introduced here and why it matters to the file.",
                    evidence=imported,
                    snippet=snippet,
                    line_start=start,
                    line_end=end,
                    priority=25,
                )
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            snippet, start, end = _source_segment(source, lines, node)
            decorator_count = len(node.decorator_list)
            async_prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
            evidence = (
                f"{async_prefix}function `{node.name}` takes {len(node.args.args)} positional parameter(s)"
                f" and uses {decorator_count} decorator(s)."
            )
            candidates.append(
                Candidate(
                    candidate_id=f"function-{node.name}",
                    category="function",
                    prompt=f"Describe the role and behavior of `{node.name}`.",
                    evidence=evidence,
                    snippet=snippet,
                    line_start=start,
                    line_end=end,
                    priority=45,
                )
            )
        elif isinstance(node, ast.ClassDef):
            snippet, start, end = _source_segment(source, lines, node)
            method_count = sum(
                isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) for child in node.body
            )
            base_names = [_safe_unparse(base) for base in node.bases] if node.bases else []
            evidence = f"Class `{node.name}` defines {method_count} method(s); bases: {base_names or ['object']}."
            candidates.append(
                Candidate(
                    candidate_id=f"class-{node.name}",
                    category="class",
                    prompt=f"Explain the purpose and shape of the class `{node.name}`.",
                    evidence=evidence,
                    snippet=snippet,
                    line_start=start,
                    line_end=end,
                    priority=50,
                )
            )
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            snippet, start, end = _source_segment(source, lines, node, fallback_span=3)
            candidates.append(
                Candidate(
                    candidate_id=f"assignment-{start}",
                    category="state",
                    prompt="Explain what module-level state is being established here.",
                    evidence=(ast.get_source_segment(source, node) or "assignment").strip(),
                    snippet=snippet,
                    line_start=start,
                    line_end=end,
                    priority=15,
                )
            )

    control_count = 0
    match_type = getattr(ast, "Match", None)
    flow_types = [ast.If, ast.For, ast.While, ast.Try, ast.With]
    if match_type is not None:
        flow_types.append(match_type)
    for node in ast.walk(tree):
        if isinstance(node, tuple(flow_types)):
            snippet, start, end = _source_segment(source, lines, node, fallback_span=10)
            if start is None:
                continue
            candidates.append(
                Candidate(
                    candidate_id=f"flow-{start}",
                    category="control-flow",
                    prompt="Explain the behavior and edge cases of this control-flow block.",
                    evidence=f"{type(node).__name__} block starts at line {start}.",
                    snippet=snippet,
                    line_start=start,
                    line_end=end,
                    priority=35,
                )
            )
            control_count += 1
            if control_count >= 8:
                break

    return candidates


def _collect_token_candidates(source: str, lines: List[str]) -> List[Candidate]:
    reader = io.StringIO(source).readline
    names: List[str] = []
    try:
        for token in tokenize.generate_tokens(reader):
            if token.type == tokenize.NAME and token.string not in {"def", "class", "import", "from"}:
                names.append(token.string)
    except tokenize.TokenError:
        return []
    common = sorted(set(names[:20]))
    if not common:
        return []
    snippet, start, end = _clip_snippet(lines, 1, min(len(lines), 20))
    return [
        Candidate(
            candidate_id="token-overview",
            category="tokens",
            prompt="What do the repeated identifiers suggest about the file's core responsibilities?",
            evidence=f"Representative identifiers: {', '.join(common[:12])}.",
            snippet=snippet,
            line_start=start,
            line_end=end,
            priority=10,
        )
    ]


def _syntax_diagnostic(path: Path, source: str, error: SyntaxError) -> Candidate:
    lines = source.splitlines()
    line = error.lineno or 1
    snippet, start, end = _clip_snippet(lines, line, line + 2)
    return Candidate(
        candidate_id="syntax-error",
        category="diagnostic",
        prompt="Identify the syntax problem in this file and explain why Python rejects it.",
        evidence=f"{error.msg} at line {line}.",
        snippet=snippet,
        line_start=start,
        line_end=end,
        priority=100,
        metadata={"path": str(path)},
    )


def _execution_candidate(result, lines: List[str]) -> Candidate:
    snippet, start, end = _clip_snippet(lines, 1, min(len(lines), 20))
    if not result.available:
        return Candidate(
            candidate_id="execution-unavailable",
            category="diagnostic",
            prompt="Why can this file not be executed for quiz validation under the default safety rules?",
            evidence=result.reason or "Sandbox execution is unavailable.",
            snippet=snippet,
            line_start=start,
            line_end=end,
            priority=85,
            metadata={"mode": result.mode},
        )

    if result.returncode == 0:
        stdout = result.stdout or "<no stdout>"
        return Candidate(
            candidate_id="execution-success",
            category="execution",
            prompt="Explain what happens when this file is executed and why.",
            evidence=f"Execution mode: {result.mode}. stdout: {stdout[:200]}",
            snippet=snippet,
            line_start=start,
            line_end=end,
            priority=60,
            execution_required=True,
            metadata={"mode": result.mode, "stdout": result.stdout},
        )

    stderr = result.stderr or "<no stderr>"
    return Candidate(
        candidate_id="execution-failure",
        category="diagnostic",
        prompt="Diagnose the import-time or runtime failure shown when this file executes.",
        evidence=f"Execution mode: {result.mode}. stderr: {stderr[:300]}",
        snippet=snippet,
        line_start=start,
        line_end=end,
        priority=95,
        metadata={"mode": result.mode, "stderr": result.stderr, "returncode": result.returncode},
    )


def analyze_target(
    target_path: Path,
    *,
    allow_unsafe_exec: bool,
    python_executable: str,
) -> AnalysisResult:
    source = target_path.read_text(encoding="utf-8")
    lines = source.splitlines()
    candidates: List[Candidate] = []
    execution_result = None

    try:
        tree = ast.parse(source, filename=str(target_path))
    except SyntaxError as exc:
        candidates.append(_syntax_diagnostic(target_path, source, exc))
        execution_result = None
    else:
        candidates.extend(_collect_ast_candidates(tree, source, lines))
        candidates.extend(_collect_token_candidates(source, lines))
        execution_result = execute_target(
            target_path,
            allow_unsafe_exec=allow_unsafe_exec,
            python_executable=python_executable,
        )
        candidates.append(_execution_candidate(execution_result, lines))
        candidates.extend(collect_lint_candidates(target_path, source))

    candidates = sorted(candidates, key=lambda item: (-item.priority, item.line_start or 0, item.candidate_id))
    return AnalysisResult(
        target_path=target_path,
        source=source,
        candidates=candidates,
        execution_result=execution_result,
    )
