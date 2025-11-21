# Step 3 -- By Mohammed

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes



def generate_rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_key_with_rsa(aes_key: bytes, public_key):
    encrypted_key = public_key.encrypt(
                                    aes_key,
                                    padding.OAEP(
                                                  mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(),
                                                  label=None
                                                )
                                    )
    return encrypted_key

def decrypt_key_with_rsa(encrypted_key: bytes, private_key):
    decrypted_key = private_key.decrypt(
                                        encrypted_key,
                                        padding.OAEP(
                                                      mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                      algorithm=hashes.SHA256(),
                                                      label=None
                                                    )
                                      )
    return decrypted_key
