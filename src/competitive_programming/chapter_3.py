def n_ary_function(n, x):
    yield f'n_ary_function({n}, {x})'
    if x == 1:
        return
    for _ in range(n):
        yield from n_ary_function(n, x - 1)


def get_max_subarray_sum_cubic(seq: list[int]) -> int:
    if not seq:
        return 0

    max_sum = seq[0]
    for start in range(len(seq)):
        for end in range(start + 1, len(seq) + 1):

            cur_sum = 0
            for i in range(start, end):
                cur_sum += seq[i]
            max_sum = max(max_sum, cur_sum)

    return max_sum


def get_max_subarray_sum_quadratic(seq: list[int]) -> int:
    if not seq:
        return 0

    max_sum = seq[0]

    sums = [0] * (len(seq) + 1)  # sums[i] = sum(itertools.islice(seq, i))
    for start in range(len(seq)):
        for i in range(start, len(seq)):
            sums[start] += seq[i]

    for start in range(len(seq)):
        for end in range(start + 1, len(seq) + 1):
            cur_sum = sums[start] - sums[end]
            max_sum = max(max_sum, cur_sum)

    return max_sum


def get_max_subarray_sum_linear(seq: list[int]) -> int:
    sums = seq.copy()
    index = len(sums) - 2
    while index >= 0:
        if sums[index + 1] > 0:
            sums[index] += sums[index + 1]
        index -= 1
    return max(sums, default=0)
