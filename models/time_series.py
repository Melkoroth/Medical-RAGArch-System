from neuralprophet import NeuralProphet
import pandas as pd

def generate_time_series_forecast():
    data = pd.DataFrame({
        'ds': pd.date_range(start='2024-01-01', periods=30, freq='D'),
        'y': [i + (i % 7) * 2 for i in range(30)]
    })

    model = NeuralProphet()
    model.fit(data, freq="D")
    future = model.make_future_dataframe(data, periods=10)
    forecast = model.predict(future)
    model.plot(forecast).savefig("forecast_example.png")

generate_time_series_forecast()
