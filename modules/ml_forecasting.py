from autogluon.tabular import TabularPredictor
import os
import torch

MODEL_PATH = "/mnt/efs1/ml_models/autogluon_model"

# 📌 **Detección automática de GPU o CPU**
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 📌 **Ajuste Automático del Tamaño de Lote**
def get_optimal_batch_size(base_size=32):
    """Ajusta automáticamente el tamaño de lote según la memoria disponible."""
    try:
        if torch.cuda.is_available():
            total_mem = torch.cuda.get_device_properties(0).total_memory
            return min(512, max(base_size, int(total_mem / 1024**3 * 64)))
        return base_size  # Si no hay GPU, usa el tamaño base
    except:
        return base_size

batch_size = get_optimal_batch_size()

# 📌 **Ajuste Automático del Número de Épocas**
epochs = 3 if torch.cuda.is_available() else 1

# 📌 **Automatización del `learning_rate` basado en la cantidad de datos**
def get_adaptive_learning_rate(base_lr=0.001, scale_factor=0.1):
    """Calcula un learning rate adaptativo en función de la capacidad de hardware."""
    return base_lr * (scale_factor if torch.cuda.is_available() else scale_factor * 0.5)

learning_rate = get_adaptive_learning_rate()

# Cargar modelo automáticamente al iniciar
if os.path.exists(MODEL_PATH):
    predictor = TabularPredictor.load(MODEL_PATH)
else:
    predictor = None

def predict_future_values(data):
    """Realiza una predicción basada en los datos de entrada."""
    if predictor:
        return predictor.predict(data)
    return {"error": "Modelo no disponible."}

def train_model(data, label_column):
    """Entrena o reentrena el modelo con nuevos datos y guarda su progreso."""
    global predictor
    predictor = TabularPredictor(label=label_column).fit(data)
    predictor.save(MODEL_PATH)
    return {"status": "Modelo actualizado y guardado correctamente."}
