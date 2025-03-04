"""
Optimización con TensorFlow XLA para mejorar rendimiento en CPUs modernas.
"""

import tensorflow as tf
from tensorflow.python.compiler.xla import xla

def optimized_tensorflow_model():
    """
    Configura TensorFlow para utilizar XLA y optimizar la ejecución.
    """
    tf.config.optimizer.set_jit(True)  # Activa XLA (Accelerated Linear Algebra)
    return "TensorFlow XLA activado para optimización"
