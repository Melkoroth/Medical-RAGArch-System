import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configuración de DynamoDB
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "MedicalDocuments")

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

def retrieve_documents(document_type: str, limit: int = 3):
    """Recupera documentos almacenados en DynamoDB, como analíticas médicas."""
    try:
        response = table.scan(
            FilterExpression="document_type = :doc_type",
            ExpressionAttributeValues={":doc_type": document_type},
            Limit=limit
        )
        documents = response.get("Items", [])
        return documents
    except (NoCredentialsError, PartialCredentialsError) as e:
        return {"error": "Credenciales de AWS no configuradas correctamente", "details": str(e)}
    except Exception as e:
        return {"error": "Error al recuperar documentos desde DynamoDB", "details": str(e)}
