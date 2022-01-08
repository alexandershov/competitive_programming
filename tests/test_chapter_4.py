import pytest
from competitive_programming import chapter_4


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [3, 2, 1],
        [1, 2, 3],
        id='should sort input'
    ),
    pytest.param(
        [-3, 2, 1],
        [-3, 1, 2],
        id='should sort input with negative elements'
    ),
    pytest.param(
        [3, 2, 3, 1],
        [1, 2, 3, 3],
        id='should sort input with duplicate elements'
    ),
    pytest.param(
        [],
        [],
        id='should work on empty input'
    ),
    pytest.param(
        [1, 2, 3],
        [1, 2, 3],
        id='should leave sorted input unchanged'
    ),
])
def test_sorting(sorting_algo, seq, expected):
    copy = seq.copy()
    sorting_algo(copy)
    assert copy == expected


@pytest.fixture(
    params=[
        chapter_4.bubble_sort,
        chapter_4.merge_sort,
        chapter_4.counting_sort,
    ]
)
def sorting_algo(request):
    return request.param


def test_islice():
    it = chapter_4.islice([8, 9, 10, 11], 1, 3)
    assert next(it) == 9
    assert next(it) == 10
    with pytest.raises(StopIteration):
        next(it)


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [8, 9, 10],
        True,
        id='it should return True if all elements are unique'
    ),
    pytest.param(
        [],
        True,
        id='it should return True on an empty sequence'
    ),
    pytest.param(
        [8, 9, 8],
        False,
        id='it should return False if some elements are duplicated'
    )
])
def test_all_unique(seq, expected):
    assert chapter_4.all_unique(seq) is expected


@pytest.mark.parametrize('intervals, expected', [
    pytest.param(
        [(18, 19), (10, 20), (15, 25), (23, 24)],
        3,
        id='it should return number of simultaneous visitors'
    ),
    pytest.param(
        [(2, 3), (1, 2)],
        1,
        id='it should handle back-to-back visits'
    ),
    pytest.param(
        [],
        0,
        id='it should handle empty list of visits'
    ),
])
def test_restaurant_problem(intervals, expected):
    assert chapter_4.solve_restaurant_problem(intervals) == expected


@pytest.mark.parametrize('intervals, expected', [
    pytest.param(
        [(1, 100), (0, 4), (8, 15)],
        2,
        id='it should maximize the number of events'
    ),
])
def test_solve_scheduling_problem(intervals, expected):
    assert chapter_4.solve_scheduling_problem(intervals) == expected


@pytest.mark.parametrize('tasks, expected', [
    pytest.param(
        [
            (4, 2),
            (3, 10),
            (2, 8),
            (4, 15),
        ],
        6,
        id='it should greedy choose the task with the minimum duration',
    )
])
def test_solve_deadline_problem(tasks, expected):
    assert chapter_4.solve_deadline_problem(tasks) == expected


@pytest.mark.parametrize('seq, value, expected', [
    pytest.param(
        [1, 3, 20, 40, 80],
        40,
        3,
        id='it should return an index of the value in seq'
    ),
    pytest.param(
        [1, 3, 20, 40, 40, 40, 40, 40, 40, 40, 80],
        40,
        3,
        id='it should return a minimum index of the value in seq'
    ),
    pytest.param(
        [1, 3, 20, 40, 80],
        41,
        -1,
        id='it should return -1 if value is not in seq'
    ),
    pytest.param(
        [],
        40,
        -1,
        id='it should return -1 on an empty array'
    )
])
def test_binary_search(seq, value, expected):
    assert chapter_4.binary_search(seq, value) == expected


@pytest.mark.parametrize('machines, k, expected', [
    pytest.param(
        [10],
        5,
        50,
        id='it should return machines[0] * k when there\'s only one machine'
    ),
    pytest.param(
        [2, 3, 7],
        8,
        9,
        id='it should on the example from the book'
    )
])
def test_solve_machine_problem(machines, k, expected):
    assert chapter_4.solve_machines_problem_brute_force(machines, k) == expected
