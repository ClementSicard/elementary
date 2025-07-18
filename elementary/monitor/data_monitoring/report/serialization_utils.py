from typing import Any
import numpy as np


def turn_nan_or_infinity_to_str(value: Any) -> str:
    """Helper function to avoid having a bare `Infinity` or `NaN` value in the output JSON, but `"Infinity"` or `NaN` instead."""
    if np.isinf(value):
        return "Infinity"
    elif np.isnan(value):
        return "NaN"

    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable.")
