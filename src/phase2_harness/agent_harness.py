"""
Phase 2: Agentic evaluation harness.

temperature=0, fixed seed where available, structured multimodal audio input
(never base64-in-text), JSON-schema structured output: choice, confidence,
artifacts. Handles API refusals, schema-validation failures, and ties.
"""

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "choice": {"type": "string", "enum": ["A", "B", "tie"]},
        "confidence": {"type": "integer", "minimum": 1, "maximum": 5},
        "artifacts": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["choice", "confidence"],
}


def evaluate_pair(clip_a_path: str, clip_b_path: str, order: int) -> dict:
    raise NotImplementedError("TODO: call audio-capable LLM, parse structured output")
