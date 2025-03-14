
import os

# Obtener los IDs de EFS desde las variables de entorno
efs_ids = os.getenv("EFS_PATHS", "").split(",")

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": f"Conectado a {len(efs_ids)} sistemas de archivos EFS: {efs_ids}"
    }
