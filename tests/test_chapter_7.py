import pytest

from competitive_programming import chapter_7


def test_dfs(search_algo):
    graph = {
        1: [8, 9],
        9: [10, 11],
        11: [2, 1],
    }

    nodes = list(search_algo(graph, 1))
    assert nodes == [1, 9, 11, 2, 10, 8]


@pytest.fixture(params=[chapter_7.dfs])
def search_algo(request):
    return request.param
