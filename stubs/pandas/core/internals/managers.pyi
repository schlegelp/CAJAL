import numpy as np
import weakref
from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._libs import internals as libinternals, lib as lib
from pandas._libs.internals import BlockPlacement as BlockPlacement
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, Shape as Shape, npt as npt, type_t as type_t
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.cast import infer_dtype_from_scalar as infer_dtype_from_scalar
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_dtype_equal as is_dtype_equal, is_list_like as is_list_like
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import array_equals as array_equals, isna as isna
from pandas.core.indexers import maybe_convert_indices as maybe_convert_indices
from pandas.core.indexes.api import Float64Index as Float64Index, Index as Index, ensure_index as ensure_index
from pandas.core.internals.base import DataManager as DataManager, SingleDataManager as SingleDataManager, interleaved_dtype as interleaved_dtype
from pandas.core.internals.blocks import Block as Block, DatetimeTZBlock as DatetimeTZBlock, NumpyBlock as NumpyBlock, ensure_block_shape as ensure_block_shape, extend_blocks as extend_blocks, get_block_type as get_block_type, new_block as new_block, new_block_2d as new_block_2d
from pandas.core.internals.ops import blockwise_all as blockwise_all, operate_blockwise as operate_blockwise
from pandas.errors import PerformanceWarning as PerformanceWarning
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Callable, Hashable, Literal, Sequence, TypeVar

T = TypeVar('T', bound='BaseBlockManager')

class BaseBlockManager(DataManager):
    blocks: tuple[Block, ...]
    axes: list[Index]
    refs: Union[list[Union[weakref.ref, None]], None]
    parent: object
    @property
    def ndim(self) -> int: ...
    def __init__(self, blocks, axes, refs: Incomplete | None = ..., verify_integrity: bool = ...) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index], refs: Union[list[Union[weakref.ref, None]], None] = ..., parent: object = ...) -> T: ...
    @property
    def blknos(self) -> npt.NDArray[np.intp]: ...
    @property
    def blklocs(self) -> npt.NDArray[np.intp]: ...
    def make_empty(self, axes: Incomplete | None = ...) -> T: ...
    def __nonzero__(self) -> bool: ...
    __bool__: Incomplete
    def set_axis(self, axis: int, new_labels: Index) -> None: ...
    @property
    def is_single_block(self) -> bool: ...
    @property
    def items(self) -> Index: ...
    def get_dtypes(self): ...
    @property
    def arrays(self) -> list[ArrayLike]: ...
    def apply(self, f, align_keys: Union[list[str], None] = ..., ignore_failures: bool = ..., **kwargs) -> T: ...
    def where(self, other, cond, align: bool) -> T: ...
    def setitem(self, indexer, value) -> T: ...
    def putmask(self, mask, new, align: bool = ...): ...
    def diff(self, n: int, axis: int) -> T: ...
    def interpolate(self, **kwargs) -> T: ...
    def shift(self, periods: int, axis: int, fill_value) -> T: ...
    def fillna(self, value, limit, inplace: bool, downcast) -> T: ...
    def astype(self, dtype, copy: bool = ..., errors: str = ...) -> T: ...
    def convert(self, copy: bool = ..., datetime: bool = ..., numeric: bool = ..., timedelta: bool = ...) -> T: ...
    def replace(self, to_replace, value, inplace: bool) -> T: ...
    def replace_regex(self, **kwargs): ...
    def replace_list(self, src_list: list[Any], dest_list: list[Any], inplace: bool = ..., regex: bool = ...) -> T: ...
    def to_native_types(self, **kwargs) -> T: ...
    @property
    def is_numeric_mixed_type(self) -> bool: ...
    @property
    def any_extension_types(self) -> bool: ...
    @property
    def is_view(self) -> bool: ...
    def get_bool_data(self, copy: bool = ...) -> T: ...
    def get_numeric_data(self, copy: bool = ...) -> T: ...
    @property
    def nblocks(self) -> int: ...
    def copy(self, deep: bool = ...) -> T: ...
    def consolidate(self) -> T: ...
    def reindex_indexer(self, new_axis: Index, indexer: Union[npt.NDArray[np.intp], None], axis: int, fill_value: Incomplete | None = ..., allow_dups: bool = ..., copy: Union[bool, None] = ..., only_slice: bool = ..., *, use_na_proxy: bool = ...) -> T: ...
    def take(self, indexer, axis: int = ..., verify: bool = ..., convert_indices: bool = ...) -> T: ...

