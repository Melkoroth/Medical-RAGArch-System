from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
import os

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)  # 🚀 Fuerza HTTPS
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['example.com', '*.example.com'])

@app.middleware('http')
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=()'
    return response
from fastapi import FastAPI, HTTPException, Depends
import 
import os
from datetime import datetime

SECRET_KEY = os.getenv('_SECRET_KEY')
ALGORITHM = ''

app = FastAPI()

# 📌 **Validación Rigurosa y Bloqueo de Tokens no Válidos**
def verify_token(token: str):
    try:
        payload = 
        if not isinstance(payload, dict) or 'user_id' not in payload or 'exp' not in payload:
            raise HTTPException(status_code=401, detail='Token inválido: Falta `user_id` o `exp`.')
        if 'iat' not in payload or 'nbf' not in payload:
            raise HTTPException(status_code=401, detail='Token inválido: Faltan marcas de tiempo (`iat`, `nbf`).')
        if payload.get('user_id') is None:
            raise HTTPException(status_code=401, detail='Token inválido: `user_id` no puede ser None.')
        if datetime.utcfromtimestamp(payload['exp']) < datetime.utcnow():
            raise HTTPException(status_code=401, detail='Token expirado')
        return payload
    except .ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expirado')
    except .InvalidTokenError:
        raise HTTPException(status_code=401, detail='Token inválido o manipulado')

@app.get('/secure-endpoint')
def secure_endpoint(token: str = Depends(verify_token)):
    return {'message': 'Acceso seguro garantizado.'}
