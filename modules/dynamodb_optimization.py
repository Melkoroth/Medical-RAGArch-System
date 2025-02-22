
from cryptography.fernet import Fernet
import boto3
from boto3.dynamodb.conditions import Key
import hashlib

# Almacenar clave de cifrado en AWS KMS
kms_client = boto3.client('kms')
encryption_key_id = 'alias/MyRAGArchKey'
clave_cifrado = kms_client.generate_data_key(KeyId=encryption_key_id, KeySpec='AES_256')['Plaintext']
cifrador = Fernet(clave_cifrado)

# Función para calcular hash de datos
def calcular_hash(dato):
    return hashlib.sha256(dato.encode()).hexdigest()

# Cifrar y almacenar en DynamoDB
def almacenar_dato_cifrado(tabla, clave, dato):
    dato_cifrado = cifrador.encrypt(dato.encode())
    hash_dato = calcular_hash(dato)
    tabla.put_item(Item={'clave': clave, 'dato': dato_cifrado.decode(), 'integridad': hash_dato})

# Descifrar y verificar integridad al recuperar datos
def recuperar_dato_descifrado(tabla, clave):
    respuesta = tabla.query(KeyConditionExpression=Key('clave').eq(clave))
    dato_cifrado = respuesta['Items'][0]['dato']
    dato_descifrado = cifrador.decrypt(dato_cifrado.encode()).decode()
    hash_guardado = respuesta['Items'][0]['integridad']
    hash_calculado = calcular_hash(dato_descifrado)

    if hash_guardado != hash_calculado:
        raise Exception("Error de integridad: El hash no coincide.")

    return dato_descifrado
