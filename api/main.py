
from fastapi import FastAPI
import boto3
import os

app = FastAPI()

# Configurar Lambda SnapStart (si está disponible)
if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    import snapstart

@app.get("/")
async def root():
    return {"message": "Medical-RAGArch-System is running on AWS Lambda"}

# Lambda Power Tuning (Se recomienda ajustar memoria en AWS Console)
lambda_client = boto3.client("lambda")

@app.on_event("startup")
async def startup_event():
    lambda_client.update_function_configuration(
        FunctionName=os.getenv("AWS_LAMBDA_FUNCTION_NAME"),
        MemorySize=512  # Ajustable según pruebas con Lambda Power Tuning
    )

import boto3
import os

dynamodb = boto3.resource("dynamodb")
table_name = os.getenv("DYNAMODB_TABLE", "MedicalData")

# Configuración de Auto Scaling
app_config = boto3.client("application-autoscaling")

app_config.register_scalable_target(
    ServiceNamespace="dynamodb",
    ResourceId=f"table/{table_name}",
    ScalableDimension="dynamodb:table:ReadCapacityUnits",
    MinCapacity=5,
    MaxCapacity=100
)

app_config.put_scaling_policy(
    PolicyName="DynamoDBAutoScaling",
    ServiceNamespace="dynamodb",
    ResourceId=f"table/{table_name}",
    ScalableDimension="dynamodb:table:ReadCapacityUnits",
    PolicyType="TargetTrackingScaling",
    TargetTrackingScalingPolicyConfiguration={
        "TargetValue": 70.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "DynamoDBReadCapacityUtilization"
        }
    }
)

# Escrituras en lote
def batch_write_items(items):
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
