from pathlib import Path

from codecheck.execution import execute_target


def test_execute_target_requires_sandbox_by_default(monkeypatch, tmp_path):
    target = tmp_path / "script.py"
    target.write_text("print('ok')\n", encoding="utf-8")
    monkeypatch.setattr("codecheck.execution.shutil.which", lambda _: None)
    result = execute_target(target, allow_unsafe_exec=False, python_executable="python")
    assert result.available is False
    assert result.mode == "sandboxed"


def test_execute_target_allows_unsafe_override(monkeypatch, tmp_path):
    target = tmp_path / "script.py"
    target.write_text("print('ok')\n", encoding="utf-8")
    monkeypatch.setattr("codecheck.execution.shutil.which", lambda _: None)
    result = execute_target(target, allow_unsafe_exec=True)
    assert result.available is True
    assert result.mode == "unsafe"
    assert result.returncode == 0
    assert result.stdout == "ok"
