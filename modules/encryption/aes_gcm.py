
# Cifrado y Descifrado con AES-GCM

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Función para cifrar datos con AES-GCM
def encrypt_aes_gcm(data, key):
    # Generar un nonce (Número único utilizado una sola vez)
    nonce = os.urandom(12)

    # Crear un cifrador AES-GCM
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    # Cifrar los datos
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return nonce, ciphertext, encryptor.tag

# Función para descifrar datos con AES-GCM
def decrypt_aes_gcm(nonce, ciphertext, tag, key):
    # Crear un cifrador AES-GCM para descifrar
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce, tag),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()

    # Descifrar los datos
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_data
