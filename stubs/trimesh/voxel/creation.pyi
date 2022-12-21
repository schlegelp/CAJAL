from . import base as base
from .. import grouping as grouping, remesh as remesh, util as util
from ..constants import log_time as log_time
from _typeshed import Incomplete

def voxelize_subdivide(mesh, pitch, max_iter: int = ..., edge_factor: float = ...): ...
def local_voxelize(mesh, point, pitch, radius, fill: bool = ..., **kwargs): ...
def voxelize_ray(mesh, pitch, per_cell=...): ...
def voxelize_binvox(mesh, pitch: Incomplete | None = ..., dimension: Incomplete | None = ..., bounds: Incomplete | None = ..., **binvoxer_kwargs): ...

voxelizers: Incomplete

def voxelize(mesh, pitch, method: str = ..., **kwargs): ...
