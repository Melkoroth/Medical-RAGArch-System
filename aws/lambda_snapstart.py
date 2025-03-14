# Enable SnapStart in AWS Lambda
import boto3

lambda_client = boto3.client("lambda")

response = lambda_client.update_function_configuration(
    FunctionName="MedicalRAGLambda",
    SnapStart={"ApplyOn": "PublishedVersions"}
)

print("SnapStart Enabled:", response)

print("SnapStart Optimization Applied")
