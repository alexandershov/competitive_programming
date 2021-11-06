def weird_algorithm(n: int) -> list[int]:
    assert n > 0
    result = [n]

    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        result.append(n)

    return result
