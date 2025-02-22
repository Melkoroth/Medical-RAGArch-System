
import redis

# Función para conectar a Redis Cloud Essentials usando SSL/TLS
def get_redis_connection():
    return redis.Redis(
        host='your_redis_host',
        port=6379,
        password='your_redis_password',
        ssl=True,  # Usar SSL/TLS para encriptar datos en tránsito
        ssl_cert_reqs='required'
    )

# Función para obtener datos en caché
def get_cached_data(key):
    redis_conn = get_redis_connection()
    return redis_conn.get(key)

# Función para almacenar datos en caché con expiración configurable
def cache_data(key, value, expiration=3600):
    redis_conn = get_redis_connection()
    redis_conn.set(key, value, ex=expiration)
