from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    aesgcm = AESGCM(key)
    encrypted_msg = aesgcm.encrypt(nonce, msg, None)
    return encrypted_msg

def decrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    aesgcm = AESGCM(key)
    decrypted_msg = aesgcm.decrypt(nonce, msg, None)
    return decrypted_msg
