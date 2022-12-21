from typing import Any, ClassVar

from typing import overload
import functools
import numpy
warn: functools.partial

class EDGE_D(numpy.signedinteger):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @overload
    def bit_count(self) -> int: ...
    @overload
    def bit_count(self) -> Any: ...
    @overload
    def bit_count(self) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __and__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lshift__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __or__(self, other) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rand__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rlshift__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __ror__(self, other) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rrshift__(self, other) -> Any: ...
    def __rshift__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __rxor__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...
    def __xor__(self, other) -> Any: ...

class FLOAT_D(numpy.floating, float):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @overload
    def as_integer_ratio(self) -> Any: ...
    @overload
    def as_integer_ratio(self) -> Any: ...
    @overload
    def as_integer_ratio(self) -> Any: ...
    @overload
    def is_integer(self) -> bool: ...
    @overload
    def is_integer(self) -> Any: ...
    @overload
    def is_integer(self) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...

class INDEX_D(numpy.signedinteger):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @overload
    def bit_count(self) -> int: ...
    @overload
    def bit_count(self) -> Any: ...
    @overload
    def bit_count(self) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __and__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lshift__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __or__(self, other) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rand__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rlshift__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __ror__(self, other) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rrshift__(self, other) -> Any: ...
    def __rshift__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __rxor__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...
    def __xor__(self, other) -> Any: ...

class MCP:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    offsets: Any
    def __init__(self, costs, offsets = ..., fully_connected = ..., sampling = ...) -> Any: ...
    def _reset(self) -> Any: ...
    def find_costs(self, *args, **kwargs) -> Any: ...
    def goal_reached(self, intindex, floatcumcost) -> Any: ...
    def traceback(self, end) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class MCP_Connect(MCP):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _reset(self, *args, **kwargs) -> Any: ...
    def create_connection(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class MCP_Flexible(MCP):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def examine_neighbor(self, index, new_index, offset_length) -> Any: ...
    def travel_cost(self, old_cost, new_cost, offset_length) -> Any: ...
    def update_node(self, index, new_index, offset_length) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class MCP_Geometric(MCP):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, costs, offsets = ..., fully_connected = ..., sampling = ...) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class OFFSETS_INDEX_D(numpy.signedinteger):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @overload
    def bit_count(self) -> int: ...
    @overload
    def bit_count(self) -> Any: ...
    @overload
    def bit_count(self) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __and__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lshift__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __or__(self, other) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rand__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rlshift__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __ror__(self, other) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rrshift__(self, other) -> Any: ...
    def __rshift__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __rxor__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...
    def __xor__(self, other) -> Any: ...

class OFFSET_D(numpy.signedinteger):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @overload
    def bit_count(self) -> int: ...
    @overload
    def bit_count(self) -> Any: ...
    @overload
    def bit_count(self) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __and__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lshift__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __or__(self, other) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rand__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rlshift__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __ror__(self, other) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rrshift__(self, other) -> Any: ...
    def __rshift__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __rxor__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...
    def __xor__(self, other) -> Any: ...

def __pyx_unpickle_Enum(*args, **kwargs) -> Any: ...
def __pyx_unpickle_MCP(*args, **kwargs) -> Any: ...
def __pyx_unpickle_MCP_Connect(*args, **kwargs) -> Any: ...
def __pyx_unpickle_MCP_Flexible(*args, **kwargs) -> Any: ...
def __pyx_unpickle_MCP_Geometric(*args, **kwargs) -> Any: ...
def _get_edge_map(*args, **kwargs) -> Any: ...
def _normalize_indices(indices, shape) -> Any: ...
def _offset_edge_map(*args, **kwargs) -> Any: ...
def _ravel_index_fortran(flat_indices, shape) -> Any: ...
def _reverse(*args, **kwargs) -> Any: ...
def _unravel_index_fortran(flat_indices, shape) -> Any: ...
def make_offsets(*args, **kwargs) -> Any: ...
