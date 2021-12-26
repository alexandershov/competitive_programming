import pytest
from competitive_programming import chapter_4


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [3, 1, 2],
        [1, 2, 3],
        id='should sort input'
    )
])
def test_sorting(sorting_algo, seq, expected):
    copy = seq.copy()
    sorting_algo(copy)
    assert copy == expected


@pytest.fixture(
    params=[
        chapter_4.bubble_sort,
    ]
)
def sorting_algo(request):
    return request.param
