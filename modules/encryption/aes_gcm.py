"""
Cifrado y Descifrado con AES-GCM, ahora usando claves seguras desde variables de entorno.
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Obtener clave segura desde variables de entorno
AES_KEY = os.getenv("AES_SECRET_KEY", os.urandom(32))  # 256-bit key

def encrypt_aes_gcm(data):
    """
    Cifra datos con AES-GCM.
    """
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(AES_KEY), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return nonce + ciphertext + encryptor.tag

def decrypt_aes_gcm(encrypted_data):
    """
    Descifra datos cifrados con AES-GCM.
    """
    nonce, ciphertext, tag = encrypted_data[:12], encrypted_data[12:-16], encrypted_data[-16:]
    cipher = Cipher(algorithms.AES(AES_KEY), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()
