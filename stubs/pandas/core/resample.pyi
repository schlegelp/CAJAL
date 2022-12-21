from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._libs import lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, IncompatibleFrequency as IncompatibleFrequency, NaT as NaT, Period as Period, Timedelta as Timedelta, Timestamp as Timestamp, to_offset as to_offset
from pandas._typing import IndexLabel as IndexLabel, NDFrameT as NDFrameT, T as T, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes, TimestampConvertibleTypes as TimestampConvertibleTypes, npt as npt
from pandas.core.apply import ResamplerWindowApply as ResamplerWindowApply
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import SeriesGroupBy as SeriesGroupBy
from pandas.core.groupby.groupby import BaseGroupBy as BaseGroupBy, GroupBy as GroupBy, get_groupby as get_groupby
from pandas.core.groupby.grouper import Grouper as Grouper
from pandas.core.groupby.ops import BinGrouper as BinGrouper
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.period import PeriodIndex as PeriodIndex, period_range as period_range
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.errors import AbstractMethodError as AbstractMethodError, DataError as DataError
from pandas.tseries.frequencies import is_subperiod as is_subperiod, is_superperiod as is_superperiod
from pandas.tseries.offsets import DateOffset as DateOffset, Day as Day, Nano as Nano, Tick as Tick
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Callable, Hashable, Literal

class Resampler(BaseGroupBy, PandasObject):
    grouper: BinGrouper
    exclusions: frozenset[Hashable]
    groupby: Incomplete
    keys: Incomplete
    sort: bool
    axis: Incomplete
    kind: Incomplete
    squeeze: bool
    group_keys: Incomplete
    as_index: bool
    def __init__(self, obj: Union[DataFrame, Series], groupby: TimeGrouper, axis: int = ..., kind: Incomplete | None = ..., *, group_keys: Union[bool, lib.NoDefault] = ..., selection: Incomplete | None = ..., **kwargs) -> None: ...
    def __getattr__(self, attr: str): ...
    @property
    def obj(self) -> NDFrame: ...
    @property
    def ax(self): ...
    def pipe(self, func: Union[Callable[..., T], tuple[Callable[..., T], str]], *args, **kwargs) -> T: ...
    def aggregate(self, func: Incomplete | None = ..., *args, **kwargs): ...
    agg: Incomplete
    apply: Incomplete
    def transform(self, arg, *args, **kwargs): ...
    def ffill(self, limit: Incomplete | None = ...): ...
    def pad(self, limit: Incomplete | None = ...): ...
    def nearest(self, limit: Incomplete | None = ...): ...
    def bfill(self, limit: Incomplete | None = ...): ...
    def backfill(self, limit: Incomplete | None = ...): ...
    def fillna(self, method, limit: Incomplete | None = ...): ...
    def interpolate(self, method: str = ..., axis: int = ..., limit: Incomplete | None = ..., inplace: bool = ..., limit_direction: str = ..., limit_area: Incomplete | None = ..., downcast: Incomplete | None = ..., **kwargs): ...
    def asfreq(self, fill_value: Incomplete | None = ...): ...
    def std(self, ddof: int = ..., numeric_only: Union[bool, lib.NoDefault] = ..., *args, **kwargs): ...
    def var(self, ddof: int = ..., numeric_only: Union[bool, lib.NoDefault] = ..., *args, **kwargs): ...
    def size(self): ...
    def count(self): ...
    def quantile(self, q: float = ..., **kwargs): ...

class _GroupByMixin(PandasObject):
    binner: Incomplete
    key: Incomplete
    groupby: Incomplete
    def __init__(self, obj, parent: Incomplete | None = ..., groupby: Incomplete | None = ..., key: Incomplete | None = ..., **kwargs) -> None: ...

class DatetimeIndexResampler(Resampler): ...
class DatetimeIndexResamplerGroupby(_GroupByMixin, DatetimeIndexResampler): ...
class PeriodIndexResampler(DatetimeIndexResampler): ...
class PeriodIndexResamplerGroupby(_GroupByMixin, PeriodIndexResampler): ...
class TimedeltaIndexResampler(DatetimeIndexResampler): ...
class TimedeltaIndexResamplerGroupby(_GroupByMixin, TimedeltaIndexResampler): ...

def get_resampler(obj, kind: Incomplete | None = ..., **kwds) -> Union[DatetimeIndexResampler, PeriodIndexResampler, TimedeltaIndexResampler]: ...
def get_resampler_for_grouping(groupby, rule, how: Incomplete | None = ..., fill_method: Incomplete | None = ..., limit: Incomplete | None = ..., kind: Incomplete | None = ..., on: Incomplete | None = ..., **kwargs): ...

class TimeGrouper(Grouper):
    closed: Incomplete
    label: Incomplete
    kind: Incomplete
    convention: Incomplete
    how: Incomplete
    fill_method: Incomplete
    limit: Incomplete
    group_keys: Incomplete
    origin: Incomplete
    offset: Incomplete
    loffset: Incomplete
    def __init__(self, freq: str = ..., closed: Union[Literal['left', 'right'], None] = ..., label: Union[Literal['left', 'right'], None] = ..., how: str = ..., axis: int = ..., fill_method: Incomplete | None = ..., limit: Incomplete | None = ..., loffset: Incomplete | None = ..., kind: Union[str, None] = ..., convention: Union[Literal['start', 'end', 'e', 's'], None] = ..., base: Union[int, None] = ..., origin: Union[str, TimestampConvertibleTypes] = ..., offset: Union[TimedeltaConvertibleTypes, None] = ..., group_keys: Union[bool, lib.NoDefault] = ..., **kwargs) -> None: ...

def asfreq(obj: NDFrameT, freq, method: Incomplete | None = ..., how: Incomplete | None = ..., normalize: bool = ..., fill_value: Incomplete | None = ...) -> NDFrameT: ...
