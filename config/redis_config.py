# Redis Configuration
import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

def cache_response(key: str, response: str, expire_time: int = 3600):
    redis_client.setex(key, expire_time, response)

def get_cached_response(key: str):
    return redis_client.get(key)
