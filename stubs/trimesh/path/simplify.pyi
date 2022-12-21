from . import arc as arc, entities as entities
from .. import util as util
from ..constants import log as log
from ..nsphere import fit_nsphere as fit_nsphere
from _typeshed import Incomplete

def fit_circle_check(points, scale, prior: Incomplete | None = ..., final: bool = ..., verbose: bool = ...): ...
def is_circle(points, scale, verbose: bool = ...): ...
def merge_colinear(points, scale): ...
def resample_spline(points, smooth: float = ..., count: Incomplete | None = ..., degree: int = ...): ...
def points_to_spline_entity(points, smooth: Incomplete | None = ..., count: Incomplete | None = ...): ...
def simplify_basic(drawing, process: bool = ..., **kwargs): ...
def simplify_spline(path, smooth: Incomplete | None = ..., verbose: bool = ...): ...
