def tree_dfs(tree, initial_node, prev_node=None):
    yield initial_node
    for node in get_adjacent_nodes(tree, initial_node):
        if node != prev_node:
            yield from tree_dfs(tree, node, initial_node)


def get_adjacent_nodes(tree, node):
    return tree.get(node, [])
