from . import cvx as cvx
from .cvx import barycenter as barycenter
from _typeshed import Incomplete

def emd(a, b, M, numItermax: int = ..., log: bool = ..., center_dual: bool = ...): ...
def emd2(a, b, M, processes=..., numItermax: int = ..., log: bool = ..., return_matrix: bool = ..., center_dual: bool = ...): ...
def free_support_barycenter(measures_locations, measures_weights, X_init, b: Incomplete | None = ..., weights: Incomplete | None = ..., numItermax: int = ..., stopThr: float = ..., verbose: bool = ..., log: Incomplete | None = ...): ...
def emd_1d(x_a, x_b, a: Incomplete | None = ..., b: Incomplete | None = ..., metric: str = ..., p: float = ..., dense: bool = ..., log: bool = ...): ...
def emd2_1d(x_a, x_b, a: Incomplete | None = ..., b: Incomplete | None = ..., metric: str = ..., p: float = ..., dense: bool = ..., log: bool = ...): ...
def wasserstein_1d(x_a, x_b, a: Incomplete | None = ..., b: Incomplete | None = ..., p: float = ...): ...
