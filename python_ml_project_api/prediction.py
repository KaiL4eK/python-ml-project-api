from typing import Any

import numpy as np


def predict(data: np.ndarray[Any, np.dtype[Any]]) -> int:
    return int(np.sum(data))
