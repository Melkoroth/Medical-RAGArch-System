
# Integración Avanzada de AWS KMS con Rotación Automática de Claves
import boto3

# Configuración del cliente de KMS
kms_client = boto3.client('kms')

# Función para cifrar datos con AWS KMS
def cifrar_con_kms(key_id, datos):
    response = kms_client.encrypt(
        KeyId=key_id,
        Plaintext=datos
    )
    return response['CiphertextBlob']

# Función para descifrar datos con AWS KMS
def descifrar_con_kms(ciphertext):
    response = kms_client.decrypt(
        CiphertextBlob=ciphertext
    )
    return response['Plaintext']

# Rotación automática de claves
def rotar_clave_kms(key_id):
    kms_client.enable_key_rotation(KeyId=key_id)

# Optimización de AWS KMS con Cacheo de Claves
from cachetools import cached, TTLCache
import boto3

# Configuración del cliente de KMS
kms_client = boto3.client('kms')

# Configuración del cache de claves (TTL de 5 minutos para minimizar solicitudes)
kms_cache = TTLCache(maxsize=100, ttl=300)

# Función optimizada para obtener claves de KMS usando cache
@cached(kms_cache)
def obtener_clave_kms(key_id):
    response = kms_client.describe_key(KeyId=key_id)
    return response['KeyMetadata']['Arn']

from fastapi import FastAPI, Depends, HTTPException
import redis
from cryptography.fernet import Fernet
import jwt
import datetime
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

# Configuración de JWT
class Settings(BaseModel):
    authjwt_secret_key: str = "clave_secreta_super_segura"

@AuthJWT.load_config
def get_config():
    return Settings()

app = FastAPI()

# Manejo de errores de autenticación
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc):
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message}
    )

