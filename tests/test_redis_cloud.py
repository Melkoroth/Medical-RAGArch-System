import pytest
from modules.redis_cloud import redis_client

def test_redis_connection():
    try:
        redis_client.ping()
        assert True, "Conexión exitosa a Redis."
    except Exception as e:
        pytest.fail(f"Error de conexión a Redis: {e}")
