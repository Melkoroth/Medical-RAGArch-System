# AWS CDK for DAX
from aws_cdk import core, aws_dynamodb as dynamodb, aws_dax as dax

class DAXStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, "MedicalData",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        dax_cluster = dax.CfnCluster(
            self, "DAXCluster",
            cluster_name="MedicalRAG-DAX",
            node_type="dax.r5.large",
            replication_factor=2,
            iam_role_arn="arn:aws:iam::your-account-id:role/DAXRole"
        )

app = core.App()
DAXStack(app, "DAXStack")
app.synth()
