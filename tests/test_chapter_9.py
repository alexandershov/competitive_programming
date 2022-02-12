from competitive_programming import chapter_9

import pytest


@pytest.mark.parametrize('seq, first, last, expected', [
])
def test_get_range_sum(seq, first, last, expected):
    assert chapter_9.get_range_sum(seq, first, last) == expected
