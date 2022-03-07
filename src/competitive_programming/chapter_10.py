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


def find_centroid(tree):
    if not tree:
        return None
    root = next(iter(tree))
    sizes = count_subtree_sizes(tree, root)
    total_size = sizes[root]
    node = root
    parent = None
    parent_size = 0
    while True:
        children = [
            child for child in get_adjacent_nodes(tree, node)
            if child != parent
        ]

        if _is_centroid(total_size, sizes, children, parent_size):
            return node
        next_ = max(children, key=lambda child: sizes[child])
        parent_size += sizes[node] - sizes[next_]
        parent = node
        node = next_


def _is_centroid(total_size, sizes, children, parent_size):
    max_size = total_size // 2
    cur_sizes = [parent_size]
    for child in children:
        cur_sizes.append(sizes[child])

    return all(a_size <= max_size for a_size in cur_sizes)
