from competitive_programming import chapter_10

import pytest


@pytest.mark.parametrize('tree, initial_node, expected', [
    pytest.param(
        {
            'A': ['C', 'D'],
            'B': ['D'],
            'C': ['A', 'E'],
            'D': ['A', 'B', 'F', 'G'],
            'E': ['C'],
            'F': ['D'],
            'G': ['D'],
        },
        'D',
        {'A', 'B', 'C', 'D', 'E', 'F', 'G'},
        id='it should traverse all nodes in a tree',
    )
])
def test_tree_dfs(tree, initial_node, expected):
    nodes = set(chapter_10.tree_dfs(tree, initial_node))
    assert nodes == expected


@pytest.mark.parametrize('tree, root, expected', [
    pytest.param(
        {
            'A': ['C', 'D'],
            'C': ['A', 'E'],
            'D': ['A', 'F', 'G'],
            'E': ['C'],
            'F': ['D'],
            'G': ['D'],
        },
        'A',
        {
            'A': 6,
            'C': 2,
            'D': 3,
            'E': 1,
            'F': 1,
            'G': 1,
        },
        id='it should count subtree size for every node'
    )
])
def test_count_subtree_sizes(tree, root, expected):
    sizes = chapter_10.count_subtree_sizes(tree, root)
    assert sizes == expected


@pytest.mark.parametrize('tree, node, k, expected', [
])
def test_get_ancestor(tree, node, k, expected):
    assert chapter_10.get_ancestor(tree, node, k) == expected
