def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return get_smallest_factor(number, start=2) == number


def get_smallest_factor(number: int, start) -> int:
    factor = start
    while factor ** 2 <= number:
        if number % factor == 0:
            return factor
        factor += 1
    return number


def factorize(number: int) -> list[int]:
    assert number > 1

    factors = []
    while number != 1:
        smallest_factor = get_smallest_factor(number, start=2)
        factors.append(smallest_factor)
        number //= smallest_factor
    return factors
