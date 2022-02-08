def get_hamming_distance(left: str, right: str) -> int:
    return (int(left, 2) ^ int(right, 2)).bit_count()


def get_minimum_hamming_distance(strings: list[str]) -> int:
    if not strings:
        raise ValueError('strings are empty')
    return min(get_hamming_distance(strings[i], strings[j])
               for i in range(len(strings))
               for j in range(i + 1, len(strings)))


def count_subgrids(grid) -> int:
    count = 0
    bit_masks = [
        int(''.join(map(str, row)), 2)
        for row in grid
    ]
    for top in range(len(grid)):
        for bottom in range(top + 1, len(grid)):
            common_count = (bit_masks[top] & bit_masks[bottom]).bit_count()
            count += (common_count * (common_count - 1)) // 2
    return count


def find_sum(seq, sum_):
    prefixes = [0]
    prefix_sum = 0

    for item in seq:
        prefix_sum += item
        prefixes.append(prefix_sum)
    suffixes = {0}
    suffix_sum = 0

    for item in reversed(seq):
        suffix_sum += item
        suffixes.add(suffix_sum)
    total_sum = sum(seq)

    for i, prefix_sum in enumerate(prefixes):
        expected_suffix = total_sum - prefix_sum - sum_
        if expected_suffix in suffixes:
            cur_sum = 0
            result = []
            j = i
            while cur_sum != sum_:
                cur_sum += seq[j]
                result.append(seq[j])
                j += 1
            return result
    return None

