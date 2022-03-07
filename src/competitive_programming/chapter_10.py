import collections


def tree_dfs(tree, initial_node, parent=None):
    yield initial_node
    for node in get_adjacent_nodes(tree, initial_node):
        if node != parent:
            yield from tree_dfs(tree, node, initial_node)


def get_adjacent_nodes(tree, node):
    return tree.get(node, [])


def count_subtree_sizes(tree, root, parent=None, sizes=None):
    if sizes is None:
        sizes = {}
    cur_size = 1
    for node in get_adjacent_nodes(tree, root):
        if node != parent:
            count_subtree_sizes(tree, node, parent=root, sizes=sizes)
            cur_size += sizes[node]
    sizes[root] = cur_size
    return sizes


def get_ancestor(tree, node, k):
    if not tree:
        return None
    try:
        return walk_tree_with_path(
            tree=tree,
            root=next(iter(tree)),
            node=node,
            k=k,
            path=[],
        )
    except IndexError:
        return None


def walk_tree_with_path(tree, root, node, k, path):
    if root == node:
        return path[-k]
    for child in get_adjacent_nodes(tree, root):
        if child != get_last_or_none(path):
            path.append(root)
            result = walk_tree_with_path(
                tree=tree,
                root=child,
                node=node,
                k=k,
                path=path,
            )
            path.pop()
            if result is not None:
                return result
    return None


def get_last_or_none(seq):
    if seq:
        return seq[-1]
    return None


def count_subtree_colors(tree, values, root, node):
    counts = collections.defaultdict(int)
    distinct_values_dfs(
        tree=tree,
        values=values,
        node=root,
        parent=None,
        counts=counts,
    )
    return counts[node]


def distinct_values_dfs(tree, values, node, parent, counts, values_by_node=None):
    if values_by_node is None:
        values_by_node = {}
    node_values = {values[node]}
    for child in get_adjacent_nodes(tree, node):
        if child != parent:
            distinct_values_dfs(
                tree=tree,
                values=values,
                node=child,
                parent=node,
                counts=counts,
                values_by_node=values_by_node
            )
            if len(values_by_node[child]) > len(node_values):
                node_values, values_by_node[child] = values_by_node[child], node_values
            node_values.update(values_by_node[child])
    values_by_node[node] = node_values
    counts[node] = len(node_values)
