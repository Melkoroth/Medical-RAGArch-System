import boto3

dynamodb_client = boto3.client("dynamodb")

table_name = "MedicalData"

response = dynamodb_client.update_table(
    TableName=table_name,
    BillingMode="PAY_PER_REQUEST",
    ProvisionedThroughput={
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
)

print("Adaptive Capacity enabled:", response)
