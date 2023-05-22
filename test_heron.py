import pytest
from task5_3 import heron


@pytest.mark.parametrize("a, x, expected_value", [
    (9, 3, 3.0),
    (16, 4, 4.0),
    (36, 15, 6.0),
    (81, 50, 9.0)
])
def test_calculate_heron(a, x, expected_value):
    result = heron(a, x)
    assert result == expected_value