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
    pytest.param(
        {
            'A': ['B', 'E'],
            'B': ['A', 'C', 'D'],
            'C': ['B'],
            'D': ['B'],
            'E': ['A', 'F', 'G'],
            'F': 'E',
            'G': 'E',
        },
        'F',
        2,
        'A',
        id='it should return k-th ancestor of the given node'
    ),
    pytest.param(
        {
            'A': ['B', 'C'],
        },
        'C',
        2,
        None,
        id='it should return None if tree is too small'
    ),
    pytest.param(
        {},
        'A',
        1,
        None,
        id='it should return None for empty tree'
    ),
])
def test_get_ancestor(tree, node, k, expected):
    assert chapter_10.get_ancestor(tree, node, k) == expected


@pytest.mark.parametrize('tree, values, root, node, expected', [
    pytest.param(
        {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A'],
        },
        {
            'A': 'blue',
            'B': 'yellow',
            'C': 'yellow',
        },
        'A', 'A', 2,
        id='it should return number of distinct colors at the given subtree'
    ),
    pytest.param(
        {
            'A': [],
        },
        {
            'A': 'blue',
        },
        'A', 'A', 1,
        id='it should return 1 on a singleton tree'
    )

])
def test_count_subtree_colors(tree, values, root, node, expected):
    assert chapter_10.count_subtree_colors(tree, values, root, node) == expected


@pytest.mark.parametrize('tree, expected_nodes', [
    pytest.param(
        {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B', 'D', 'F'],
            'D': ['C', 'E'],
            'F': ['C', 'G', 'H'],
            'G': ['F'],
            'H': ['F'],
        },
        {'C'},
        id='it should find the centroid'
    )
])
def test_find_centroid(tree, expected_nodes):
    assert chapter_10.find_centroid(tree) in expected_nodes
