from _typeshed import Incomplete
from typing import Callable, List, Optional, Set

def directed_hausdorff(u, v, seed: int = ...): ...
def minkowski(u, v, p: int = ..., w: Incomplete | None = ...): ...
def euclidean(u, v, w: Incomplete | None = ...): ...
def sqeuclidean(u, v, w: Incomplete | None = ...): ...
def correlation(u, v, w: Incomplete | None = ..., centered: bool = ...): ...
def cosine(u, v, w: Incomplete | None = ...): ...
def hamming(u, v, w: Incomplete | None = ...): ...
def jaccard(u, v, w: Incomplete | None = ...): ...
def kulsinski(u, v, w: Incomplete | None = ...): ...
def kulczynski1(u, v, *, w: Incomplete | None = ...): ...
def seuclidean(u, v, V): ...
def cityblock(u, v, w: Incomplete | None = ...): ...
def mahalanobis(u, v, VI): ...
def chebyshev(u, v, w: Incomplete | None = ...): ...
def braycurtis(u, v, w: Incomplete | None = ...): ...
def canberra(u, v, w: Incomplete | None = ...): ...
def jensenshannon(p, q, base: Incomplete | None = ..., *, axis: int = ..., keepdims: bool = ...): ...
def yule(u, v, w: Incomplete | None = ...): ...
def dice(u, v, w: Incomplete | None = ...): ...
def rogerstanimoto(u, v, w: Incomplete | None = ...): ...
def russellrao(u, v, w: Incomplete | None = ...): ...
def sokalmichener(u, v, w: Incomplete | None = ...): ...
def sokalsneath(u, v, w: Incomplete | None = ...): ...

class CDistMetricWrapper:
    metric_name: str
    def __call__(self, XA, XB, *, out: Incomplete | None = ..., **kwargs): ...
    def __init__(self, metric_name) -> None: ...

class CDistWeightedMetricWrapper:
    metric_name: str
    weighted_metric: str
    def __call__(self, XA, XB, *, out: Incomplete | None = ..., **kwargs): ...
    def __init__(self, metric_name, weighted_metric) -> None: ...

class PDistMetricWrapper:
    metric_name: str
    def __call__(self, X, *, out: Incomplete | None = ..., **kwargs): ...
    def __init__(self, metric_name) -> None: ...

class PDistWeightedMetricWrapper:
    metric_name: str
    weighted_metric: str
    def __call__(self, X, *, out: Incomplete | None = ..., **kwargs): ...
    def __init__(self, metric_name, weighted_metric) -> None: ...

class MetricInfo:
    canonical_name: str
    aka: Set[str]
    dist_func: Callable
    cdist_func: Callable
    pdist_func: Callable
    validator: Optional[Callable]
    types: List[str]
    requires_contiguous_out: bool
    def __init__(self, canonical_name, aka, dist_func, cdist_func, pdist_func, validator, types, requires_contiguous_out) -> None: ...

def pdist(X, metric: str = ..., *, out: Incomplete | None = ..., **kwargs): ...
def squareform(X, force: str = ..., checks: bool = ...): ...
def is_valid_dm(D, tol: float = ..., throw: bool = ..., name: str = ..., warning: bool = ...): ...
def is_valid_y(y, warning: bool = ..., throw: bool = ..., name: Incomplete | None = ...): ...
def num_obs_dm(d): ...
def num_obs_y(Y): ...
def cdist(XA, XB, metric: str = ..., *, out: Incomplete | None = ..., **kwargs): ...
