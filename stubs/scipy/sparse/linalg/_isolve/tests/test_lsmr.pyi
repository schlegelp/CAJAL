from .test_lsqr import G as G, b as b
from _typeshed import Incomplete
from scipy.sparse import coo_matrix as coo_matrix
from scipy.sparse.linalg import lsmr as lsmr
from scipy.sparse.linalg._interface import aslinearoperator as aslinearoperator

class TestLSMR:
    n: int
    m: int
    def setup_method(self) -> None: ...
    def assertCompatibleSystem(self, A, xtrue) -> None: ...
    def testIdentityACase1(self) -> None: ...
    def testIdentityACase2(self) -> None: ...
    def testIdentityACase3(self) -> None: ...
    def testBidiagonalA(self) -> None: ...
    def testScalarB(self) -> None: ...
    def testComplexX(self) -> None: ...
    def testComplexX0(self) -> None: ...
    def testComplexA(self) -> None: ...
    def testComplexB(self) -> None: ...
    def testColumnB(self) -> None: ...
    def testInitialization(self) -> None: ...

class TestLSMRReturns:
    n: int
    A: Incomplete
    xtrue: Incomplete
    Afun: Incomplete
    b: Incomplete
    x0: Incomplete
    x00: Incomplete
    returnValues: Incomplete
    returnValuesX0: Incomplete
    def setup_method(self) -> None: ...
    def test_unchanged_x0(self) -> None: ...
    def testNormr(self) -> None: ...
    def testNormar(self) -> None: ...
    def testNormx(self) -> None: ...

def lowerBidiagonalMatrix(m, n): ...
