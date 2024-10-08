# test_calculator.py

import pytest

# Parameterized tests for the add method
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

# Parameterized tests for the subtract method
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 0, 0),
    (2.5, 1.0, 1.5),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

# Parameterized tests for the multiply method
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 5, 0),
    (1.5, 2, 3.0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

# Parameterized tests for the divide method
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-9, -3, 3),
    (7.5, 2.5, 3.0),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# Test division by zero
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)