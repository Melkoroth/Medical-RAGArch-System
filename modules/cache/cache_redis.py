
# Cache Optimizada con Redis

import redis

# Conexión a Redis Cloud Essentials
cache = redis.Redis(host='localhost', port=6379, db=0)

# Almacenar y Recuperar Datos en Cache
cache.set('clave', 'valor cacheado')
valor = cache.get('clave').decode('utf-8')
print(f"Valor recuperado de Redis: {valor}")
