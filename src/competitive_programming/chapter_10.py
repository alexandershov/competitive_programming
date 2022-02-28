def tree_dfs(tree, initial_node, prev_node=None):
    yield initial_node
    for node in get_adjacent_nodes(tree, initial_node):
        if node != prev_node:
            yield from tree_dfs(tree, node, initial_node)


def get_adjacent_nodes(tree, node):
    return tree.get(node, [])


def count_subtree_sizes(tree, root, prev_node=None, sizes=None):
    if sizes is None:
        sizes = {}
    cur_size = 1
    for node in get_adjacent_nodes(tree, root):
        if node != prev_node:
            count_subtree_sizes(tree, node, prev_node=root, sizes=sizes)
            cur_size += sizes[node]
    sizes[root] = cur_size
    return sizes


def get_ancestor(tree, node, k):
    pass
