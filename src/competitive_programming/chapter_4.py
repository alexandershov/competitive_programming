def bubble_sort(seq: list):
    for i in range(len(seq)):
        for j in range(0, len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                swap(seq, j, j + 1)


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
