import pytest

from competitive_programming import chapter_7


def test_dfs(search_algo):
    graph = {
        1: [2, 3],
        2: [4, 3],
    }

    nodes = list(search_algo(graph, 1))
    assert nodes == [1, 2, 4, 3]


def test_bfs(search_algo):
    graph = {
        1: [8, 9],
        8: [10, 11],
        11: [2, 1],
    }

    nodes = list(chapter_7.bfs(graph, 1))
    assert nodes == [1, 8, 9, 10, 11, 2]


@pytest.fixture(params=[chapter_7.dfs, chapter_7.rec_dfs])
def search_algo(request):
    return request.param
