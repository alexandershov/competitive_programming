# graph algorithms

def dfs(graph, starting_node):
    frontier = [starting_node]
    visited = set()
    while frontier:
        node = frontier.pop()
        yield node
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                frontier.append(neighbour)
