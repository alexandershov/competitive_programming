def is_prime(number: int) -> bool:
    if number < 2:
        return False
    factor = 2
    while factor ** 2 <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True


def factorize(number: int) -> list[int]:
    assert number > 1

    factors = []
    divisor = 2
    while not is_prime(number):
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    factors.append(1)
    factors.append(number)
    return factors
