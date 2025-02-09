import gradio as gr
import os
import json

LOCAL_PROMPT_PATH = "./data/prompts/prompts.json"
LOCAL_BACKUP_PATH = "./data/prompts_backup/prompts.json"

def load_prompt(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def compare_versions():
    local_data = load_prompt(LOCAL_PROMPT_PATH)
    backup_data = load_prompt(LOCAL_BACKUP_PATH)

    differences = []
    for key in local_data:
        if key in backup_data and local_data[key] != backup_data[key]:
            differences.append(f"🟡 Cambio en {key}: 
 - Anterior: {backup_data[key]}
 - Nuevo: {local_data[key]}")

    return differences if differences else ["✅ No hay cambios significativos."]

iface = gr.Interface(fn=compare_versions, inputs=[], outputs="text", title="Comparar versiones de Prompts")
iface.launch()