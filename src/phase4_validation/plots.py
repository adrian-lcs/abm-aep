"""
Phase 4: Caterpillar plots of beta estimates with 95% CIs; flag overlapping
CIs between adjacent bitrates; likelihood-ratio test for the order effect.
"""


def caterpillar_plot(beta_estimates, ci_lower, ci_upper, labels, out_path: str):
    raise NotImplementedError("TODO: matplotlib/seaborn caterpillar plot")


def likelihood_ratio_test_order_effect(full_model, restricted_model) -> dict:
    raise NotImplementedError("TODO: LR test, model with vs. without delta")
