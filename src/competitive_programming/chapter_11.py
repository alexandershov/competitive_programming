def is_prime(number: int) -> bool:
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
