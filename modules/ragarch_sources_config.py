
def consultar_con_jerarquizacion(pregunta):
    respuesta_ragarch = consultar_ragarch(pregunta)
    if respuesta_ragarch:
        return respuesta_ragarch
    else:
        respuesta_chatgpt = consultar_chatgpt_conocimiento_preexistente(pregunta)
        return respuesta_chatgpt

import json
import requests
import redis
import os

# Configuración de Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

# URL de la API de RAGArch para obtener fuentes
RAGARCH_API_URL = "https://ragarch-instance.com/api/get_sources"

# Fuentes secundarias para fallback
FALLBACK_SOURCES = [
    "https://api.fallback-source1.com/get_sources",
    "https://api.fallback-source2.com/get_sources"
]

# Función para obtener las fuentes jerarquizadas
def get_sources(region=None):
    cache_key = f"sources:{region}"
    cached_result = redis_client.get(cache_key)
    
    # Verificar si el resultado está en caché
    if cached_result:
        return json.loads(cached_result)
    
    # Intentar obtener las fuentes de la API principal
    params = {"region": region} if region else {}
    try:
        response = requests.get(RAGARCH_API_URL, params=params)
        if response.status_code == 200:
            result = response.json()
            # Expiración de caché según frecuencia de actualización
            cache_expiration = 1800 if region == "Europa" else 3600  # 30 min para Europa, 1 hora para otros
            redis_client.setex(cache_key, cache_expiration, json.dumps(result))
            return result
    except Exception as e:
        logging.info(f"Error al obtener fuentes de la API principal: {e}")
    
    # Estrategia de Fallback: Intentar con fuentes secundarias
    for fallback_url in FALLBACK_SOURCES:
        try:
            response = requests.get(fallback_url, params=params)
            if response.status_code == 200:
                result = response.json()
                redis_client.setex(cache_key, 3600, json.dumps(result))  # 1 hora para fallback
                return result
        except Exception as e:
            logging.info(f"Error al obtener fuentes de la fuente secundaria {fallback_url}: {e}")

    # Si todas las fuentes fallan, retornar un error
    logging.info("Error: No se pudo obtener fuentes de ninguna API disponible.")
    return {"error": "No se pudieron obtener fuentes de información."}
