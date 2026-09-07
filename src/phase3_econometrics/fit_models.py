"""
Phase 3: Econometric model fitting.

Model 1: pooled Bradley-Terry-with-order-effects via statsmodels Logit,
  cov_type='cluster' clustered on clip_id; cross-checked via wild cluster
  bootstrap (wildboottest / hand-rolled bootstrap-t), given only 20 clusters.
Model 2 (robustness): ConditionalLogit stratified by clip.
Davidson (1970) tie extension for the ties-aware variant.
"""


def fit_pooled_bt_logit(design_matrix):
    raise NotImplementedError("TODO: statsmodels Logit + cluster-robust SEs")


def fit_conditional_logit(design_matrix, clip_id_col: str = "clip_id"):
    raise NotImplementedError("TODO: statsmodels ConditionalLogit stratified by clip")


def fit_davidson_tie_model(trials):
    raise NotImplementedError("TODO: joint MLE of beta, delta, nu (ties)")


def wild_cluster_bootstrap(model, clip_id_col: str = "clip_id", n_boot: int = 999):
    raise NotImplementedError("TODO: CGM (2008) wild cluster bootstrap via wildboottest")
