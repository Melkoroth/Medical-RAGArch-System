
# Predicciones de Series Temporales con Prophet y pmdarima

from prophet import Prophet
from pmdarima import auto_arima
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

class TimeSeriesPredictor:
    def __init__(self, data, date_col, value_col):
        self.data = data
        self.date_col = date_col
        self.value_col = value_col

    def prophet_prediction(self, periods=30):
        df = self.data[[self.date_col, self.value_col]].rename(columns={self.date_col: 'ds', self.value_col: 'y'})
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        self.plot_prophet(df, forecast)
        return forecast

    def plot_prophet(self, df, forecast):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Actual'))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted'))
        fig.update_layout(title='Predicciones de Series Temporales con Prophet')
        fig.show()
