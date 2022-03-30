import collections


def get_strongly_connected_components_brute_force(graph):
    reachable_by_node = {}
    for node in graph:
        reachable_by_node[node] = get_reachable_nodes(graph, node)
    nodes_by_reachable = collections.defaultdict(set)
    for node, reachable in reachable_by_node.items():
        nodes_by_reachable[frozenset(reachable)].add(node)
    return set(map(frozenset, nodes_by_reachable.values()))


def get_reachable_nodes(graph, node):
    visited = set()
    frontier = [node]
    while frontier:
        cur = frontier.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for neighbour in get_neighbours(graph, cur):
            frontier.append(neighbour)
    return visited


def get_neighbours(graph, node):
    return graph.get(node, [])
