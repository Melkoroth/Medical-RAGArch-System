
# Optimización de Machine Learning con scikit-learn-intelex

from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de Ejemplo
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Modelo de Regresión Lineal Optimizado
model = LinearRegression()
model.fit(X, y)

# Predicción con modelo optimizado
pred = model.predict(np.array([[6]]))
print(f"Predicción optimizada para 6: {pred[0]}")
