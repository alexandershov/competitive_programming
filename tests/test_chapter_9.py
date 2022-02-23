import operator

import pytest

from competitive_programming import chapter_9


@pytest.mark.parametrize('algo', [
    chapter_9.get_range_sum,
    chapter_9.get_fenwick_tree_range_sum,
    chapter_9.get_segment_tree_range_sum,
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
    assert chapter_9.FenwickTree.build(seq) == expected


@pytest.mark.parametrize('seq, index, value, expected', [
    pytest.param(
        [8, 5, 7, 3, 6, 8],
        1, 9,
        chapter_9.FenwickTree([8, 17, 7, 27, 6, 14]),
        id='it should update value at index and related indexes'
    )
])
def test_update_fenwick_tree(seq, index, value, expected):
    tree = chapter_9.FenwickTree.build(seq)
    tree[index] = value
    assert tree == expected


@pytest.mark.parametrize('value, index, expected', [
    pytest.param(
        8, 1,
        chapter_9.Node(
            value=8,
            range=chapter_9.Range(1, 1),
            left=None,
            right=None,
            parent=None,
        ),
        id='it should build a node without parent/children and with range of length 1'
    )
])
def test_node_build_leaf(value, index, expected):
    assert chapter_9.Node.build_leaf(value, index) == expected


@pytest.mark.parametrize('seq, operation, expected_root_value', [
    pytest.param(
        [5, 8, 6, 3, 2, 7, 2, 6], operator.add,
        39,
        id='segment tree root should store sum of all elements'
    )
])
def test_build_segment_tree(seq, operation, expected_root_value):
    tree = chapter_9.SegmentTree.build(seq, operation, 0)
    assert tree.root.value == expected_root_value


@pytest.mark.parametrize('seq, operation, index, expected', [
    pytest.param(
        [5, 3, 1, 7, 6, 4, 2, 8], operator.add, 2,
        1,
        id='it should return node at index'
    ),
])
def test_segment_tree_get_node_at(seq, operation, index, expected):
    tree = chapter_9.SegmentTree.build(seq, operation, 0)
    assert tree.get_node_at(index).value == expected


@pytest.mark.parametrize('x, y, expected', [
    pytest.param(
        chapter_9.Range(1, 5), chapter_9.Range(2, 4),
        chapter_9.Range(2, 4),
        id='it should return smaller range when one range contains another'
    ),
    pytest.param(
        chapter_9.Range(2, 4), chapter_9.Range(1, 5),
        chapter_9.Range(2, 4),
        id='it should return smaller range when one range contains another'
    ),
    pytest.param(
        chapter_9.Range(1, 3), chapter_9.Range(2, 4),
        chapter_9.Range(2, 3),
        id='it should return intersection of two ranges'
    ),
    pytest.param(
        chapter_9.Range(2, 4), chapter_9.Range(1, 3),
        chapter_9.Range(2, 3),
        id='it should return intersection of two ranges'
    ),
    pytest.param(
        chapter_9.Range(1, 3), chapter_9.Range(4, 6),
        None,
        id="it should return None if ranges don't intersect",
    )
])
def test_range_intersection(x, y, expected):
    assert x.intersection(y) == expected


@pytest.mark.parametrize('seq, index, value, expected', [
    pytest.param(
        [5, 8, 6, 3, 2, 7, 2, 6], 2, 9,
        42,
        id='it should update value at the index and its parents'
    )
])
def test_segment_tree_update_value(seq, index, value, expected):
    tree = chapter_9.SegmentTree.build(seq, operator.add, 0)
    tree[index] = value
    assert tree.root.value == expected
