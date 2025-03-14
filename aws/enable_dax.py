import boto3

dynamodb_client = boto3.client("dynamodb")

response = dynamodb_client.create_cluster(
    ClusterName="MedicalRAG-DAX",
    NodeType="dax.r5.large",
    ReplicationFactor=2,
    IAMRoleArn="arn:aws:iam::your-account-id:role/DAXRole"
)

print("DAX enabled:", response)
