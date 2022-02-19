def get_range_sum(seq: list, first: int, last: int) -> int:
    assert last >= first
    prefix_sums = get_prefix_sums(seq)
    return prefix_sums[last] - prefix_sums[first] + seq[first]


def get_prefix_sums(seq):
    cur_sum = 0
    sums = []
    for item in seq:
        cur_sum += item
        sums.append(cur_sum)
    return sums


def get_range_min(seq: list, first: int, last: int) -> int:
    assert first <= last
    sparse_table = get_sparse_table(seq)
    range_len = last - first + 1
    closest_len = max(size for size in sparse_table if size <= range_len)
    return min(
        sparse_table[closest_len][first],
        sparse_table[closest_len][last - closest_len + 1],
    )


def get_sparse_table(seq: list):
    table = {
        1: dict(enumerate(seq)),
    }
    range_len = 2
    while range_len <= len(seq):
        row = {}
        for i, item in enumerate(seq):
            if i + range_len <= len(seq):
                prev = table[range_len // 2]
                row[i] = min(prev[i], prev[i + range_len // 2])
        table[range_len] = row
        range_len *= 2
    return table


def build_fenwick_tree(seq: list) -> list:
    prefix_sums = get_prefix_sums(seq)
    tree = []
    for last in range(0, len(seq)):
        length = (last + 1) & -(last + 1)
        first = last - length + 1
        value = prefix_sums[last] - prefix_sums[first] + seq[first]
        tree.append(value)
    return tree


def get_fenwick_range_sum_till(seq: list, last: int) -> int:
    tree = build_fenwick_tree(seq)
    range_sum = 0
    current = last + 1
    while current >= 1:
        length = current & (-current)
        range_sum += tree[current - 1]
        current -= length
    return range_sum


def get_fenwick_range_sum(seq: list, first: int, last: int) -> int:
    assert first <= last
    return get_fenwick_range_sum_till(seq, last) - get_fenwick_range_sum_till(seq, first) + seq[
        first]
