from _typeshed import Incomplete
from pandas import Categorical as Categorical, DataFrame as DataFrame, DatetimeIndex as DatetimeIndex, Index as Index, IntervalIndex as IntervalIndex, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex, RangeIndex as RangeIndex, Series as Series, TimedeltaIndex as TimedeltaIndex
from pandas._libs.lib import NoDefault as NoDefault, no_default as no_default
from pandas._libs.missing import is_matching_na as is_matching_na
from pandas._libs.sparse import SparseIndex as SparseIndex
from pandas.core.algorithms import take_nd as take_nd
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntervalArray as IntervalArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin as DatetimeLikeArrayMixin
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.dtypes.common import is_bool as is_bool, is_categorical_dtype as is_categorical_dtype, is_extension_array_dtype as is_extension_array_dtype, is_interval_dtype as is_interval_dtype, is_number as is_number, is_numeric_dtype as is_numeric_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, PandasDtype as PandasDtype
from pandas.core.dtypes.missing import array_equivalent as array_equivalent
from pandas.core.indexes.api import safe_sort_index as safe_sort_index
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal

def assert_almost_equal(left, right, check_dtype: Union[bool, Literal['equiv']] = ..., check_less_precise: Union[bool, int, NoDefault] = ..., rtol: float = ..., atol: float = ..., **kwargs) -> None: ...
def assert_dict_equal(left, right, compare_keys: bool = ...) -> None: ...
def assert_index_equal(left: Index, right: Index, exact: Union[bool, str] = ..., check_names: bool = ..., check_less_precise: Union[bool, int, NoDefault] = ..., check_exact: bool = ..., check_categorical: bool = ..., check_order: bool = ..., rtol: float = ..., atol: float = ..., obj: str = ...) -> None: ...
def assert_class_equal(left, right, exact: Union[bool, str] = ..., obj: str = ...) -> None: ...
def assert_attr_equal(attr: str, left, right, obj: str = ...) -> None: ...
def assert_is_valid_plot_return_object(objs) -> None: ...
def assert_is_sorted(seq) -> None: ...
def assert_categorical_equal(left, right, check_dtype: bool = ..., check_category_order: bool = ..., obj: str = ...) -> None: ...
def assert_interval_array_equal(left, right, exact: str = ..., obj: str = ...) -> None: ...
def assert_period_array_equal(left, right, obj: str = ...) -> None: ...
def assert_datetime_array_equal(left, right, obj: str = ..., check_freq: bool = ...) -> None: ...
def assert_timedelta_array_equal(left, right, obj: str = ..., check_freq: bool = ...) -> None: ...
def raise_assert_detail(obj, message, left, right, diff: Incomplete | None = ..., index_values: Incomplete | None = ...) -> None: ...
def assert_numpy_array_equal(left, right, strict_nan: bool = ..., check_dtype: Union[bool, Literal['equiv']] = ..., err_msg: Incomplete | None = ..., check_same: Incomplete | None = ..., obj: str = ..., index_values: Incomplete | None = ...) -> None: ...
def assert_extension_array_equal(left, right, check_dtype: Union[bool, Literal['equiv']] = ..., index_values: Incomplete | None = ..., check_less_precise=..., check_exact: bool = ..., rtol: float = ..., atol: float = ...) -> None: ...
def assert_series_equal(left, right, check_dtype: Union[bool, Literal['equiv']] = ..., check_index_type: Union[bool, Literal['equiv']] = ..., check_series_type: bool = ..., check_less_precise: Union[bool, int, NoDefault] = ..., check_names: bool = ..., check_exact: bool = ..., check_datetimelike_compat: bool = ..., check_categorical: bool = ..., check_category_order: bool = ..., check_freq: bool = ..., check_flags: bool = ..., rtol: float = ..., atol: float = ..., obj: str = ..., *, check_index: bool = ..., check_like: bool = ...) -> None: ...
def assert_frame_equal(left, right, check_dtype: Union[bool, Literal['equiv']] = ..., check_index_type: Union[bool, Literal['equiv']] = ..., check_column_type: str = ..., check_frame_type: bool = ..., check_less_precise=..., check_names: bool = ..., by_blocks: bool = ..., check_exact: bool = ..., check_datetimelike_compat: bool = ..., check_categorical: bool = ..., check_like: bool = ..., check_freq: bool = ..., check_flags: bool = ..., rtol: float = ..., atol: float = ..., obj: str = ...) -> None: ...
def assert_equal(left, right, **kwargs) -> None: ...
def assert_sp_array_equal(left, right) -> None: ...
def assert_contains_all(iterable, dic) -> None: ...
def assert_copy(iter1, iter2, **eql_kwargs) -> None: ...
def is_extension_array_dtype_and_needs_i8_conversion(left_dtype, right_dtype) -> bool: ...
def assert_indexing_slices_equivalent(ser: Series, l_slc: slice, i_slc: slice) -> None: ...
def assert_metadata_equivalent(left, right) -> None: ...
