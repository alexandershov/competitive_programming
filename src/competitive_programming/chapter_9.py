from dataclasses import dataclass


def get_range_sum(seq: list, first: int, last: int) -> int:
    assert last >= first
    prefix_sums = get_prefix_sums(seq)
    return prefix_sums[last] - prefix_sums[first] + seq[first]


def get_prefix_sums(seq):
    cur_sum = 0
    sums = []
    for item in seq:
        cur_sum += item
        sums.append(cur_sum)
    return sums


def get_range_min(seq: list, first: int, last: int) -> int:
    assert first <= last
    sparse_table = get_sparse_table(seq)
    range_len = last - first + 1
    closest_len = max(size for size in sparse_table if size <= range_len)
    return min(
        sparse_table[closest_len][first],
        sparse_table[closest_len][last - closest_len + 1],
    )


def get_sparse_table(seq: list):
    table = {
        1: dict(enumerate(seq)),
    }
    range_len = 2
    while range_len <= len(seq):
        row = {}
        for i, item in enumerate(seq):
            if i + range_len <= len(seq):
                prev = table[range_len // 2]
                row[i] = min(prev[i], prev[i + range_len // 2])
        table[range_len] = row
        range_len *= 2
    return table


@dataclass(frozen=True)
class FenwickTree:
    # TODO: improve the code
    values: list

    @staticmethod
    def get_length_at_index(index):
        return (index + 1) & -(index + 1)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, item, value):
        seq_value = self._get_seq_value(item)
        change = value - seq_value
        power = 0
        updated = set()
        while True:
            div, mod = divmod(item + 1, 2 ** power)
            index_dividing_power = (div + int(bool(mod))) * 2 ** power - 1
            if index_dividing_power >= len(self.values):
                break
            if index_dividing_power not in updated:
                self.values[index_dividing_power] += change
                updated.add(index_dividing_power)
            power += 1

    def get_range_sum_till(self, last: int) -> int:
        range_sum = 0
        current = last + 1
        while current >= 1:
            length = current & (-current)
            range_sum += self[current - 1]
            current -= length
        return range_sum

    def _get_seq_value(self, item):
        if item == 0:
            original_value = self.values[0]
        else:
            original_value = self.get_range_sum_till(item) - self.get_range_sum_till(item - 1)
        return original_value

    def __eq__(self, other):
        if not isinstance(other, FenwickTree):
            return False
        return self.values == other.values


def build_fenwick_tree(seq: list) -> FenwickTree:
    # TODO: is there a way with less extra memory
    prefix_sums = get_prefix_sums(seq)
    values = []
    for last in range(0, len(seq)):
        length = FenwickTree.get_length_at_index(last)
        first = last - length + 1
        last_value = prefix_sums[last] - prefix_sums[first] + seq[first]
        values.append(last_value)
    return FenwickTree(values)


def get_fenwick_range_sum(seq: list, first: int, last: int) -> int:
    assert first <= last
    tree = build_fenwick_tree(seq)
    sum_till_last = tree.get_range_sum_till(last)
    sum_till_first = tree.get_range_sum_till(first)
    return sum_till_last - sum_till_first + seq[first]
