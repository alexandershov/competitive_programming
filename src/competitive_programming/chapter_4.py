def bubble_sort(seq: list):
    for _ in range(len(seq)):
        for i in range(0, len(seq) - 1):
            j = i + 1
            if seq[i] > seq[j]:
                swap(seq, i, j)


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
