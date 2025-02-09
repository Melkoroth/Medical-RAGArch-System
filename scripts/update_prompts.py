import requests
import os
import hashlib

HUGGING_FACE_DATASET_URL = "https://huggingface.co/datasets/YOUR_DATASET/raw/main/prompts.json"
LOCAL_PROMPT_PATH = "./data/prompts/"
BACKUP_SCRIPT = "python scripts/rollback.py backup"
ROLLBACK_SCRIPT = "python scripts/rollback.py rollback"

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def update_prompts():
    try:
        response = requests.get(HUGGING_FACE_DATASET_URL, timeout=10)
        response.raise_for_status()

        os.makedirs(LOCAL_PROMPT_PATH, exist_ok=True)
        file_path = os.path.join(LOCAL_PROMPT_PATH, "prompts.json")

        # Hacer backup antes de actualizar
        os.system(BACKUP_SCRIPT)

        with open(file_path, "wb") as f:
            f.write(response.content)

        # Verificar integridad
        new_hash = calculate_hash(file_path)
        print(f"Prompts actualizados correctamente. Hash: {new_hash}")

    except requests.exceptions.RequestException as e:
        print(f"Error al actualizar prompts: {e}")
        os.system(ROLLBACK_SCRIPT)

if __name__ == "__main__":
    update_prompts()