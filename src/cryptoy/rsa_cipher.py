from math import gcd
from cryptoy.utils import (
    draw_random_prime,
    int_to_str,
    modular_inverse,
    pow_mod,
    str_to_int,
)

def keygen() -> dict:
    e = 65537

    p = draw_random_prime()
    q = draw_random_prime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    d = modular_inverse(e, phi_n)

    return {
        "public_key": (e, n),
        "private_key": d
    }

def encrypt(msg: str, public_key: tuple) -> int:
    e, n = public_key

    m = str_to_int(msg)

    if m >= n:
        raise ValueError("Le message est trop long pour être chiffré avec la clé publique donnée.")

    c = pow_mod(m, e, n)
    return c

def decrypt(msg: int, key: dict) -> str:
    public_key = key["public_key"]
    d = key["private_key"]
    n = public_key[1]

    m = pow_mod(msg, d, n)

    return int_to_str(m
