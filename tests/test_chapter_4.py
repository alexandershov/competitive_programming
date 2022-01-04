import pytest
from competitive_programming import chapter_4


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [3, 2, 1],
        [1, 2, 3],
        id='should sort input'
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
