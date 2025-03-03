
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from mangum import Mangum
from api.main import router as api_router
from pydantic import BaseModel
from redis import Redis
from cryptography.fernet import Fernet
import jwt
import logging
from typing import Optional
import os

# Configuración de FastAPI
app = FastAPI()

# Incluir el router de la API principal
app.include_router(api_router)

# Configuración de JWT
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret_key")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configuración de Redis Cloud Essentials
redis_cloud = Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    password=os.getenv('REDIS_PASSWORD', '')
)

# Cifrado AES-256 con Fernet
SECRET_KEY_PATH = 'security/secret.key'
if os.path.exists(SECRET_KEY_PATH):
    with open(SECRET_KEY_PATH, 'rb') as key_file:
        fernet_key = key_file.read()
else:
    fernet_key = Fernet.generate_key()
    os.makedirs('security', exist_ok=True)
    with open(SECRET_KEY_PATH, 'wb') as key_file:
        key_file.write(fernet_key)

cipher = Fernet(fernet_key)

# Configuración de logs avanzado
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Modelo para almacenamiento de datos
class DataModel(BaseModel):
    data: str

# Función para generar JWT
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# Función para verificar JWT
def verify_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Endpoint para generar token JWT
@app.post("/token")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "password":
        access_token = create_jwt_token({"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Endpoint para almacenar datos cifrados
@app.post("/store/")
def store_data(data_model: DataModel, token: str = Depends(oauth2_scheme)):
    verify_jwt_token(token)
    encrypted_data = cipher.encrypt(data_model.data.encode())
    redis_cloud.set('encrypted_data', encrypted_data)
    logger.info("Datos cifrados almacenados en Redis Cloud.")
    return {"message": "Data stored securely."}

# Endpoint para recuperar datos cifrados
@app.get("/retrieve/")
def retrieve_data(token: str = Depends(oauth2_scheme)):
    verify_jwt_token(token)
    encrypted_data = redis_cloud.get('encrypted_data')
    if encrypted_data:
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        logger.info("Datos cifrados recuperados de Redis Cloud.")
        return {"data": decrypted_data}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")

# Endpoint para consultar datos cacheados
@app.get("/cached-query/{query_key}")
def get_cached_query(query_key: str):
    cached_data = redis_cloud.get(query_key)
    if cached_data:
        return {"cached_data": cached_data.decode()}
    else:
        return {"message": "No cached data found for this query."}

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Medical-RAGArch-System is running with AES-256, JWT, and Redis Cloud!"}

# Integración con AWS Lambda utilizando Mangum
handler = Mangum(app)
