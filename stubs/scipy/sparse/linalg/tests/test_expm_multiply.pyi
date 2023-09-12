from _typeshed import Incomplete
from scipy.sparse import SparseEfficiencyWarning as SparseEfficiencyWarning
from scipy.sparse.linalg import aslinearoperator as aslinearoperator
from scipy.sparse.linalg._expm_multiply import expm_multiply as expm_multiply

IMPRECISE: Incomplete
REAL_DTYPES: Incomplete
COMPLEX_DTYPES: Incomplete
DTYPES: Incomplete

def estimated(func): ...
def less_than_or_close(a, b): ...

class TestExpmActionSimple:
    def test_theta_monotonicity(self) -> None: ...
    def test_p_max_default(self) -> None: ...
    def test_p_max_range(self) -> None: ...
    def test_onenormest_matrix_power(self) -> None: ...
    def test_expm_multiply(self) -> None: ...
    def test_matrix_vector_multiply(self) -> None: ...
    def test_scaled_expm_multiply(self) -> None: ...
    def test_scaled_expm_multiply_single_timepoint(self) -> None: ...
    def test_sparse_expm_multiply(self) -> None: ...
    def test_complex(self) -> None: ...

class TestExpmActionInterval:
    def test_sparse_expm_multiply_interval(self) -> None: ...
    def test_expm_multiply_interval_vector(self) -> None: ...
    def test_expm_multiply_interval_matrix(self) -> None: ...
    def test_sparse_expm_multiply_interval_dtypes(self) -> None: ...
    def test_expm_multiply_interval_status_0(self) -> None: ...
    def test_expm_multiply_interval_status_1(self) -> None: ...
    def test_expm_multiply_interval_status_2(self) -> None: ...

def test_expm_multiply_dtype(dtype_a, dtype_b, b_is_matrix) -> None: ...
