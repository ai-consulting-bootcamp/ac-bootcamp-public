from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

from .models import ExecutionResult


def _base_env() -> Dict[str, str]:
    env: Dict[str, str] = {
        "PATH": os.environ.get("PATH", ""),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if "SYSTEMROOT" in os.environ:
        env["SYSTEMROOT"] = os.environ["SYSTEMROOT"]
    return env


def _run_subprocess(command: List[str], timeout: int) -> ExecutionResult:
    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=_base_env(),
    )
    return ExecutionResult(
        mode="unsafe",
        available=True,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout.strip(),
        stderr=completed.stderr.strip(),
    )


def _run_bwrap(target_path: Path, python_executable: str, timeout: int) -> ExecutionResult:
    bwrap = shutil.which("bwrap")
    if not bwrap:
        return ExecutionResult(
            mode="sandboxed",
            available=False,
            command=[],
            returncode=None,
            stdout="",
            stderr="",
            reason="bubblewrap is not installed",
        )

    command = [
        bwrap,
        "--ro-bind",
        "/",
        "/",
        "--tmpfs",
        "/tmp",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--chdir",
        "/tmp",
        "--unshare-all",
        "--die-with-parent",
        python_executable,
        "-I",
        "-B",
        str(target_path),
    ]
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=_base_env(),
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return ExecutionResult(
            mode="sandboxed",
            available=False,
            command=command,
            returncode=None,
            stdout="",
            stderr="",
            reason=str(exc),
        )

    return ExecutionResult(
        mode="sandboxed",
        available=True,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout.strip(),
        stderr=completed.stderr.strip(),
    )


def execute_target(
    target_path: Path,
    *,
    allow_unsafe_exec: bool,
    python_executable: Optional[str] = None,
    timeout: int = 10,
) -> ExecutionResult:
    python_executable = python_executable or sys.executable
    sandboxed = _run_bwrap(target_path, python_executable, timeout)
    if sandboxed.available:
        return sandboxed
    if not allow_unsafe_exec:
        return sandboxed
    unsafe_command = [python_executable, "-I", "-B", str(target_path)]
    result = _run_subprocess(unsafe_command, timeout)
    result.mode = "unsafe"
    return result
