import redis
import json
import os

# Configurar conexión con Redis Cloud Essentials (requiere endpoint y credenciales)
REDIS_HOST = os.getenv("REDIS_HOST", "your_redis_cloud_host")  # Debes reemplazar con el host de Redis Cloud
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))  # Puerto por defecto de Redis
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "your_redis_cloud_password")  # Contraseña de Redis Cloud

redis_client = redis.StrictRedis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
)

def get_cached_data(key):
    """Obtiene los datos almacenados en Redis Cloud Essentials."""
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None

def cache_data(key, data, expiration=3600):
    """Almacena datos en Redis Cloud Essentials con un tiempo de expiración definido."""
    redis_client.set(key, json.dumps(data), ex=expiration)
