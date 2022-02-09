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
    total_sum = sum(seq)
    suffix_sums = get_suffix_sums(seq)

    prefix_sum = 0
    for i, item in enumerate(seq):
        expected_suffix = total_sum - prefix_sum - sum_
        if expected_suffix in suffix_sums:
            return take_items_to_form_sum(seq, i, sum_)
        prefix_sum += item
    return None


def take_items_to_form_sum(seq, i, sum_):
    cur_sum = 0
    result = []
    while cur_sum != sum_:
        cur_sum += seq[i]
        result.append(seq[i])
        i += 1
    return result


def get_suffix_sums(seq):
    suffixes = {0}
    suffix_sum = 0
    for item in reversed(seq):
        suffix_sum += item
        suffixes.add(suffix_sum)
    return suffixes


def find_2_sum(seq, sum_):
    pass
