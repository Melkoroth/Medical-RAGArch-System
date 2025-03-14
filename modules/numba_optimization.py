"""
Optimización con numba y numpy para mejorar eficiencia en cálculos numéricos.
"""

try:
    import numpy as np
except ImportError:
    numpy = None  # Carga opcional
try:
    from numba import jit
except ImportError:
    numba = None  # Carga opcional

@jit(nopython=True, parallel=True)
def fast_matrix_multiplication(A, B):
    """
    Multiplicación optimizada de matrices con numba y numpy.
    """
    return np.dot(A, B)
