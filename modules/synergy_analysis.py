"""
Módulo de sinergias optimizado con paralelización en joblib/Dask.
"""

import numpy as np
from sklearn.linear_model import Ridge
from joblib import Parallel, delayed
import dask.array as da

def train_synergy_model(X, y):
    """
    Entrena un modelo de regresión Ridge con paralelización.
    """
    model = Ridge(alpha=1.0)
    model.fit(X, y)
    return model

def predict_synergy_effect(model, new_supplements):
    """
    Predice el impacto de nuevas combinaciones de suplementos con múltiples hilos.
    """
    predictions = Parallel(n_jobs=-1)(delayed(model.predict)([supp]) for supp in new_supplements)
    return np.array(predictions).flatten()
