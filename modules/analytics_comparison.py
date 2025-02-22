
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import numpy as np

def seleccionar_modelo_serie_temporal(serie):
    # Detección de estacionalidad no lineal o eventos irregulares
    if detectar_estacionalidad_no_lineal(serie):
        modelo = Prophet()
    else:
        modelo = ARIMA(serie, order=(5,1,0))
    return modelo

def entrenar_y_evaluar_modelo(modelo, serie_entrenamiento, serie_prueba):
    modelo_entrenado = modelo.fit()
    predicciones = modelo_entrenado.forecast(steps=len(serie_prueba))
    rmse = np.sqrt(np.mean((predicciones - serie_prueba)**2))
    return rmse, predicciones
import matplotlib.pyplot as plt
import json

def plot_clinical_trends(data_file):
    """Genera un gráfico de tendencia a partir de analíticas previas almacenadas en JSON."""
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    for test_name, values in data.items():
        plt.figure(figsize=(8, 5))
        dates = [entry["date"] for entry in values]
        results = [entry["value"] for entry in values]

        plt.plot(dates, results, marker="o", linestyle="-", label=test_name)
        plt.xlabel("Fecha")
        plt.ylabel("Valor Clínico")
        plt.title(f"Evolución de {test_name}")
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()
