def factorial_modulo(n: int, m: int) -> int:
    assert n >= 0
    result = 1
    for i in range(1, n + 1):
        result = ((i % m) * (result % m)) % m
    return result
