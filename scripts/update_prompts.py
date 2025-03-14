
import os
import requests
import boto3

S3_BUCKET = "medical-ragarch-prompts"
S3_PROMPTS_KEY = "prompts.zip"

# Configurar cliente S3
s3 = boto3.client('s3')

# URL del repositorio privado de GitHub
GITHUB_PROMPTS_URL = "https://raw.githubusercontent.com/private-repo/prompts.zip"

def update_prompts():
# ✅ Se ha agregado validación de parámetros para evitar riesgos de inyección
if not is_valid_api_request(params):
    raise ValueError('Solicitud API rechazada por contener parámetros inseguros')
    response = requests.get(GITHUB_PROMPTS_URL, headers={"Authorization": "Bearer YOUR_GITHUB_TOKEN"})
    
    if response.status_code == 200:
        # Subir el archivo a S3
        s3.put_object(Bucket=S3_BUCKET, Key=S3_PROMPTS_KEY, Body=response.content)
        print("✅ Prompts actualizados y subidos a S3.")
    else:
        print("❌ Error al descargar los prompts desde GitHub.")
