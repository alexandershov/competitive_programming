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
    pass
