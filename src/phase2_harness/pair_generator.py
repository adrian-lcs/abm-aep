"""
Phase 2: Pair generator (hub + adjacent + symmetric cross-codec, both orders).

(a) every format vs. WAV reference (hub) -- 9 pairs
(b) adjacent-bitrate pairs within each codec family -- 5 pairs
(c) matched-bitrate cross-codec pairs, symmetric across 96k and 128k tiers -- 5 pairs
Each pair is presented in both presentation orders. Includes hidden-reference
and low-quality-anchor trials per clip. Verify the resulting comparison graph
is connected before proceeding (see phase3_econometrics/diagnostics.py).
"""


def generate_pairs(formats: list[str]) -> list[tuple[str, str]]:
    raise NotImplementedError("TODO: implement hub+adjacent+cross-codec pairing")
