# Codecheck V1 Plan

## Summary
Build a Python package `codecheck` whose primary interface is `python -m codecheck <target.py> [-n quiz_name]`. It analyzes one target file at a time, generates exactly 10 quiz items with a mix of MCQ and short-answer questions, and outputs both a Quarto source deck and rendered HTML. Each question slide shows only the relevant code snippet with line references; the next slide contains the correct answer plus a brief explanation.

## Implementation Changes
- Create a CLI entrypoint for `python -m codecheck` with required target-file input and optional `-n/--name`.
- Generate a random unique quiz name when `-n/--name` is omitted.
- Limit analysis scope to the target file only; do not traverse sibling modules or package context.
- Build a file-analysis pipeline that extracts:
  - structural facts from the file AST/token stream,
  - relevant snippets and line references,
  - obvious syntax/import/runtime failures as diagnostic material,
  - improvement findings from both `Ruff` and `Pylint`, merged and deduped before question selection.
- Use OpenAI to synthesize exactly 10 questions from the collected facts/findings, with the model free to choose the depth/detail mix.
- Convert obvious bugs and lint findings into quiz items rather than a separate review section.
- Render the quiz as Quarto:
  - slide N = question + snippet + line refs,
  - slide N+1 = answer + brief explanation.
- Keep both the generated `.qmd` and rendered `.html` artifact.

## Execution and Validation Rules
- Execution-based questions require a strict sandbox by default.
- Add an explicit unsafe override flag so users can opt into local non-sandboxed execution when sandboxing is unavailable.
- When code cannot be imported/executed because of syntax errors, import-time crashes, or missing dependencies, generate diagnostic quiz content instead of aborting.
- Treat Quarto availability, Python runtime availability, and OpenAI credentials as hard prerequisites with clear CLI errors if absent.

## Public Interfaces
- Primary command: `python -m codecheck target.py -n quiz1`
- New CLI flag: `--allow-unsafe-exec` to bypass the sandbox requirement explicitly.
- Output contract:
  - `<name>.qmd`
  - `<name>.html`

## Test Plan
- Unit tests for CLI parsing, quiz naming, snippet extraction, line-reference mapping, and lint deduplication.
- Unit tests for diagnostic-mode handling of:
  - syntax-error files,
  - import-time exceptions,
  - missing-dependency failures.
- Integration tests for:
  - a valid Python file producing 10 question/answer slide pairs,
  - mixed MCQ + short-answer output formatting,
  - `.qmd` generation plus Quarto HTML rendering,
  - sandbox-required execution paths,
  - `--allow-unsafe-exec` override behavior.

## Assumptions
- The later clarification supersedes the earlier “fail fast on missing deps” answer: dependency-related import failures should become diagnostic quiz content.
- `Ruff` and `Pylint` are both required in v1 and their findings are normalized into one ranked pool.
- Answer slides stay brief; they explain the result but do not become full tutorials.
- V1 does not analyze imported local modules or whole-package context.
