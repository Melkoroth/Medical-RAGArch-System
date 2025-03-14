
from aws_cdk import core
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam
import aws_cdk.aws_dax as dax

class MedicalRAGArchStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Crear tabla DynamoDB con Auto Scaling habilitado
        self.table = dynamodb.Table(
            self, "MedicalDataTable",
            table_name="MedicalData",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST  # Auto Scaling
        )

        # Crear un bucket S3 para almacenamiento de documentos
        self.bucket = s3.Bucket(
            self, "MedicalDocumentsBucket",
            bucket_name="medical-ragarch-docs",
            removal_policy=core.RemovalPolicy.RETAIN
        )

        # Crear un rol IAM con permisos para DynamoDB y S3
        self.role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBAcceleratorFullAccess")
            ]
        )

        # Crear una instancia de DAX (DynamoDB Accelerator)
        self.dax_cluster = dax.CfnCluster(
            self, "MedicalDataDAXCluster",
            cluster_name="MedicalDataDAX",
            node_type="dax.t3.small",  # Tipo de instancia DAX
            replication_factor=2,  # Número de nodos en el clúster
            iam_role_arn=self.role.role_arn,
            subnet_group_name="default",  # Se debe configurar la VPC en AWS manualmente si es necesario
            security_group_ids=[]  # Agregar manualmente si es necesario
        )

        # Salidas del stack
        core.CfnOutput(self, "DynamoDBTableName", value=self.table.table_name)
        core.CfnOutput(self, "S3BucketName", value=self.bucket.bucket_name)
        core.CfnOutput(self, "IAMRoleArn", value=self.role.role_arn)
        core.CfnOutput(self, "DAXClusterName", value=self.dax_cluster.cluster_name)
