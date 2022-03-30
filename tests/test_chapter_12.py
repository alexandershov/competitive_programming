import pytest

from competitive_programming import chapter_12


@pytest.mark.parametrize('graph, expected', [
    pytest.param(
        {
            'A': ['B'],
            'B': ['C'],
            'C': ['D'],
            'D': ['B']
        },
        {frozenset('A'), frozenset('BCD')},
        id='it should return strongly connected components of a graph'
    ),
    pytest.param(
        {},
        set(),
        id='it should return an empty set if graph is empty'
    ),
])
def test_get_strongly_connected_components(graph, expected):
    assert chapter_12.get_strongly_connected_components(graph) == expected
