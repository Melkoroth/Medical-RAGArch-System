import boto3

apigateway_client = boto3.client("apigateway")

response = apigateway_client.update_stage(
    restApiId="your-api-id",
    stageName="prod",
    patchOperations=[
        {
            "op": "replace",
            "path": "/cacheClusterEnabled",
            "value": "true"
        },
        {
            "op": "replace",
            "path": "/cacheClusterSize",
            "value": "1.0"
        }
    ]
)

print("API Gateway caching enabled:", response)
