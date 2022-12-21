import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, Period as Period, Resolution as Resolution, Tick as Tick
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, npt as npt
from pandas.core.arrays.period import PeriodArray as PeriodArray, period_array as period_array, raise_on_incompatible as raise_on_incompatible, validate_dtype_freq as validate_dtype_freq
from pandas.core.dtypes.common import is_datetime64_any_dtype as is_datetime64_any_dtype, is_integer as is_integer, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype
from pandas.core.indexes.base import maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin as DatetimeIndexOpsMixin
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, Index as Index
from pandas.core.indexes.extension import inherit_names as inherit_names
from pandas.core.indexes.numeric import Int64Index as Int64Index
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Hashable

class PeriodIndex(DatetimeIndexOpsMixin):
    freq: BaseOffset
    dtype: PeriodDtype
    def asfreq(self, freq: Incomplete | None = ..., how: str = ...) -> PeriodIndex: ...
    def to_timestamp(self, freq: Incomplete | None = ..., how: str = ...) -> DatetimeIndex: ...
    @property
    def hour(self) -> Int64Index: ...
    @property
    def minute(self) -> Int64Index: ...
    @property
    def second(self) -> Int64Index: ...
    def __new__(cls, data: Incomplete | None = ..., ordinal: Incomplete | None = ..., freq: Incomplete | None = ..., dtype: Union[Dtype, None] = ..., copy: bool = ..., name: Hashable = ..., **fields) -> PeriodIndex: ...
    @property
    def values(self) -> np.ndarray: ...
    def asof_locs(self, where: Index, mask: npt.NDArray[np.bool_]) -> np.ndarray: ...
    def astype(self, dtype, copy: bool = ..., how=...): ...
    @property
    def is_full(self) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def get_loc(self, key, method: Incomplete | None = ..., tolerance: Incomplete | None = ...): ...

def period_range(start: Incomplete | None = ..., end: Incomplete | None = ..., periods: Union[int, None] = ..., freq: Incomplete | None = ..., name: Incomplete | None = ...) -> PeriodIndex: ...
