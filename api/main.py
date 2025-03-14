from fastapi import FastAPI, HTTPException
import requests
import os
import logging
from fastapi.middleware.cors import CORSMiddleware
from modules.ml_forecasting import predict_future_values
from modules.nlp.intelligent_context import analyze_text
from autogluon.tabular import TabularPredictor
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

app = FastAPI()

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Habilitar CORS para compatibilidad con el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de API Keys desde variables de entorno
API_KEYS = {
    "gemini": os.getenv("GEMINI_API_KEY", ""),
    "claude": os.getenv("CLAUDE_API_KEY", ""),
    "mistral": os.getenv("MISTRAL_API_KEY", ""),
    "llama": os.getenv("LLAMA_API_KEY", ""),
    "cohere": os.getenv("COHERE_API_KEY", ""),
    "deepseek": os.getenv("DEEPSEEK_API_KEY", "")
}

CHAT_ONLY_MODELS = ["chatgpt"]
DUAL_MODE_MODELS = ["gemini", "claude", "mistral", "llama", "cohere", "deepseek"]

# 📌 **Cargar Modelos IA al Inicio**
MODEL_PATH_ML = "/mnt/efs1/ml_models/autogluon_model"
MODEL_PATH_NLP = "/mnt/efs1/nlp_models/transformers_model"

# Cargar modelo ML Forecasting
predictor = None
if os.path.exists(MODEL_PATH_ML):
    try:
        predictor = TabularPredictor.load(MODEL_PATH_ML)
        logging.info("✅ Modelo ML Forecasting cargado correctamente.")
    except Exception as e:
        logging.error(f"⚠️ Error al cargar el modelo ML: {e}")

# 📌 **Cargar Modelo NLP con Verificaciones Detalladas**
nlp_pipeline = None
if os.path.exists(MODEL_PATH_NLP):
    try:
        # Verificar si la ruta contiene archivos válidos antes de cargar
        if os.path.isdir(MODEL_PATH_NLP) and any(os.scandir(MODEL_PATH_NLP)):
            logging.info("🔍 Verificación: Se encontró la ruta del modelo NLP.")
            tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH_NLP)
            model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH_NLP)
            nlp_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)
            logging.info("✅ Modelo NLP cargado correctamente.")
        else:
            logging.error("⚠️ Ruta del modelo NLP encontrada, pero está vacía o no contiene un modelo válido.")
    except Exception as e:
        logging.error(f"⚠️ Error al cargar el modelo NLP: {e}")
else:
    logging.error("⚠️ Ruta del modelo NLP no encontrada.")

@app.post("/ask_auto")
async def ask_auto(prompt: dict):
    """Selecciona automáticamente el mejor modelo IA para responder."""
    query = prompt.get("prompt", "").lower()
    
    if "predecir" in query or "futuro" in query:
        if predictor:
            return {"modelo_usado": "ML Forecasting", "resultado": predictor.predict({})}
        else:
            return {"error": "Modelo ML no disponible."}
    
    if "resumen" in query or "extraer" in query:
        if nlp_pipeline:
            return {"modelo_usado": "NLP", "resultado": nlp_pipeline(query)}
        else:
            return {"error": "Modelo NLP no disponible."}
    
    for model in DUAL_MODE_MODELS:
        if model in API_KEYS and API_KEYS[model]:
            return await call_ai_api(model, query)
    
    return {"error": "No se encontró un modelo adecuado para esta consulta."}

@app.post("/ask/{model}")
async def ask_ai(model: str, prompt: dict):
    """Permite al usuario elegir manualmente qué modelo de IA utilizar."""
    if model in CHAT_ONLY_MODELS:
        return {"error": f"{model} solo funciona en modo chat y debe usarse a través de su propia plataforma."}
    
    if model not in API_KEYS or not API_KEYS[model]:
        raise HTTPException(status_code=404, detail="Modelo no soportado o API Key no configurada.")

    return await call_ai_api(model, prompt.get("prompt", ""))

@app.get("/models")
async def list_models():
    return {"chat_only_models": CHAT_ONLY_MODELS, "dual_mode_models": DUAL_MODE_MODELS}

@app.get("/health")
async def health_check():
    return {"status": "running"}
