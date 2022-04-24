def find_longest_common_subsequence(left: str, right: str, cache=None) -> str:
    if cache is None:
        cache = {}

    key = (left, right)
    if key in cache:
        return cache[key]

    if not left or not right:
        return ''

    if left[-1] == right[-1]:
        return find_longest_common_subsequence(left[:-1], right[:-1], cache) + left[-1]

    first = find_longest_common_subsequence(left[:-1], right, cache)
    second = find_longest_common_subsequence(left, right[:-1], cache)
    result = max(first, second, key=len)
    cache[key] = result
    return result


def find_minimum_edit_distance(left: str, right: str) -> int:
    distances = {
        (-1, -1): 0,
    }
    for i in range(len(left)):
        distances[(i, - 1)] = i + 1
    for j in range(len(right)):
        distances[(-1, j)] = j + 1

    for i in range(len(left)):
        for j in range(len(right)):
            key = (i, j)
            modify_cost = 0 if left[i] == right[j] else 1
            distances[key] = min(
                distances[(i - 1, j - 1)] + modify_cost,
                distances[(i - 1, j)] + 1,
                distances[(i, j - 1)] + 1,
            )
    return distances[(len(left) - 1, len(right) - 1)]
