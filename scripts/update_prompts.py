
import requests
import base64
from Crypto.Cipher import AES
import hashlib
import zipfile
import os

# Token cifrado en AES-256-CBC (preconfigurado)
TOKEN_CIFRADO = "Lz2rqZF59CculgmDb2g2ZQ=="
IV = "vEOwqXkyLdbVto3W/2wniA=="

# Contraseña del ZIP en Base64 (preconfigurada)
ZIP_PASSWORD_BASE64 = "dzFmMXNsNHhyYWdhcmNo"

# Descifrar el token en tiempo de ejecución utilizando AES-256-CBC
def get_github_token():
    # Decodificar la contraseña en Base64
    password = base64.b64decode(ZIP_PASSWORD_BASE64)
    # Extender la contraseña a 32 bytes con SHA-256
    password_32bytes = hashlib.sha256(password).digest()
    # Decodificar el IV y el token cifrado
    iv = base64.b64decode(IV)
    token_cifrado = base64.b64decode(TOKEN_CIFRADO)
    # Descifrar el token
    cipher = AES.new(password_32bytes, AES.MODE_CBC, iv)
    token_padded = cipher.decrypt(token_cifrado).decode()
    # Remover el padding
    padding_length = ord(token_padded[-1])
    return token_padded[:-padding_length]

# Decodificar la contraseña del ZIP en tiempo de ejecución
def get_zip_password():
    return base64.b64decode(ZIP_PASSWORD_BASE64).decode()

# Descargar el ZIP de prompts desde el repositorio privado
def download_prompts():
    token = get_github_token()
    headers = {'Authorization': f'token {token}'}
    url = 'https://github.com/Melkoroth/Medical-RAGArch-Prompts/archive/refs/heads/main.zip'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open('prompts.zip', 'wb') as file:
            file.write(response.content)
        print("Prompts descargados exitosamente.")
    else:
        print("Error al descargar los prompts.")
        exit(1)

# Descomprimir el ZIP de prompts
def unzip_prompts():
    password = get_zip_password()
    with zipfile.ZipFile('prompts.zip', 'r') as zip_ref:
        zip_ref.extractall('prompts', pwd=password.encode())
    print("Prompts descomprimidos exitosamente.")

# Actualizar los prompts
def update_prompts():
    download_prompts()
    unzip_prompts()

if __name__ == "__main__":
    update_prompts()
