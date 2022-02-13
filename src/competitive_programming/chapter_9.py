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
    range_min = seq[first]
    cur = last
    for i, bit in enumerate(reversed(bin(last - first + 1)[2:])):
        next_ = cur - int(bit) * (2 ** i)
        if next_ != cur:
            range_min = min(range_min, sparse_table[2 ** i][next_ + 1])
            cur = next_
    return range_min


def get_sparse_table(seq: list):
    table = {}
    range_len = 1
    while range_len <= len(seq):
        row = {}
        if range_len == 1:
            for i, item in enumerate(seq):
                row[i] = item
        else:
            for i, item in enumerate(seq):
                if i + range_len <= len(seq):
                    prev = table[range_len // 2]
                    row[i] = min(prev[i], prev[i + range_len // 2])
        table[range_len] = row
        range_len *= 2
    return table
