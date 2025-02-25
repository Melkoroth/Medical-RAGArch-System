
# Autenticación con FastAPI OAuth2PasswordBearer y ES256 (ECDSA)

from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from jose import JWTError, jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature

# Generar clave privada y pública ECDSA
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Serializar las claves
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Configuración del esquema OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modelo de usuario
class User(BaseModel):
    username: str
    email: Optional[str] = None

# Función para crear un token con ES256
def create_access_token(data: dict):
    token = jwt.encode(data, private_pem, algorithm="ES256")
    return token

# Función para verificar el token con ES256
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, public_pem, algorithms=["ES256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return User(username=username)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
