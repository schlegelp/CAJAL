from .bregman import sinkhorn as sinkhorn
from .optim import cg as cg
from .utils import UndefinedParameter as UndefinedParameter, dist as dist
from _typeshed import Incomplete

def init_matrix(C1, C2, p, q, loss_fun: str = ...): ...
def tensor_product(constC, hC1, hC2, T): ...
def gwloss(constC, hC1, hC2, T): ...
def gwggrad(constC, hC1, hC2, T): ...
def update_square_loss(p, lambdas, T, Cs): ...
def update_kl_loss(p, lambdas, T, Cs): ...
def gromov_wasserstein(C1, C2, p, q, loss_fun, log: bool = ..., armijo: bool = ..., **kwargs): ...
def gromov_wasserstein2(C1, C2, p, q, loss_fun, log: bool = ..., armijo: bool = ..., **kwargs): ...
def fused_gromov_wasserstein(M, C1, C2, p, q, loss_fun: str = ..., alpha: float = ..., armijo: bool = ..., log: bool = ..., **kwargs): ...
def fused_gromov_wasserstein2(M, C1, C2, p, q, loss_fun: str = ..., alpha: float = ..., armijo: bool = ..., log: bool = ..., **kwargs): ...
def entropic_gromov_wasserstein(C1, C2, p, q, loss_fun, epsilon, max_iter: int = ..., tol: float = ..., verbose: bool = ..., log: bool = ...): ...
def entropic_gromov_wasserstein2(C1, C2, p, q, loss_fun, epsilon, max_iter: int = ..., tol: float = ..., verbose: bool = ..., log: bool = ...): ...
def entropic_gromov_barycenters(N, Cs, ps, p, lambdas, loss_fun, epsilon, max_iter: int = ..., tol: float = ..., verbose: bool = ..., log: bool = ..., init_C: Incomplete | None = ...): ...
def gromov_barycenters(N, Cs, ps, p, lambdas, loss_fun, max_iter: int = ..., tol: float = ..., verbose: bool = ..., log: bool = ..., init_C: Incomplete | None = ...): ...
def fgw_barycenters(N, Ys, Cs, ps, lambdas, alpha, fixed_structure: bool = ..., fixed_features: bool = ..., p: Incomplete | None = ..., loss_fun: str = ..., max_iter: int = ..., tol: float = ..., verbose: bool = ..., log: bool = ..., init_C: Incomplete | None = ..., init_X: Incomplete | None = ...): ...
def update_sructure_matrix(p, lambdas, T, Cs): ...
def update_feature_matrix(lambdas, Ys, Ts, p): ...
