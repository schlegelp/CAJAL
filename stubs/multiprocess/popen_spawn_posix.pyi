from . import popen_fork
from _typeshed import Incomplete

class _DupFd:
    fd: Incomplete
    def __init__(self, fd) -> None: ...
    def detach(self): ...

class Popen(popen_fork.Popen):
    method: str
    DupFd: Incomplete
    def __init__(self, process_obj) -> None: ...
    def duplicate_for_child(self, fd): ...
