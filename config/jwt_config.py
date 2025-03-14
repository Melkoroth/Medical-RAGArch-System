
from aws.secrets_manager import get_secret

SECRET_NAME_JWT = "MedicalRAG_JWT_SECRET"

secret_data = get_secret(SECRET_NAME_JWT)
if secret_data:
    JWT_SECRET = secret_data["JWT_SECRET"]
else:
    raise ValueError("❌ No se pudo obtener la clave JWT desde AWS Secrets Manager.")
