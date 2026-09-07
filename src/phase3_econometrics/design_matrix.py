"""
Phase 3: Differenced design matrix construction.

Each trial row = (dummy columns for i's format) - (dummy columns for j's
format), WAV column omitted as reference, plus the order indicator o_ij
in {+1, -1}.
"""


def build_design_matrix(trials: list[dict]):
    raise NotImplementedError("TODO: implement differenced dummy encoding")
