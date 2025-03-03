"""
Optimización con numba y numpy para mejorar eficiencia en cálculos numéricos.
"""

import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def fast_matrix_multiplication(A, B):
    """
    Multiplicación optimizada de matrices con numba y numpy.
    """
    return np.dot(A, B)
