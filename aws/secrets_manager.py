
import boto3
import json
import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
SECRET_NAME_AES = "MedicalRAG_AES_KEY"
SECRET_NAME_JWT = "MedicalRAG_JWT_SECRET"

client = boto3.client("secretsmanager", region_name=AWS_REGION)

def create_secret(secret_name, secret_value):
    try:
        client.create_secret(Name=secret_name, SecretString=json.dumps(secret_value))
        print(f"✅ Se ha creado el secreto: {secret_name}")
    except client.exceptions.ResourceExistsException:
        print(f"⚠️ El secreto {secret_name} ya existe.")

# ✅ Se ha agregado verificación de existencia de clave antes de usarla
if secret_data is None:
    raise ValueError('No se pudo obtener la clave desde AWS Secrets Manager')
def get_secret(secret_name):
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response["SecretString"])
    except client.exceptions.ResourceNotFoundException:
        print(f"❌ Secreto {secret_name} no encontrado.")
        return None

# Crear secretos automáticamente si no existen
# ✅ Se ha agregado verificación de existencia de clave antes de usarla
if secret_data is None:
    raise ValueError('No se pudo obtener la clave desde AWS Secrets Manager')
if not get_secret(SECRET_NAME_AES):
    create_secret(SECRET_NAME_AES, {"AES_KEY": os.urandom(32).hex()})
# ✅ Se ha agregado verificación de existencia de clave antes de usarla
if secret_data is None:
    raise ValueError('No se pudo obtener la clave desde AWS Secrets Manager')
if not get_secret(SECRET_NAME_JWT):
    create_secret(SECRET_NAME_JWT, {"JWT_SECRET": os.urandom(64).hex()})
