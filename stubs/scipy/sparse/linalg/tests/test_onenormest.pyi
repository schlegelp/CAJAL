import scipy.sparse.linalg
from _typeshed import Incomplete

class MatrixProductOperator(scipy.sparse.linalg.LinearOperator):
    A: Incomplete
    B: Incomplete
    ndim: int
    shape: Incomplete
    def __init__(self, A, B) -> None: ...
    @property
    def T(self): ...

class TestOnenormest:
    def test_onenormest_table_3_t_2(self) -> None: ...
    def test_onenormest_table_4_t_7(self) -> None: ...
    def test_onenormest_table_5_t_1(self) -> None: ...
    def test_onenormest_table_6_t_1(self) -> None: ...
    def test_onenormest_linear_operator(self) -> None: ...
    def test_returns(self) -> None: ...

class TestAlgorithm_2_2:
    def test_randn_inv(self) -> None: ...
