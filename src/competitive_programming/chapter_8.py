def get_hamming_distance(left: str, right: str) -> int:
    return (int(left, 2) ^ int(right, 2)).bit_count()


def get_minimum_hamming_distance(strings: list[str]) -> int:
    pass
