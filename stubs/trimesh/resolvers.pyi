import abc
from . import caching as caching, util as util
from _typeshed import Incomplete
from collections.abc import Generator

class Resolver(util.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, *args, **kwargs): ...
    @abc.abstractmethod
    def get(self, key): ...
    def write(self, name, data) -> None: ...
    def namespaced(self, namespace) -> None: ...
    def __getitem__(self, key): ...

class FilePathResolver(Resolver):
    clean: Incomplete
    parent: Incomplete
    def __init__(self, source) -> None: ...
    def keys(self) -> Generator[Incomplete, None, None]: ...
    def get(self, name): ...
    def write(self, name, data) -> None: ...

class ZipResolver(Resolver):
    archive: Incomplete
    namespace: Incomplete
    def __init__(self, archive, namespace: Incomplete | None = ...) -> None: ...
    def keys(self): ...
    def get(self, name): ...
    def namespaced(self, namespace): ...

class WebResolver(Resolver):
    base_url: Incomplete
    def __init__(self, url) -> None: ...
    def get(self, name): ...

class GithubResolver(Resolver):
    url: Incomplete
    cache: Incomplete
    def __init__(self, repo, branch: Incomplete | None = ..., commit: Incomplete | None = ..., save: Incomplete | None = ...) -> None: ...
    def keys(self): ...
    @property
    def zipped(self): ...
    def get(self, key): ...
    def namespaced(self, namespace): ...

def nearby_names(name, namespace: Incomplete | None = ...) -> Generator[Incomplete, None, Incomplete]: ...
