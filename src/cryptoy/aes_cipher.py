from cryptography.hazmat.primitives.ciphers.aead import (
    AESGCM,
)


def encrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM
    pass


def decrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM
    pass
