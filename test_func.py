import pytest
from task3 import func


@pytest.mark.parametrize("x, c, b, expected_value", [
    (11, 3, 10, 27.0),
    (20, 5, 4, 23.75),
    (9, 3, 5, 13.5),
])
def test_func(x, c, b, expected_value):
    result = func(x, c, b)
    assert result == expected_value