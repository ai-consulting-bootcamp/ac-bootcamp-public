from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Iterable, Sequence


@dataclass
class PineconeVector:
    id: str
    values: list[float]
    metadata: dict[str, Any]


def _json_safe(value: Any) -> Any:
    """Convert a value into something Pinecone metadata can store safely."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}

    if isinstance(value, (list, tuple, set)):
        return [_json_safe(v) for v in value]

    return str(value)


def build_pinecone_vectors(
    records: Sequence[dict[str, Any]],
    embeddings: Sequence[Sequence[float]],
    id_prefix: str = "section",
) -> list[dict[str, Any]]:
    """
    Build Pinecone-compatible vector payloads.

    Assumptions:
    - `records[i]["heading"]` is the text you want to embed.
    - Every other field becomes metadata.
    - `embeddings[i]` is the vector for `records[i]["heading"]`.

    Returns objects shaped like:
    {
        "id": "section-1",
        "values": [...],
        "metadata": {...}
    }
    """
    if len(records) != len(embeddings):
        raise ValueError("records and embeddings must have the same length")

    vectors: list[dict[str, Any]] = []

    for i, (record, vector) in enumerate(zip(records, embeddings), start=1):
        if "heading" not in record:
            raise KeyError("Each record must contain a 'heading' field")

        metadata = {
            key: _json_safe(value)
            for key, value in record.items()
            if key != "heading"
        }

        vectors.append(
            {
                "id": f"{id_prefix}-{i}",
                "values": list(vector),
                "metadata": metadata,
            }
        )

    return vectors


def build_documents_for_embedding(records: Iterable[dict[str, Any]]) -> list[str]:
    """
    Build the text inputs you can send to your embedding model.

    This keeps the full heading as the primary searchable text.
    """
    texts: list[str] = []
    for record in records:
        heading = str(record.get("heading", "")).strip()
        if heading:
            texts.append(heading)
    return texts


def serialize_metadata(metadata: dict[str, Any]) -> str:
    """Optional helper if you want to inspect metadata as JSON."""
    return json.dumps(_json_safe(metadata), ensure_ascii=True, indent=2)


if __name__ == "__main__":
    sample = [
        {
            "level": "rule",
            "heading": "1. Governing Rules",
            "body": [],
            "page": 1,
        }
    ]
    print(serialize_metadata({k: v for k, v in sample[0].items() if k != "heading"}))
