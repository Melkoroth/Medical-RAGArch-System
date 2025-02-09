import os
from fastapi import FastAPI, Depends, HTTPException, Header
from cryptography.fernet import Fernet
import jwt
import datetime

app = FastAPI()

# Configuración de JWT
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

# Función para generar JWT
def create_jwt():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para verificar JWT en cada solicitud
def verify_jwt(x_api_key: str = Header(...)):
    try:
        jwt.decode(x_api_key, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")

# Configuración de cifrado AES-256
SECRET_KEY_FILE = "security/secret.key"

def generate_secret_key():
    """Genera una clave de cifrado AES-256 si no existe."""
    if not os.path.exists(SECRET_KEY_FILE):
        key = Fernet.generate_key()
        with open(SECRET_KEY_FILE, "wb") as f:
            f.write(key)

def load_secret_key():
    """Carga la clave de cifrado AES-256."""
    with open(SECRET_KEY_FILE, "rb") as f:
        return Fernet(f.read())

# Generar clave si no existe
generate_secret_key()
cipher = load_secret_key()

@app.get("/token/")
def get_token():
    return {"token": create_jwt()}

@app.get("/")
def read_root():
    return {"message": "Medical-RAGArch está funcionando correctamente."}

@app.post("/store/")
def store_data(data: str, x_api_key: str = Depends(verify_jwt)):
    """Almacena datos médicos cifrados en AES-256 dentro del RAG."""
    encrypted_data = cipher.encrypt(data.encode())
    with open("data/encrypted_storage.bin", "wb") as f:
        f.write(encrypted_data)
    return {"message": "Datos almacenados cifrados correctamente."}

@app.get("/retrieve/")
def retrieve_data(x_api_key: str = Depends(verify_jwt)):
    """Recupera y descifra los datos médicos almacenados en AES-256."""
    with open("data/encrypted_storage.bin", "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return {"message": "Datos recuperados exitosamente.", "data": decrypted_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 7860)))