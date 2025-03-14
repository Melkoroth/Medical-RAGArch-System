import httpx

# 📌 **Verificación Avanzada en Requests con Autenticación Fuerte**
def secure_request(url, method='GET', data=None, headers=None, auth_token=None):
    try:
        headers = headers or {}
        headers['User-Agent'] = 'Medical-RAGArch-Secure/1.0'
        if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
        if method == 'POST':
            if not isinstance(data, dict) or any(not isinstance(value, (str, int, float, list, dict, bool)) for value in data.values()):
                raise ValueError('Datos POST inválidos. Se requieren valores limpios y estructurados.')
            response = httpx.post(url, json=data, headers=headers, verify=True, timeout=10)
        elif method == 'GET':
            response = httpx.get(url, headers=headers, verify=True, timeout=10)
        else:
            raise ValueError('Método HTTP no permitido')
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        return {'error': f'Request failed: {e}'}
