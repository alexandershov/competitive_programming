def find_longest_common_subsequence(left: str, right: str) -> str:
    # TODO: add caching
    if not left or not right:
        return ''
    if left[-1] == right[-1]:
        return find_longest_common_subsequence(left[:-1], right[:-1]) + left[-1]
    first = find_longest_common_subsequence(left[:-1], right)
    second = find_longest_common_subsequence(left, right[:-1])
    return max(first, second, key=len)
