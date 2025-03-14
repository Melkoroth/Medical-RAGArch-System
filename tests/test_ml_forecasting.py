import pytest
import pandas as pd
from modules.ml_forecasting import Prophet

def test_prophet_forecast():
    data = pd.DataFrame({
        "ds": pd.date_range(start="2023-01-01", periods=30, freq="D"),
        "y": range(30)
    })
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=10)
    forecast = model.predict(future)
    assert len(forecast) > 30, "El modelo debe generar predicciones."