class BlockManager(libinternals.BlockManager, BaseBlockManager):
    ndim: int
    def __init__(self, blocks: Sequence[Block], axes: Sequence[Index], refs: Union[list[Union[weakref.ref, None]], None] = ..., parent: object = ..., verify_integrity: bool = ...) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index], refs: Union[list[Union[weakref.ref, None]], None] = ..., parent: object = ...) -> BlockManager: ...
    def fast_xs(self, loc: int) -> SingleBlockManager: ...
    def iget(self, i: int, track_ref: bool = ...) -> SingleBlockManager: ...
    def iget_values(self, i: int) -> ArrayLike: ...
    @property
    def column_arrays(self) -> list[np.ndarray]: ...
    blocks: Incomplete
    refs: Incomplete
    def iset(self, loc: Union[int, slice, np.ndarray], value: ArrayLike, inplace: bool = ...): ...
    def column_setitem(self, loc: int, idx: Union[int, slice, np.ndarray], value) -> None: ...
    def insert(self, loc: int, item: Hashable, value: ArrayLike) -> None: ...
    def idelete(self, indexer) -> BlockManager: ...
    def grouped_reduce(self, func: Callable, ignore_failures: bool = ...) -> T: ...
    def reduce(self, func: Callable, ignore_failures: bool = ...) -> tuple[T, np.ndarray]: ...
    def operate_blockwise(self, other: BlockManager, array_op) -> BlockManager: ...
    def quantile(self, *, qs: Float64Index, axis: int = ..., interpolation: str = ...) -> T: ...
    def unstack(self, unstacker, fill_value) -> BlockManager: ...
    def to_dict(self, copy: bool = ...): ...
    def as_array(self, dtype: Union[np.dtype, None] = ..., copy: bool = ..., na_value: object = ...) -> np.ndarray: ...
    def is_consolidated(self) -> bool: ...

class SingleBlockManager(BaseBlockManager, SingleDataManager):
    @property
    def ndim(self) -> Literal[1]: ...
    is_single_block: bool
    axes: Incomplete
    blocks: Incomplete
    refs: Incomplete
    parent: Incomplete
    def __init__(self, block: Block, axis: Index, refs: Union[list[Union[weakref.ref, None]], None] = ..., parent: object = ..., verify_integrity: bool = ..., fastpath=...) -> None: ...
    @classmethod
    def from_blocks(cls, blocks: list[Block], axes: list[Index], refs: Union[list[Union[weakref.ref, None]], None] = ..., parent: object = ...) -> SingleBlockManager: ...
    @classmethod
    def from_array(cls, array: ArrayLike, index: Index) -> SingleBlockManager: ...
    def to_2d_mgr(self, columns: Index) -> BlockManager: ...
    def getitem_mgr(self, indexer: Union[slice, npt.NDArray[np.bool_]]) -> SingleBlockManager: ...
    def get_slice(self, slobj: slice, axis: int = ...) -> SingleBlockManager: ...
    @property
    def index(self) -> Index: ...
    @property
    def dtype(self) -> DtypeObj: ...
    def get_dtypes(self) -> np.ndarray: ...
    def external_values(self): ...
    def internal_values(self): ...
    def array_values(self): ...
    def get_numeric_data(self, copy: bool = ...): ...
    def setitem_inplace(self, indexer, value) -> None: ...
    def idelete(self, indexer) -> SingleBlockManager: ...
    def fast_xs(self, loc) -> None: ...
    def set_values(self, values: ArrayLike): ...

def create_block_manager_from_blocks(blocks: list[Block], axes: list[Index], consolidate: bool = ..., verify_integrity: bool = ...) -> BlockManager: ...
def create_block_manager_from_column_arrays(arrays: list[ArrayLike], axes: list[Index], consolidate: bool = ...) -> BlockManager: ...
def construction_error(tot_items: int, block_shape: Shape, axes: list[Index], e: Union[ValueError, None] = ...): ...
