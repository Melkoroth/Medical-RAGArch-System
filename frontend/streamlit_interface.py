
import os
import requests
import boto3

S3_BUCKET = "medical-ragarch-prompts"
S3_PROMPTS_KEY = "prompts.zip"

# Configurar cliente S3
s3 = boto3.client('s3')

def fetch_prompts_from_s3():
    prompts_url = s3.generate_presigned_url("get_object", Params={"Bucket": S3_BUCKET, "Key": S3_PROMPTS_KEY})
    response = requests.get(prompts_url)
    
    if response.status_code == 200:
        with open('prompts.zip', 'wb') as file:
            file.write(response.content)
        print("✅ Prompts descargados desde S3.")
    else:
        print("❌ Error al descargar los prompts desde S3.")

# Llamar a la función para obtener los prompts desde S3
fetch_prompts_from_s3()
