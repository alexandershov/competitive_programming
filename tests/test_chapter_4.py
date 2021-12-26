import pytest


@pytest.mark.parametrize('seq, expected', [
])
def test_sorting(sorting_algo, seq, expected):
    copy = seq.copy()
    sorting_algo(copy)
    assert copy == expected


@pytest.fixture(
    params=[]
)
def sorting_algo(request):
    return request.param
