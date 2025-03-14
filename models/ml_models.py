import lightgbm as lgb
import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Datos de ejemplo para entrenamiento
X, y = np.random.rand(100, 5), np.random.rand(100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo con LightGBM
lgb_train = lgb.Dataset(X_train, label=y_train)
lgb_eval = lgb.Dataset(X_test, label=y_test, reference=lgb_train)
params = {"objective": "regression", "metric": "rmse"}
lgb_model = lgb.train(params, lgb_train, valid_sets=[lgb_eval], num_boost_round=100)

y_pred_lgb = lgb_model.predict(X_test)
print(f"LightGBM MSE: {mean_squared_error(y_test, y_pred_lgb)}")

# Modelo con XGBoost
xgb_model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

print(f"XGBoost MSE: {mean_squared_error(y_test, y_pred_xgb)}")
