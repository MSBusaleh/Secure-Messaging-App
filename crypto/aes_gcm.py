#Step 2 -- By Mohammed
from cryptography import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def generate_key():
    return AESGCM.generate_key(bit_length=256)

def encrypt_aes_gcm(plaintext: bytes, key: bytes):
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext, None)
    return ciphertext, iv

def decrypt_aes_gcm(iv: bytes, ciphertext: bytes, tag: bytes, key: bytes):
    aesgcm = AESGCM(key)
    decryptedText = aesgcm.decrypt(iv, ciphertext + tag, None)
    return decryptedText