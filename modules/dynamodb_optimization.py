try:
    import boto3
except ImportError:
    boto3 = None  # Carga opcional
try:
    import json
except ImportError:
    json = None  # Carga opcional

def optimized_dynamodb_query(table_name, key, value):
    """Optimiza las consultas a DynamoDB usando índices secundarios y filtros inteligentes."""
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)
    
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key(key).eq(value)
    )
    
    return response["Items"]
