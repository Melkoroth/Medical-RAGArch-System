
#!/bin/bash
echo "Configuring AWS Lambda with EFS..."

# Instalar dependencias de AWS CLI si no están disponibles
if ! command -v aws &> /dev/null; then
    echo "AWS CLI not found, installing..."
    apt update && apt install -y awscli
fi

# Configurar variables de entorno
EFS_ID_PRIMARY="EFS_PRIMARY_ID"
EFS_ID_SECONDARY="EFS_SECONDARY_ID"
LAMBDA_ROLE="LAMBDA_EXECUTION_ROLE"

# Montar EFS en AWS Lambda
aws lambda update-function-configuration --function-name RAGArchLambda --file-system-configurations Arn=arn:aws:elasticfilesystem:us-east-1:ACCOUNT_ID:file-system/$EFS_ID_PRIMARY,LocalMountPath=/mnt/efs1 Arn=arn:aws:elasticfilesystem:us-east-1:ACCOUNT_ID:file-system/$EFS_ID_SECONDARY,LocalMountPath=/mnt/efs2

echo "EFS successfully mounted in AWS Lambda."
