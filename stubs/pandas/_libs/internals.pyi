from typing import Any, ClassVar

class Block(SharedBlock):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    values: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class BlockManager:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    _blklocs: Any
    _blknos: Any
    _is_consolidated: Any
    _known_consolidated: Any
    axes: Any
    blocks: Any
    parent: Any
    refs: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def _post_setstate(self, *args, **kwargs) -> Any: ...
    def _rebuild_blknos_and_blklocs(self, *args, **kwargs) -> Any: ...
    def get_slice(self, *args, **kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class BlockPlacement:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    as_array: Any
    as_slice: Any
    indexer: Any
    is_slice_like: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def add(self, *args, **kwargs) -> Any: ...
    def append(self, *args, **kwargs) -> Any: ...
    def delete(self, *args, **kwargs) -> Any: ...
    def increment_above(self, *args, **kwargs) -> Any: ...
    def tile_for_unstack(self, *args, **kwargs) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class NDArrayBackedBlock(SharedBlock):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    values: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def getitem_block_index(self, *args, **kwargs) -> Any: ...

class NumpyBlock(SharedBlock):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    values: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def getitem_block_index(self, *args, **kwargs) -> Any: ...

class SharedBlock:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    _mgr_locs: Any
    ndim: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class defaultdict(dict):
    default_factory: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def copy(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __class_getitem__(cls, *args, **kwargs) -> Any: ...
    def __copy__(self) -> Any: ...
    def __missing__(self, key) -> Any: ...
    def __or__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __ror__(self, other) -> Any: ...

def __pyx_unpickle_Enum(*args, **kwargs) -> Any: ...
def _unpickle_block(*args, **kwargs) -> Any: ...
def ensure_int64(*args, **kwargs) -> Any: ...
def get_blkno_indexers(*args, **kwargs) -> Any: ...
def get_blkno_placements(*args, **kwargs) -> Any: ...
def slice_len(*args, **kwargs) -> Any: ...
def update_blklocs_and_blknos(*args, **kwargs) -> Any: ...
