from ._rolling_ball_cy import apply_kernel as apply_kernel, apply_kernel_nan as apply_kernel_nan
from _typeshed import Incomplete

def rolling_ball(image, *, radius: int = ..., kernel: Incomplete | None = ..., nansafe: bool = ..., num_threads: Incomplete | None = ...): ...
def ball_kernel(radius, ndim): ...
def ellipsoid_kernel(shape, intensity): ...
