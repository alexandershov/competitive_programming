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
    costs_in_progress = collections.defaultdict(list, {starting_node: [0]})
    while frontier:
        cost, node = heapq.heappop(frontier)
        heapq.heappop(costs_in_progress[node])
        assert cost >= 0
        if node in result:
            continue
        result[node] = cost
        for neighbour, n_cost in _get_neighbours(graph, node):
            if not costs_in_progress[neighbour] or costs_in_progress[neighbour][0] > cost + n_cost:
                heapq.heappush(frontier, (cost + n_cost, neighbour))
                heapq.heappush(costs_in_progress[neighbour], cost + n_cost)
    return result
