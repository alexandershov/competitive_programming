# graph algorithms
import collections


def dfs(graph, starting_node):
    frontier = [starting_node]
    visited = set()
    while frontier:
        node = frontier.pop()
        yield node
        visited.add(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
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
