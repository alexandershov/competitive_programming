def factorial_modulo(n: int, m: int) -> int:
    assert n >= 0
    if n == 0:
        return 1

    return ((n % m) * factorial_modulo(n - 1, m)) % m
