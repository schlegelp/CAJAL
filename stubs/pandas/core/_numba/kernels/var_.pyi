import numpy as np
from pandas.core._numba.kernels.shared import is_monotonic_increasing as is_monotonic_increasing

def add_var(val: float, nobs: int, mean_x: float, ssqdm_x: float, compensation: float, num_consecutive_same_value: int, prev_value: float) -> tuple[int, float, float, float, int, float]: ...
def remove_var(val: float, nobs: int, mean_x: float, ssqdm_x: float, compensation: float) -> tuple[int, float, float, float]: ...
def sliding_var(values: np.ndarray, start: np.ndarray, end: np.ndarray, min_periods: int, ddof: int = ...) -> np.ndarray: ...
