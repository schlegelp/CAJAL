from _typeshed import Incomplete
from trimesh import util as util

def cylinder_inertia(mass, radius, height, transform: Incomplete | None = ...): ...
def sphere_inertia(mass, radius): ...
def principal_axis(inertia): ...
def transform_inertia(transform, inertia_tensor): ...
def radial_symmetry(mesh): ...
