# graph algorithms
import collections
import heapq
from dataclasses import dataclass


def dfs(graph, starting_node):
    frontier = [starting_node]
    visited = set()
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        yield node
        visited.add(node)
        for neighbour in reversed(graph.get(node, [])):
            frontier.append(neighbour)


def rec_dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return

    yield node
    visited.add(node)
    for neighbour in graph.get(node, []):
        yield from rec_dfs(graph, neighbour, visited)


def bfs(graph, starting_node):
    frontier = collections.deque([starting_node])
    visited = set()
    while frontier:
        node = frontier.popleft()
        if node in visited:
            continue
        yield node
        visited.add(node)
        for neighbour in graph.get(node, []):
            frontier.append(neighbour)


def has_cycle(graph) -> bool:
    return any(dfs_has_cycle(graph, node) for node in graph)


@dataclass
class Path:
    nodes: list[int]
    visited: set[int]

    @staticmethod
    def empty():
        return Path(nodes=[], visited=set())

    def add(self, node: int):
        self.nodes.append(node)
        self.visited.add(node)

    def remove(self):
        node = self.nodes.pop()
        self.visited.remove(node)

    def has_visited(self, node: int) -> bool:
        return node in self.visited

    def will_lead_to_trivial_cycle(self, node) -> bool:
        if len(self.nodes) < 2:
            return False
        return self.nodes[-2] == node


def dfs_has_cycle(graph, node, path=None) -> bool:
    if path is None:
        path = Path.empty()

    for neighbour in _get_neighbours(graph, node):
        if not path.will_lead_to_trivial_cycle(neighbour):
            if path.has_visited(neighbour):
                return True
            path.add(neighbour)
            result = dfs_has_cycle(graph, neighbour, path)
            path.remove()
            if result:
                return result
    return False


def _get_neighbours(graph, node):
    return graph.get(node, [])


def get_shortest_paths_spfa(graph, starting_node):
    weights = {starting_node: 0}
    frontier = collections.deque([starting_node])
    while frontier:
        node = frontier.popleft()
        for neighbour, n_weight in _get_neighbours(graph, node):
            new_weight = weights[node] + n_weight
            if new_weight < weights.get(neighbour, float('inf')):
                weights[neighbour] = new_weight
                frontier.append(neighbour)
    return weights


def get_shortest_paths_dijkstra(graph, starting_node):
    result = {}
    frontier = [(0, starting_node)]
    current_weights = {starting_node: 0}
    while frontier:
        weight, node = heapq.heappop(frontier)
        assert weight >= 0
        if node in result:
            continue
        result[node] = weight
        for neighbour, edge_weight in _get_neighbours(graph, node):
            n_weight = weight + edge_weight
            if n_weight < current_weights.get(neighbour, float('inf')):
                heapq.heappush(frontier, (n_weight, neighbour))
                current_weights[neighbour] = n_weight
    return result


def get_all_shortest_paths(graph):
    result = {}
    nodes = list(graph)
    for src in nodes:
        for dst, weight in get_shortest_paths_spfa(graph, src).items():
            result[(src, dst)] = weight
    return result


def get_all_shortest_paths_floyd_warshall(graph):
    result = collections.defaultdict(lambda: float('inf'))
    for node in graph:
        result[(node, node)] = 0
        for neighbour, n_weight in _get_neighbours(graph, node):
            result[node, neighbour] = n_weight

    for intermediate in graph:
        for src in graph:
            for dst in graph:
                path = (src, dst)
                new_weight = result[(src, intermediate)] + result[intermediate, dst]
                result[path] = min(new_weight, result[path])
    return dict(result)


def topological_sort_brute_force(graph) -> dict[int, set]:
    group_by_node = {}  # node -> group
    nodes_with_parents = set()
    for neighbours in graph.values():
        nodes_with_parents.update(neighbours)
    starting_nodes = set(graph) - nodes_with_parents
    frontier = [(node, 0) for node in starting_nodes]
    while frontier:
        node, node_group = frontier.pop()
        group_by_node[node] = max(group_by_node.get(node, -1), node_group)
        for neighbour in _get_neighbours(graph, node):
            frontier.append((neighbour, node_group + 1))
    result = collections.defaultdict(set)
    for node, group in group_by_node.items():
        result[group].add(node)
    return dict(result)


def count_paths(graph, src, dst) -> int:
    counts = collections.Counter({dst: 1})
    rec_count_paths(graph, src, dst, counts)
    return counts[src]


def rec_count_paths(graph, src, dst, counts):
    if src in counts:
        return counts[src]
    src_count = 0
    for node in _get_neighbours(graph, src):
        src_count += rec_count_paths(graph, node, dst, counts)
    counts[src] = src_count
    return src_count


def count_paths_dynamic_programming(graph, src, dst) -> int:
    nodes = topological_sort(graph)
    counts = collections.Counter({src: 1})
    parents = collections.defaultdict(set)
    for a_node, neighbours in graph.items():
        for a_neighbour in neighbours:
            parents[a_neighbour].add(a_node)
    for a_node in nodes:
        for a_parent in parents[a_node]:
            counts[a_node] += counts[a_parent]
    return counts[dst]


def topological_sort(graph):
    result = []
    visited = set()
    for node in graph:
        topological_visit(graph, node, visited, result)
    return list(reversed(result))


def topological_visit(graph, node, visited, result):
    if node in visited:
        return
    for neighbour in _get_neighbours(graph, node):
        topological_visit(graph, neighbour, visited, result)
    visited.add(node)
    result.append(node)


def get_successor_cycle_length(graph, node) -> int:
    node_in_cycle = get_node_in_cycle(graph, node)
    cur = node_in_cycle
    length = 0
    while True:
        cur = succ(graph, cur)
        length += 1
        if cur == node_in_cycle:
            return length


def get_node_in_cycle(graph, node):
    slow = node
    fast = node
    while True:
        for i in range(2):
            fast = succ(graph, fast)
            if slow == fast:
                return slow
        slow = succ(graph, slow)


def succ(graph, node):
    neighbours = _get_neighbours(graph, node)
    assert len(neighbours) == 1
    return neighbours[0]
