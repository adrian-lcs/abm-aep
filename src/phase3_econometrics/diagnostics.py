"""
Phase 3.3: Separation & identification diagnostics.

1. Complete/quasi-complete separation detection (statsmodels warnings).
2. Comparison-graph connectivity check (formats=nodes, comparisons=edges) --
   must hold for all beta_i to be jointly identified.

Hypothesis tests: H1 one-sided vs. non-zero thresholds; H2 TOST-style
equivalence test on delta; H3 at both the 96k and 128k tiers.
"""


def check_connectivity(formats: list[str], observed_pairs: list[tuple[str, str]]) -> bool:
    raise NotImplementedError("TODO: graph connectivity check (e.g. networkx)")


def check_separation(fitted_model) -> list[str]:
    raise NotImplementedError("TODO: flag formats at/near 100% win or loss rate")


def test_h1_monotonicity(fitted_model, thresholds: dict) -> dict:
    raise NotImplementedError("TODO: one-sided (estimate-threshold)/SE tests")


def test_h2_order_equivalence(fitted_model, bound: float = 0.5, alpha: float = 0.10) -> dict:
    raise NotImplementedError("TODO: TOST-style 90% CI equivalence test on delta")


def test_h3_cross_codec(fitted_model) -> dict:
    raise NotImplementedError("TODO: AAC/Opus/Vorbis vs MP3 at 96k and 128k tiers")
