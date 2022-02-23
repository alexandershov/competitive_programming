from competitive_programming import chapter_10

import pytest


@pytest.mark.parametrize('tree, initial_node, expected', [
])
def test_tree_dfs(tree, initial_node, expected):
    nodes = set(chapter_10.tree_dfs(tree, initial_node))
    assert nodes == expected
