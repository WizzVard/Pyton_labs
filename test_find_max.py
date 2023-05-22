import pytest
from task4 import find_max


@pytest.mark.parametrize('left_contour, right_contour, expected_output', [
    (0, 1, 1.382),
    (1, 2, 1.566),
    (2, 3, 1.862),
    (3, 4, 2.951),
])
def test_find_max(left_contour, right_contour, expected_output):
    assert find_max(left_contour, right_contour) == expected_output
