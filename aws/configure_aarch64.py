import boto3

lambda_client = boto3.client("lambda")

response = lambda_client.update_function_configuration(
    FunctionName="MedicalRAGLambda",
    Architectures=["arm64"]
)

print("AWS Lambda now runs on aarch64:", response)
