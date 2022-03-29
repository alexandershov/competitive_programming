import pytest

from competitive_programming import chapter_12


@pytest.mark.parametrize('graph, expected', [
])
def test_get_strongly_connected_components(graph, expected):
    assert chapter_12.get_strongly_connected_components(graph) == expected
