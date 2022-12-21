from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike
from pandas.util._exceptions import find_stack_level as find_stack_level

is_bool: Incomplete
is_integer: Incomplete
is_float: Incomplete
is_complex: Incomplete
is_scalar: Incomplete
is_decimal: Incomplete
is_interval: Incomplete
is_list_like: Incomplete
is_iterator: Incomplete

def is_number(obj) -> bool: ...
def iterable_not_string(obj) -> bool: ...
def is_file_like(obj) -> bool: ...
def is_re(obj) -> bool: ...
def is_re_compilable(obj) -> bool: ...
def is_array_like(obj) -> bool: ...
def is_nested_list_like(obj) -> bool: ...
def is_dict_like(obj) -> bool: ...
def is_named_tuple(obj) -> bool: ...
def is_hashable(obj) -> bool: ...
def is_sequence(obj) -> bool: ...
def is_dataclass(item): ...
def is_inferred_bool_dtype(arr: ArrayLike) -> bool: ...
