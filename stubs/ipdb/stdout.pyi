from .__main__ import post_mortem as post_mortem, set_trace as set_trace
from _typeshed import Incomplete
from collections.abc import Generator

def update_stdout() -> None: ...
def sset_trace(frame: Incomplete | None = ..., context: int = ...) -> None: ...
def spost_mortem(tb: Incomplete | None = ...) -> None: ...
def spm() -> None: ...
def slaunch_ipdb_on_exception() -> Generator[None, None, None]: ...
