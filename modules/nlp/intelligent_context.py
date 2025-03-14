from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
import os
import torch

MODEL_PATH = "/mnt/efs1/nlp_models/transformers_model"

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

# 📌 **Automatización del `learning_rate` con adaptación al hardware**
def get_adaptive_learning_rate(base_lr=2e-5, scale_factor=0.1):
    """Ajusta el learning rate dinámicamente según la capacidad del hardware."""
    return base_lr * (scale_factor if torch.cuda.is_available() else scale_factor * 0.5)

learning_rate = get_adaptive_learning_rate()

# Cargar modelo automáticamente al iniciar
if os.path.exists(MODEL_PATH):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH).to(device)
    nlp_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
else:
    tokenizer, model, nlp_pipeline = None, None, None

def analyze_text(text):
    """Analiza el texto utilizando el modelo NLP y devuelve la clasificación."""
    if nlp_pipeline:
        return nlp_pipeline(text)
    return {"error": "Modelo NLP no disponible."}

def fine_tune_nlp(train_dataset, eval_dataset):
    """Realiza fine-tuning del modelo NLP con los nuevos datos y lo guarda."""
    global model, tokenizer, nlp_pipeline
    if model and tokenizer:
        training_args = TrainingArguments(
            output_dir=MODEL_PATH,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            learning_rate=learning_rate,  # Automatización aplicada
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            num_train_epochs=epochs,
            weight_decay=0.01,
            save_total_limit=1,
            logging_dir="./logs",
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
        )

        trainer.train()
        trainer.save_model(MODEL_PATH)
        tokenizer.save_pretrained(MODEL_PATH)
        
        # 📌 **Recargar el modelo actualizado después del fine-tuning**
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH).to(device)
        nlp_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

        return {"status": "Modelo NLP actualizado y guardado correctamente."}
    return {"error": "No se pudo realizar fine-tuning del modelo NLP."}
