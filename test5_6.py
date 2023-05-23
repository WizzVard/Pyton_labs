import pytest
from task8_9_5_6 import count_days_in_month, leap_year


@pytest.mark.parametrize('month, expected_value', [
    ("June", 30),
    ("April", 30),
    ("March", 31),
])
def test_count_days_in_month(month, expected_value):
    result = count_days_in_month(month)
    assert result == expected_value


@pytest.mark.parametrize('year, expected_value', [
    (1000, "Ordinary year"),
    (1904, "Leap year"),
    (4034, "Ordinary year"),
])
def test_leap_year(year, expected_value):
    result = leap_year(year)
    assert result == expected_value

