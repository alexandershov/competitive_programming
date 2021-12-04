def n_ary_function(n, x):
    yield f'n_ary_function({n}, {x})'
    if x == 1:
        return
    for _ in range(n):
        yield from n_ary_function(n, x - 1)


def get_max_subarray_sum_brute_force(seq: list[int]) -> int:
    max_sum = 0
    for start in range(len(seq)):
        for end in range(start + 1, len(seq) + 1):
            cur_sum = 0
            for i in range(start, end):
                cur_sum += seq[i]
            max_sum = max(max_sum, cur_sum)
    return max_sum
