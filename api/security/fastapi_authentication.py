
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
import hmac
import hashlib
import os

app = FastAPI()

# Configuración de seguridad
SECRET_KEY = os.environ.get("SECRET_KEY", "clave_super_secreta")
API_KEY = os.environ.get("API_KEY", "api-key-generada-dinamicamente")
ALGORITHM = ""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para verificar el token 
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        return payload
    except .ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except .InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Función para verificar la firma HMAC en cada solicitud
def verify_hmac(signature: str = Header(None), payload: str = Header(None)):
    if not signature or not payload:
        raise HTTPException(status_code=401, detail="Falta la firma de seguridad")

    expected_signature = hmac.new(
        API_KEY.encode(), payload.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(status_code=401, detail="Firma HMAC no válida")

# Endpoint protegido con autenticación  y firma HMAC
@app.get("/tools/summarizer")
async def summarize(text: str, user: dict = Depends(verify_token), hmac_check=Depends(verify_hmac)):
    """Endpoint protegido para resumir texto."""
    return {"summary": text[:100] + "..."}
