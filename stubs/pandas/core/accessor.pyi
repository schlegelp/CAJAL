from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level

class DirNamesMixin:
    def __dir__(self) -> list[str]: ...

class PandasDelegate: ...

def delegate_names(delegate, accessors, typ: str, overwrite: bool = ...): ...

class CachedAccessor:
    def __init__(self, name: str, accessor) -> None: ...
    def __get__(self, obj, cls): ...

def register_dataframe_accessor(name): ...
def register_series_accessor(name): ...
def register_index_accessor(name): ...
