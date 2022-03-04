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
    if not tree:
        return None
    return walk_tree_with_path(
        tree=tree,
        root=next(iter(tree)),
        node=node,
        k=k,
        path=[],
    )


def walk_tree_with_path(tree, root, node, k, path):
    if root == node:
        try:
            return path[-k]
        except IndexError:
            return None
    for child in get_adjacent_nodes(tree, root):
        prev = None
        if path:
            prev = path[-1]
        if child != prev:
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
