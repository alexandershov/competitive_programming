def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return get_smallest_prime_factor(number) == number


def get_smallest_prime_factor(number: int) -> int:
    factor = 2
    while factor ** 2 <= number:
        if number % factor == 0:
            return factor
        factor += 1
    return number


def factorize(number: int) -> list[int]:
    assert number > 1

    factors = []
    while number != 1:
        smallest_factor = get_smallest_prime_factor(number)
        factors.append(smallest_factor)
        number //= smallest_factor
    return factors


def build_eratosthenes_sieve(length: int) -> list[int]:
    sieve = length * [0]
    for i in range(length):
        if i in [0, 1]:
            sieve[i] = 1
            continue

        if not sieve[i]:
            j = 2
            while j * i < length:
                sieve[j * i] = 1
                j += 1
    return sieve


def gcd(x: int, y: int) -> int:
    pass
