from typing import Optional

Interval = tuple[int, int]


def bubble_sort(seq: list) -> None:
    for i in range(len(seq)):
        for j in range(0, len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                swap(seq, j, j + 1)


def merge_sort(seq: list, start: int = 0, end: Optional[int] = None) -> None:
    if end is None:
        end = len(seq)

    if (end - start) <= 1:
        return

    mid = (start + end) // 2
    merge_sort(seq, start, mid)
    merge_sort(seq, mid, end)
    merged = merge(islice(seq, start, mid), islice(seq, mid, end))

    seq[start:end] = merged


def counting_sort(seq: list) -> None:
    if not seq:
        return

    minimum = min(seq)
    maximum = max(seq)

    counts = [0] * (maximum - minimum + 1)

    for item in seq:
        bucket = item - minimum
        counts[bucket] += 1

    index = 0
    for bucket, count in enumerate(counts):
        for _ in range(count):
            item = bucket + minimum
            seq[index] = item
            index += 1


def merge(*iters):
    values_by_it = {}
    for it in iters:
        try_add_next_value(values_by_it, it)

    while values_by_it:
        min_it = min(values_by_it, key=values_by_it.__getitem__)
        yield values_by_it.pop(min_it)

        try_add_next_value(values_by_it, min_it)


def try_add_next_value(values_by_it, it):
    try:
        values_by_it[it] = next(it)
    except StopIteration:
        pass


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def islice(seq, start, end):
    for i in range(start, end):
        yield seq[i]


def all_unique(seq: list) -> bool:
    merge_sort(seq)
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            return False
    return True


def solve_restaurant_problem(intervals: list[Interval]) -> int:
    events = []
    for (start, end) in intervals:
        events.append((start, +1))
        events.append((end, -1))
    events.sort()
    cur = 0
    result = 0
    for time, action in events:
        cur += action
        result = max(result, cur)
    return result


def solve_scheduling_problem(intervals: list[Interval]) -> int:
    intervals.sort(key=_by_end)
    schedule = []
    for cur in intervals:
        if not schedule:
            schedule.append(cur)
        elif are_disjoint(schedule[-1], cur):
            schedule.append(cur)

    return len(schedule)


def are_disjoint(left: Interval, right: Interval) -> bool:
    return right[0] >= left[1] or right[1] <= left[0]


def _by_end(interval: Interval) -> int:
    return interval[1]


def solve_deadline_problem(tasks: list[tuple[int, int]]) -> int:
    score = 0
    cur_time = 0
    for duration, deadline in sorted(tasks):
        cur_time += duration
        score += deadline - cur_time
    return score


def binary_search(seq: list, value) -> int:
    start = 0
    end = len(seq)
    result = -1
    while start < end:
        middle = (start + end) // 2
        if seq[middle] == value:
            if result == -1:
                result = middle
            else:
                result = min(middle, result)
            end = middle
        elif seq[middle] > value:
            end = middle
        else:
            start = middle + 1

    return result


def solve_machines_problem_brute_force(machines: list[int], k: int) -> int:
    return _solve_sorted_machines_problem(sorted(machines), k, len(machines))


def _solve_sorted_machines_problem(machines: list[int], k: int, end: int) -> int:
    assert end > 0

    assert k > 0
    if end == 1:
        return machines[0] * k
    best = None
    for slowest_k in range(0, k):
        solution = _solve_sorted_machines_problem(machines, k - slowest_k, end - 1)
        if best is None:
            best = solution
        else:
            best = min(best, max(solution, machines[end - 1] * slowest_k))
    return best
