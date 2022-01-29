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


@pytest.mark.parametrize('graph, expected', [
    pytest.param(
        {},
        False,
        id='it should return False for an empty graph'
    ),
    pytest.param(
        {
            1: [2, 3],
            2: [4, 3, 1],
            3: [2, 1],
            4: [2],
        },
        True,
        id='it should return True when graph has a cycle'
    ),
    pytest.param(
        {
            1: [2],
            2: [4, 3, 1],
            3: [2],
            4: [2],
        },
        False,
        id='it should return False when graph has no cycle'
    ),
    pytest.param(
        {
            1: [2, 1],
            2: [4, 3, 1],
            3: [2],
            4: [2],
        },
        True,
        id='it should return True when graph has a cycle of length 1'
    ),
])
def test_has_cycle(graph, expected):
    assert chapter_7.has_cycle(graph) is expected


@pytest.mark.parametrize('graph, node, expected', [
    pytest.param(
        {
            'A': [('B', 3), ('C', 100), ('D', 13)],
            'B': [('A', 3), ('C', 2)],
            'C': [('B', 2), ('D', 9)],
            'D': [('C', 9), ('A', 13)],
        },
        'A',
        {
            'A': 0,
            'B': 3,
            'C': 5,
            'D': 13,
        },
        id='it should return the shortest paths to each node'
    )
])
def test_get_shortest_paths(get_shortest_paths_algo, graph, node, expected):
    assert get_shortest_paths_algo(graph, node) == expected


@pytest.mark.parametrize('graph, expected', [
])
def test_get_all_shortest_paths(graph, expected):
    assert chapter_7.get_all_shortest_paths(graph) == expected


@pytest.fixture(params=[
    chapter_7.get_shortest_paths_spfa,
    chapter_7.get_shortest_paths_dijkstra,
])
def get_shortest_paths_algo(request):
    return request.param
