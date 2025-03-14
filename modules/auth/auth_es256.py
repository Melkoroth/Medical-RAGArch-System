"""
Autenticación con FastAPI OAuth2PasswordBearer y ES256 (ECDSA), ahora usando claves seguras.
"""

import os
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generar clave privada ECDSA si no existe en variables de entorno
PRIVATE_KEY = os.getenv("ECDSA_PRIVATE_KEY")
if not PRIVATE_KEY:
    private_key = ec.generate_private_key(ec.SECP256R1())
    PRIVATE_KEY = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

# Cargar clave privada
private_key = serialization.load_pem_private_key(PRIVATE_KEY.encode(), password=None)

# Generar clave pública
public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()

def create_jwt(data, expires_in=1800):
    """
    Genera un JWT con ES256 (ECDSA) con expiración de 30 minutos.
    """
