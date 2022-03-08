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
    # TODO: can it be improved?
    # TODO: what is its complexity?
    assert number > 1

    factors = []
    divisor = 2
    number_is_prime = is_prime(number)
    while not number_is_prime:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
            number_is_prime = is_prime(number)
        else:
            divisor += 1
    factors.append(1)
    factors.append(number)
    return factors
