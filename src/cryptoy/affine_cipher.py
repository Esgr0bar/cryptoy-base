from math import (
    gcd,
)

from cryptoy.utils import (
    str_to_unicodes,
    unicodes_to_str,
)

# TP: Chiffrement affine


def compute_permutation(a: int, b: int, n: int) -> list[int]:
    # A implémenter, en sortie on doit avoir une liste result tel que result[i] == (a * i + b) % n
    pass


def compute_inverse_permutation(a: int, b: int, n: int) -> list[int]:
    # A implémenter, pour cela on appelle perm = compute_permutation(a, b, n) et on calcule la permutation inverse
    # result qui est telle que: perm[i] == j implique result[j] == i
    pass


def encrypt(msg: str, a: int, b: int) -> str:
    # A implémenter, en utilisant compute_permutation, str_to_unicodes et unicodes_to_str
    pass


def encrypt_optimized(msg: str, a: int, b: int) -> str:
    # A implémenter, sans utiliser compute_permutation
    pass


def decrypt(msg: str, a: int, b: int) -> str:
    # A implémenter, en utilisant compute_inverse_permutation, str_to_unicodes et unicodes_to_str
    pass


def decrypt_optimized(msg: str, a_inverse: int, b: int) -> str:
    # A implémenter, sans utiliser compute_inverse_permutation
    # On suppose que a_inverse a été précalculé en utilisant compute_affine_key_inverse, et passé
    # a la fonction
    pass


def compute_affine_keys(n: int) -> list[int]:
    # A implémenter, doit calculer l'ensemble des nombre a entre 1 et n tel que gcd(a, n) == 1
    # c'est à dire les nombres premiers avec n
    pass


def compute_affine_key_inverse(a: int, affine_keys: list, n: int) -> int:
    # Trouver a_1 dans affine_keys tel que a * a_1 % N == 1 et le renvoyer
    # Placer le code ici (une boucle)

    # Si a_1 n'existe pas, alors a n'a pas d'inverse, on lance une erreur:
    raise RuntimeError(f"{a} has no inverse")


def attack() -> tuple[str, tuple[int, int]]:
    s = "࠾ੵΚઐ௯ஹઐૡΚૡೢఊஞ௯\u0c5bૡీੵΚ៚Κஞїᣍફ௯ஞૡΚր\u05ecՊՊΚஞૡΚՊեԯՊ؇ԯրՊրր"
    # trouver msg, a et b tel que affine_cipher_encrypt(msg, a, b) == s
    # avec comme info: "bombe" in msg et b == 58

    # Placer le code ici

    raise RuntimeError("Failed to attack")


def attack_optimized() -> tuple[str, tuple[int, int]]:
    s = (
        "જഏ൮ൈ\u0c51ܲ೩\u0c51൛൛అ౷\u0c51ܲഢൈᘝఫᘝా\u0c51\u0cfc൮ܲఅܲᘝ൮ᘝܲాᘝఫಊಝ"
        "\u0c64\u0c64ൈᘝࠖܲೖఅܲఘഏ೩ఘ\u0c51ܲ\u0c51൛൮ܲఅ\u0cfc\u0cfcඁೖᘝ\u0c51"
    )
    # trouver msg, a et b tel que affine_cipher_encrypt(msg, a, b) == s
    # avec comme info: "bombe" in msg

    # Placer le code ici

    raise RuntimeError("Failed to attack")
