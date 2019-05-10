#pythran export numexpr(int)
def numexpr(n):
    import numpy as np
    return np.sum(3 * np.arange(n, dtype=float))
