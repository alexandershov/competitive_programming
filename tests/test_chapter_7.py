from competitive_programming import chapter_7


def dfs():
    graph = {
        1: [8, 9],
        9: [10, 11],
        11: [2, 1],
    }

    nodes = list(chapter_7.dfs(graph, 1))
    assert nodes == [1, 9, 11, 2, 10, 8]
