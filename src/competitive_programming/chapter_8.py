def get_hamming_distance(left: str, right: str) -> int:
    return (int(left, 2) ^ int(right, 2)).bit_count()


def get_minimum_hamming_distance(strings: list[str]) -> int:
    if not strings:
        raise ValueError('strings are empty')
    return min(get_hamming_distance(strings[i], strings[j])
               for i in range(len(strings))
               for j in range(i + 1, len(strings)))


def count_subgrids(grid) -> int:
    pass
