from typing import Optional


def bubble_sort(seq: list) -> None:
    for i in range(len(seq)):
        for j in range(0, len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                swap(seq, j, j + 1)


def merge_sort(seq: list, start: int = 0, end: Optional[int] = None) -> None:
    if end is None:
        end = len(seq)

    if (end - start) <= 1:
        return

    mid = (start + end) // 2
    merge_sort(seq, start, mid)
    merge_sort(seq, mid, end)
    merge(seq, start, mid, end)


def merge(seq, start, mid, end):
    merged = []
    left = start
    right = mid

    while (left < mid) or (right < end):
        if (right != end) and ((left == mid) or seq[right] < seq[left]):
            item = seq[right]
            right += 1
        else:
            item = seq[left]
            left += 1

        merged.append(item)

    seq[start:end] = merged


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
