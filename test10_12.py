import pytest
from task8_9_10_12 import validate_input, dec_to_bin, bin_to_dec, r_p_s


@pytest.mark.parametrize('row, col, expected_value', [
    ('a', 1, 'black'),
    ('h', 3, 'white'),
    ('b', 6, 'black'),
])
def test_get_color(row, col, expected_value):
    result = validate_input(row, col)
    assert result == expected_value


@pytest.mark.parametrize('num, expected_value', [
    (12, '1100'),
    (34, '100010'),
    (104, '1101000')
])
def test_dec_to_bin(num, expected_value):
    result = dec_to_bin(num)
    assert result == expected_value


@pytest.mark.parametrize('num, expected_value', [
    ('1100', 12),
    ('100010', 34),
    ('111000', 56)
])
def test_bin_to_dec(num, expected_value):
    result = bin_to_dec(num)
    assert result == expected_value