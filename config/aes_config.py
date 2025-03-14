
from aws.secrets_manager import get_secret

SECRET_NAME_AES = "MedicalRAG_AES_KEY"

secret_data = get_secret(SECRET_NAME_AES)
if secret_data:
    AES_KEY = bytes.fromhex(secret_data["AES_KEY"])
else:
    raise ValueError("❌ No se pudo obtener la clave AES desde AWS Secrets Manager.")
