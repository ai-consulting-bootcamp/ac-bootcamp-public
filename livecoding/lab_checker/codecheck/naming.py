from __future__ import annotations

import re
import secrets
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "quiz"


def generate_quiz_name(target_path: Path) -> str:
    stem = slugify(target_path.stem)
    suffix = secrets.token_hex(4)
    return f"{stem}-{suffix}"
