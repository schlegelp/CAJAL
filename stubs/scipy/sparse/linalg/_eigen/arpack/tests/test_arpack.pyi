from _typeshed import Incomplete
from scipy._lib._gcutils import IS_PYPY as IS_PYPY, assert_deallocated as assert_deallocated
from scipy.linalg import eig as eig, eigh as eigh
from scipy.sparse import csc_matrix as csc_matrix, csr_matrix as csr_matrix, diags as diags, rand as rand
from scipy.sparse.linalg import LinearOperator as LinearOperator, aslinearoperator as aslinearoperator
from scipy.sparse.linalg._eigen.arpack import ArpackNoConvergence as ArpackNoConvergence, arpack as arpack, eigs as eigs, eigsh as eigsh

__usage__: str

def generate_matrix(N, complex_: bool = ..., hermitian: bool = ..., pos_definite: bool = ..., sparse: bool = ...): ...
def generate_matrix_symmetric(N, pos_definite: bool = ..., sparse: bool = ...): ...
def assert_allclose_cc(actual, desired, **kw) -> None: ...
def argsort_which(eigenvalues, typ, k, which, sigma: Incomplete | None = ..., OPpart: Incomplete | None = ..., mode: Incomplete | None = ...): ...
def eval_evec(symmetric, d, typ, k, which, v0: Incomplete | None = ..., sigma: Incomplete | None = ..., mattype=..., OPpart: Incomplete | None = ..., mode: str = ...) -> None: ...

class DictWithRepr(dict):
    name: Incomplete
    def __init__(self, name) -> None: ...

class SymmetricParams:
    eigs: Incomplete
    which: Incomplete
    mattypes: Incomplete
    sigmas_modes: Incomplete
    real_test_cases: Incomplete
    complex_test_cases: Incomplete
    def __init__(self) -> None: ...

class NonSymmetricParams:
    eigs: Incomplete
    which: Incomplete
    mattypes: Incomplete
    sigmas_OPparts: Incomplete
    real_test_cases: Incomplete
    complex_test_cases: Incomplete
    def __init__(self) -> None: ...

def test_symmetric_modes() -> None: ...
def test_hermitian_modes() -> None: ...
def test_symmetric_starting_vector() -> None: ...
def test_symmetric_no_convergence() -> None: ...
def test_real_nonsymmetric_modes() -> None: ...
def test_complex_nonsymmetric_modes() -> None: ...
def test_standard_nonsymmetric_starting_vector() -> None: ...
def test_general_nonsymmetric_starting_vector() -> None: ...
def test_standard_nonsymmetric_no_convergence() -> None: ...
def test_eigen_bad_shapes() -> None: ...
def test_eigen_bad_kwargs() -> None: ...
def test_ticket_1459_arpack_crash() -> None: ...
def test_linearoperator_deallocation(): ...
def test_parallel_threads() -> None: ...
def test_reentering(): ...
def test_regression_arpackng_1315() -> None: ...
def test_eigs_for_k_greater() -> None: ...
def test_eigsh_for_k_greater() -> None: ...
def test_real_eigs_real_k_subset() -> None: ...
