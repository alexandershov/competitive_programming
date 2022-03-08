def is_prime(number: int) -> bool:
    if number < 2:
        return False
    factor = 2
    while factor ** 2 <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True
