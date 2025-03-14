 
from aws_cdk import core
from aws_cdk import aws_efs as efs
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_iam as iam
from aws_cdk import aws_apigateway as apigw

class MedicalRAGArchStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Crear un rol IAM para Lambda con permisos de acceso a EFS y API Gateway
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonElasticFileSystemFullAccess")
            ]
        )

        # Crear 3 sistemas de archivos EFS
        efs_systems = []
        for i in range(3):
            efs_system = efs.FileSystem(
                self, f"MedicalEFS{i+1}",
                vpc=core.Fn.import_value("VPCID"),  # Requiere una VPC preexistente
                lifecycle_policy=efs.LifecyclePolicy.AFTER_7_DAYS,
                removal_policy=core.RemovalPolicy.DESTROY  # Cambiar a RETAIN en producción
            )
            efs_systems.append(efs_system)

        # Crear función Lambda vinculada a los 3 EFS
        lambda_function = lambda_.Function(
            self, "MedicalLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.lambda_handler",
            code=lambda_.Code.from_asset("lambda_code/"),  # Directorio con código de Lambda
            role=lambda_role,
            timeout=core.Duration.seconds(30),
            memory_size=512,
            environment={"EFS_PATHS": ",".join([efs_system.file_system_id for efs_system in efs_systems])}
        )

        # Agregar montajes EFS a la Lambda
        for i, efs_system in enumerate(efs_systems):
            lambda_function.add_environment(f"EFS_{i+1}_ID", efs_system.file_system_id)

        # Crear API Gateway para exponer Lambda
        api = apigw.LambdaRestApi(self, "MedicalAPI", handler=lambda_function)

        core.CfnOutput(self, "APIGatewayURL", value=api.url)
