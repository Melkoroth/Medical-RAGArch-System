
# Dashboards Interactivos con Dash

import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

# Inicialización de la aplicación Dash
app = dash.Dash(__name__)

# Ejemplo de Datos de Series Temporales
df = pd.DataFrame({
    'Fecha': pd.date_range(start='2023-01-01', periods=30),
    'Valor': [x**2 for x in range(30)]
})

# Gráfico interactivo de Series Temporales
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Fecha'], y=df['Valor'], mode='lines', name='Tendencia'))

# Layout de la aplicación Dash
app.layout = html.Div(children=[
    html.H1(children='Dashboards Interactivos de Series Temporales'),
    dcc.Graph(id='grafico-tendencia', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
