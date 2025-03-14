import httpx

# 📌 **Forzar verificación SSL en peticiones HTTP**
def secure_request(url, method="GET", data=None, headers=None):
    try:
        if method == "POST":
            response = httpx.post(url, json=data, headers=headers, verify=True, timeout=10)
        else:
            response = httpx.get(url, headers=headers, verify=True, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
