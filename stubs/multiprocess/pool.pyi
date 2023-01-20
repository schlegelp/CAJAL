from _typeshed import Incomplete

class RemoteTraceback(Exception):
    tb: Incomplete
    def __init__(self, tb) -> None: ...

class ExceptionWithTraceback:
    exc: Incomplete
    tb: Incomplete
    def __init__(self, exc, tb) -> None: ...
    def __reduce__(self): ...

class MaybeEncodingError(Exception):
    exc: Incomplete
    value: Incomplete
    def __init__(self, exc, value) -> None: ...

class _PoolCache(dict):
    notifier: Incomplete
    def __init__(self, *args, notifier: Incomplete | None = ..., **kwds) -> None: ...
    def __delitem__(self, item) -> None: ...

class Pool:
    @staticmethod
    def Process(ctx, *args, **kwds): ...
    def __init__(self, processes: Incomplete | None = ..., initializer: Incomplete | None = ..., initargs=..., maxtasksperchild: Incomplete | None = ..., context: Incomplete | None = ...) -> None: ...
    def __del__(self, _warn=..., RUN=...) -> None: ...
    def apply(self, func, args=..., kwds=...): ...
    def map(self, func, iterable, chunksize: Incomplete | None = ...): ...
    def starmap(self, func, iterable, chunksize: Incomplete | None = ...): ...
    def starmap_async(self, func, iterable, chunksize: Incomplete | None = ..., callback: Incomplete | None = ..., error_callback: Incomplete | None = ...): ...
    def imap(self, func, iterable, chunksize: int = ...): ...
    def imap_unordered(self, func, iterable, chunksize: int = ...): ...
    def apply_async(self, func, args=..., kwds=..., callback: Incomplete | None = ..., error_callback: Incomplete | None = ...): ...
    def map_async(self, func, iterable, chunksize: Incomplete | None = ..., callback: Incomplete | None = ..., error_callback: Incomplete | None = ...): ...
    def __reduce__(self) -> None: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

class ApplyResult:
    def __init__(self, pool, callback, error_callback) -> None: ...
    def ready(self): ...
    def successful(self): ...
    def wait(self, timeout: Incomplete | None = ...) -> None: ...
    def get(self, timeout: Incomplete | None = ...): ...
    __class_getitem__: Incomplete
AsyncResult = ApplyResult

class MapResult(ApplyResult):
    def __init__(self, pool, chunksize, length, callback, error_callback) -> None: ...

class IMapIterator:
    def __init__(self, pool) -> None: ...
    def __iter__(self): ...
    def next(self, timeout: Incomplete | None = ...): ...
    __next__: Incomplete

class IMapUnorderedIterator(IMapIterator): ...

class ThreadPool(Pool):
    @staticmethod
    def Process(ctx, *args, **kwds): ...
    def __init__(self, processes: Incomplete | None = ..., initializer: Incomplete | None = ..., initargs=...) -> None: ...
