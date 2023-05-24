import pytest
from task8_9_8 import calculator


@pytest.mark.parametrize('a, b, op, expected_value', [
    (20, 5, '*', 100),
    (20, 5, '/', 4),
    (20, 5, '+', 25),
    (20, 5, '-', 15),
    (20, 5, 'mod', 0),
    (20, 5, 'pow', 3200000),
    (20, 5, 'div', 4)

])
def test_calculator(a, b, op, expected_value):
    result = calculator(a, b, op)
    assert result == expected_value




