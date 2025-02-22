
# analytics_comparison.py

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class TimeSeriesComparison:
    def __init__(self, data, date_col, value_col, freq='D'):
        self.data = data.copy()
        self.data[date_col] = pd.to_datetime(self.data[date_col])
        self.data.set_index(date_col, inplace=True)
        self.data = self.data.resample(freq).mean().fillna(method='ffill')
        self.value_col = value_col

    def fit_predict_prophet(self):
        df = self.data.reset_index().rename(columns={'index': 'ds', self.value_col: 'y'})
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    def fit_predict_arima(self, order=(5, 1, 0)):
        model = ARIMA(self.data[self.value_col], order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=30)
        return forecast

    def calculate_rmse(self, actual, predicted):
        return sqrt(mean_squared_error(actual, predicted))

    def compare_models(self):
        # Prophet
        prophet_forecast = self.fit_predict_prophet()
        prophet_rmse = self.calculate_rmse(self.data[self.value_col][-30:], prophet_forecast['yhat'][-30:])

        # ARIMA
        arima_forecast = self.fit_predict_arima()
        arima_rmse = self.calculate_rmse(self.data[self.value_col][-30:], arima_forecast)

        if prophet_rmse < arima_rmse:
            logging.info("Prophet is better with RMSE:", prophet_rmse)
            return 'Prophet', prophet_forecast
        else:
            logging.info("ARIMA is better with RMSE:", arima_rmse)
            return 'ARIMA', arima_forecast

    def plot_predictions(self, model_name, predictions):
        if model_name == 'Prophet':
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=self.data.index, y=self.data[self.value_col], mode='lines', name='Actual'))
            fig.add_trace(go.Scatter(x=predictions['ds'], y=predictions['yhat'], mode='lines', name='Forecast'))
            fig.show()
        elif model_name == 'ARIMA':
            plt.figure(figsize=(10, 6))
            plt.plot(self.data.index, self.data[self.value_col], label='Actual')
            plt.plot(pd.date_range(start=self.data.index[-1], periods=31, freq='D')[1:], predictions, label='Forecast')
            plt.legend()
            plt.show()

# Example Usage
if __name__ == "__main__":
    data = pd.read_csv('example_data.csv')
    ts_comparison = TimeSeriesComparison(data, 'date', 'value')
    best_model, predictions = ts_comparison.compare_models()
    ts_comparison.plot_predictions(best_model, predictions)
