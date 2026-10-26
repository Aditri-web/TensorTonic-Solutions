import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    arr = np.array(x, dtype=float)
    result = 1/(1+np.exp(-arr))
    if isinstance(x,(int,float)):
        return float(result)
    return result # Write code here
    pass