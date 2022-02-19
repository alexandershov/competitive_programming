from competitive_programming import chapter_9

import pytest


@pytest.mark.parametrize('algo', [
    chapter_9.get_range_sum,
    chapter_9.get_fenwick_range_sum,
])
@pytest.mark.parametrize('seq, first, last, expected', [
    pytest.param(
        [8, 10, 12, 6, 7], 1, 3,
        28,
        id='it should return sum of elements in the range [first; last]'
    ),
    pytest.param(
        [8, 10, 12, 6, 7], 1, 1,
        10,
        id='it should return seq[first] when first==last'
    ),
])
def test_get_range_sum(algo, seq, first, last, expected):
    assert algo(seq, first, last) == expected


@pytest.mark.parametrize('seq, first, last, expected', [
    pytest.param(
        [8, 10, 12, 6, 7], 1, 3,
        6,
        id='it should return the minimum value in range'
    ),
    pytest.param(
        [8, 10, 12, 6, 7], 1, 1,
        10,
        id='it should seq[first] when first == last',
    ),
])
def test_get_range_min(seq, first, last, expected):
    assert chapter_9.get_range_min(seq, first, last) == expected


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [8, 5, 7, 3, 6, 8],
        chapter_9.FenwickTree([8, 13, 7, 23, 6, 14]),
        id='it should build a fenwick tree',
    )
])
def test_build_fenwick_tree(seq, expected):
    assert chapter_9.build_fenwick_tree(seq) == expected


@pytest.mark.parametrize('seq, index, value, expected', [
])
def test_update_fenwick_tree(seq, index, value, expected):
    tree = chapter_9.build_fenwick_tree(seq)
    tree[index] = value
    assert tree == expected
