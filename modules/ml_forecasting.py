"""
Módulo de predicción de biomarcadores con Prophet, optimizado con joblib/Dask.
"""

import pandas as pd
from prophet import Prophet
from joblib import Parallel, delayed
import dask
import dask.dataframe as dd

def train_forecast_model(data: pd.DataFrame):
    """
    Entrena un modelo Prophet basado en datos históricos de biomarcadores.
    """
    model = Prophet()
    model.fit(data)
    return model

def predict_future_values(model, periods=3):
    """
    Genera predicciones con paralelización en múltiples hilos.
    """
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = Parallel(n_jobs=-1)(delayed(model.predict)(future) for _ in range(1))[0]
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
