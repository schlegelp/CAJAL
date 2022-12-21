from . import caching as caching, grouping as grouping, transformations as transformations, util as util
from .constants import tol as tol
from .geometry import plane_transform as plane_transform
from .parent import Geometry3D as Geometry3D
from .visual.color import VertexColor as VertexColor
from _typeshed import Incomplete

def point_plane_distance(points, plane_normal, plane_origin=...): ...
def major_axis(points): ...
def plane_fit(points): ...
def radial_sort(points, origin, normal, start: Incomplete | None = ...): ...
def project_to_plane(points, plane_normal=..., plane_origin=..., transform: Incomplete | None = ..., return_transform: bool = ..., return_planar: bool = ...): ...
def remove_close(points, radius): ...
def k_means(points, k, **kwargs): ...
def tsp(points, start: int = ...): ...
def plot_points(points, show: bool = ...) -> None: ...

class PointCloud(Geometry3D):
    metadata: Incomplete
    visual: Incomplete
    def __init__(self, vertices, colors: Incomplete | None = ..., metadata: Incomplete | None = ..., **kwargs) -> None: ...
    def __setitem__(self, *args, **kwargs): ...
    def __getitem__(self, *args, **kwargs): ...
    @property
    def shape(self): ...
    @property
    def is_empty(self): ...
    def copy(self): ...
    def hash(self): ...
    def crc(self): ...
    def merge_vertices(self) -> None: ...
    def apply_transform(self, transform): ...
    @property
    def bounds(self): ...
    @property
    def extents(self): ...
    @property
    def centroid(self): ...
    @property
    def vertices(self): ...
    @vertices.setter
    def vertices(self, data) -> None: ...
    @property
    def colors(self): ...
    @colors.setter
    def colors(self, data) -> None: ...
    def kdtree(self): ...
    def convex_hull(self): ...
    def scene(self): ...
    def show(self, **kwargs) -> None: ...
    def export(self, file_obj: Incomplete | None = ..., file_type: Incomplete | None = ..., **kwargs): ...
    def query(self, input_points, **kwargs): ...
    def __add__(self, other): ...