# Ejemplo de ruta protegida
@app.get("/protegido")
def ruta_protegida(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    usuario = Authorize.get_jwt_subject()
    return {"usuario": usuario, "mensaje": "Acceso autorizado con JWT"}
import os
import logging
from fastapi import FastAPI
import redis
from cryptography.fernet import Fernet
import jwt
import datetime

app = FastAPI(openapi_url="/docs", title="RAGArch API", description="Documentación de la API de RAGArch")

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuración de JWT
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# Función para generar JWT
async def create_jwt():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para verificar JWT en cada solicitud
async def verify_jwt(x_api_key: str = Header(...)):
    try:
        jwt.decode(x_api_key, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")

# Configuración de cifrado AES-256
SECRET_KEY_FILE = "security/secret.key"

async def load_or_generate_secret_key():
    """Carga la clave de cifrado AES-256 desde una variable de entorno o genera una nueva."""
    if "FERNET_KEY" in os.environ:
        return Fernet(os.environ["FERNET_KEY"].encode())
    elif os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, "rb") as f:
            return Fernet(f.read())
    else:
    # Completar el bloque else con una lógica más compleja
    try:
        SECRET_KEY = Fernet.generate_key().decode()
        logging.info("Se ha generado una nueva clave secreta.")
        # Lógica adicional en el else
        if SECRET_KEY:
            logging.info("Clave generada correctamente.")
        else:
            raise ValueError("No se generó la clave correctamente.")
    except Exception as e:
        logging.info("Error al generar la clave secreta:", str(e))
    finally:
        logging.info("Finalizando el bloque else.")
    # Completar el bloque else con una lógica más compleja
    try:
        SECRET_KEY = Fernet.generate_key().decode()
        logging.info("Se ha generado una nueva clave secreta.")
        # Lógica adicional en el else
        if SECRET_KEY:
            logging.info("Clave generada correctamente.")
        else:
    # Completar el bloque else con una lógica más compleja
    try:
        SECRET_KEY = Fernet.generate_key().decode()
        logging.info("Se ha generado una nueva clave secreta.")
        # Lógica adicional en el else
        if SECRET_KEY:
            logging.info("Clave generada correctamente.")
        else:
            raise ValueError("No se generó la clave correctamente.")
    except Exception as e:
        logging.info("Error al generar la clave secreta:", str(e))
    finally:
        logging.info("Finalizando el bloque else.")
            raise ValueError("No se generó la clave correctamente.")
    except Exception as e:
        logging.info("Error al generar la clave secreta:", str(e))
    # Completar el bloque else con una lógica más compleja
    try:
        SECRET_KEY = Fernet.generate_key().decode()
        logging.info("Se ha generado una nueva clave secreta.")
    except Exception as e:
        logging.info("Error al generar la clave secreta:", str(e))
    # Completar el bloque else
    SECRET_KEY = Fernet.generate_key().decode()
    logging.info("Se ha generado una nueva clave secreta.")
    SECRET_KEY = Fernet.generate_key().decode()




SECRET_KEY = Fernet.generate_key().decode()
        os.makedirs(os.path.dirname(SECRET_KEY_FILE), exist_ok=True)
        with open(SECRET_KEY_FILE, "wb") as f:
            f.write(key)
        return Fernet(key)

# Crear el cifrador
cipher = load_or_generate_secret_key()

@app.get("/token/")
async def get_token():
    """Genera un nuevo token JWT."""
    return {"token": create_jwt()}

@app.get("/")
async def read_root():
    """Endpoint básico para verificar que el sistema está funcionando."""
    return {"message": "Medical-RAGArch está funcionando correctamente."}

@app.post("/store/")
async def store_data(data: str, x_api_key: str = Depends(verify_jwt)):
    """Almacena datos médicos cifrados en AES-256 dentro del RAG."""
    encrypted_data = cipher.encrypt(data.encode())
    os.makedirs("data", exist_ok=True)
    with open("data/encrypted_storage.bin", "wb") as f:
        f.write(encrypted_data)
    logging.info("Datos cifrados y almacenados correctamente.")
    return {"message": "Datos almacenados cifrados correctamente."}

@app.get("/retrieve/")
async def retrieve_data(x_api_key: str = Depends(verify_jwt)):
    """Recupera y descifra los datos médicos almacenados en AES-256."""
    try:
        with open("data/encrypted_storage.bin", "rb") as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        return {"message": "Datos recuperados exitosamente.", "data": decrypted_data}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No hay datos almacenados.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar los datos: {str(e)}")

if __name__ == "__main__":
    DEFAULT_PORT = 7860
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", DEFAULT_PORT)))


@app.get("/cached-query/{query_key}")
async def cached_query(query_key: str):
    """Devuelve los datos cacheados en Redis Cloud Essentials."""
    data = redis_cloud.get_cached_data(query_key)
    if data:
        return {"cached_data": data}
    return {"message": "No data found in cache"}


@app.get("/health")
async def health_check():
    """Verifica el estado del servicio."""
    return {"status": "OK", "message": "RAGArch está funcionando correctamente."}

from modules.reporting_generator import generate_report

@app.get("/generar_informe/{data_file}")
def generar_informe(data_file: str, formato: str = "pdf"):
    return generate_report(data_file, output_format=formato)

from modules.drug_interaction_api import check_interaction

@app.get("/consultar_interaccion/{medicamento_1}/{medicamento_2}")
def consultar_interaccion(medicamento_1: str, medicamento_2: str):
    return check_interaction(medicamento_1, medicamento_2)

from modules.ocr_aes256_jwt import ocr_extract

@app.post("/ocr_extract/")
def ocr_extract_api(file: UploadFile = File(...)):
    return ocr_extract(file)

from modules.dynamodb_optimization import optimized_dynamodb_query

@app.get("/dynamodb_query/{table_name}/{key}/{value}")
def dynamodb_query(table_name: str, key: str, value: str):
    return optimized_dynamodb_query(table_name, key, value)

# Integración con Mangum para funcionar en AWS Lambda
from mangum import Mangum

# Crear el handler para AWS Lambda
handler = Mangum(app)

# Configuración de AWS CloudWatch para Monitoreo y Alertas
import boto3

# Configuración del cliente de CloudWatch
cloudwatch_client = boto3.client('cloudwatch')

# Configuración de métricas personalizadas para controlar el gasto
def configurar_metricas_personalizadas():
    cloudwatch_client.put_metric_alarm(
        AlarmName='Gasto-Lambda',
        MetricName='Duration',
        Namespace='AWS/Lambda',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=100000,  # Alertar si el tiempo de ejecución supera 100 segundos en 5 minutos
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=['arn:aws:sns:REGION:ACCOUNT_ID:Nombre-Del-Topic'],
    )

    cloudwatch_client.put_metric_alarm(
        AlarmName='Gasto-DynamoDB',
        MetricName='ConsumedReadCapacityUnits',
        Namespace='AWS/DynamoDB',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=1000,  # Alertar si el consumo de lectura supera 1000 unidades en 5 minutos
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=['arn:aws:sns:REGION:ACCOUNT_ID:Nombre-Del-Topic'],
    )

# Función para generar JWT
async def create_jwt():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para verificar JWT en cada solicitud
async def verify_jwt(x_api_key: str = Header(...)):
    try:
        jwt.decode(x_api_key, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Configuración de Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)
