import pytest
from task5_2 import count_digits


@pytest.mark.parametrize("num, expected_value", [
    (12, 2),
    (-2324, 4),
    (122321, 6)
])
def test_count_digits(num, expected_value):
    assert count_digits(num) == expected_value