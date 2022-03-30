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
        {
            '1': ['2', '4'],
            '2': ['1', '5'],
            '3': ['2', '7'],
            '4': [],
            '5': ['4'],
            '6': ['3', '5'],
            '7': ['6'],
        },
        {frozenset('12'), frozenset('4'), frozenset('5'), frozenset('367')},
        id='it should work on an example from the book'
    ),
    pytest.param(
        {},
        set(),
        id='it should return an empty set if graph is empty'
    ),
])
def test_get_strongly_connected_components(graph, expected):
    assert chapter_12.get_strongly_connected_components(graph) == expected
