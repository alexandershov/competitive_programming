import itertools

from competitive_programming import chapter_2


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
    if not seq:
        return 0

    prev = 0
    max_sum = seq[0]
    for i in range(len(seq)):
        cur = seq[i] + max(prev, 0)
        max_sum = max(max_sum, cur)
        prev = cur
    return max_sum


def solve_two_queens_problem_brute_force(size: int) -> int:
    squares = get_all_squares(size)
    count = 0
    for src, dst in itertools.combinations(squares, 2):
        if not queen_can_move(src, dst):
            count += 1
    return count


def get_all_squares(size: int) -> list[chapter_2.Square]:
    squares = []
    for column in range(size):
        for row in range(size):
            squares.append(chapter_2.Square(column, row, size))
    return squares


def queen_can_move(src: chapter_2.Square, dst: chapter_2.Square) -> bool:
    same_line = (src.row == dst.row) or (src.column == dst.column)
    same_up_diagonal = (src.up_diagonal == dst.up_diagonal)
    same_down_diagonal = (src.down_diagonal == dst.down_diagonal)

    return same_line or same_up_diagonal or same_down_diagonal


def get_up_diagonal_length(square: chapter_2.Square) -> int:
    free_columns = square.size - square.column
    free_rows = square.size - square.row
    return min(free_rows, free_columns)


def get_down_diagonal_length(square: chapter_2.Square) -> int:
    free_columns = square.size - square.column
    free_rows = square.row + 1
    return min(free_rows, free_columns)
