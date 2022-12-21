from pandas._config import get_option as get_option
from pandas.core.dtypes.inference import is_sequence as is_sequence
from typing import Any, Callable, Dict, Iterable, Mapping, Union

EscapeChars = Union[Mapping[str, str], Iterable[str]]

def adjoin(space: int, *lists: list[str], **kwargs) -> str: ...
def justify(texts: Iterable[str], max_len: int, mode: str = ...) -> list[str]: ...
def pprint_thing(thing: Any, _nest_lvl: int = ..., escape_chars: Union[EscapeChars, None] = ..., default_escapes: bool = ..., quote_strings: bool = ..., max_seq_items: Union[int, None] = ...) -> str: ...
def pprint_thing_encoded(object, encoding: str = ..., errors: str = ...) -> bytes: ...
def enable_data_resource_formatter(enable: bool) -> None: ...
def default_pprint(thing: Any, max_seq_items: Union[int, None] = ...) -> str: ...
def format_object_summary(obj, formatter: Callable, is_justify: bool = ..., name: Union[str, None] = ..., indent_for_name: bool = ..., line_break_each_value: bool = ...) -> str: ...

class PrettyDict(Dict[_KT, _VT]): ...
