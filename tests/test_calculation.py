import pytest
from app.calculation import Addition, Subtraction, Multiplication, Division  # Assuming your classes are in 'calculation' module

# Test the Addition class for different sets of input using pytest's parametrize
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),     # simple addition
    (0, 0, 0),     # edge case with zeros
    (-1, -1, -2),  # adding two negative numbers
    (100, 200, 300),  # larger positive numbers
    (-10, 20, 10),  # one negative, one positive
    (0.5, 1.5, 2.0),  # floating point addition
    (-0.5, 1.5, 1.0), # negative and positive floating points
])
def test_addition_compute(a, b, expected):
    addition = Addition.create(a, b)
    assert addition.compute() == expected, f"Expected {expected}, but got {addition.compute()}"


# Test the Subtraction class
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),      # simple subtraction
    (0, 0, 0),      # subtracting zero from zero
    (-1, -1, 0),    # subtracting two negative numbers
    (100, 50, 50),  # larger positive numbers
    (-10, 20, -30), # one negative, one positive
    (0.5, 1.5, -1.0),  # floating point subtraction
    (-0.5, 1.5, -2.0), # negative and positive floating points
])
def test_subtraction_compute(a, b, expected):
    subtraction = Subtraction.create(a, b)
    assert subtraction.compute() == expected, f"Expected {expected}, but got {subtraction.compute()}"


# Test the Multiplication class
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),      # simple multiplication
    (0, 100, 0),    # multiplying by zero
    (-1, -1, 1),    # multiplying two negative numbers
    (100, 2, 200),  # larger positive numbers
    (-10, 20, -200), # one negative, one positive
    (0.5, 2, 1.0),  # floating point multiplication
    (-0.5, 1.5, -0.75), # negative and positive floating points
])
def test_multiplication_compute(a, b, expected):
    multiplication = Multiplication.create(a, b)
    assert multiplication.compute() == expected, f"Expected {expected}, but got {multiplication.compute()}"


# Test the Division class
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),      # simple division
    (1, 1, 1),      # dividing the same number
    (-1, -1, 1),    # dividing two negative numbers
    (100, 2, 50),   # larger positive numbers
    (-10, 2, -5),   # one negative, one positive
    (0.5, 0.5, 1.0),  # floating point division
    (-0.5, 0.5, -1.0), # negative and positive floating points
])
def test_division_compute(a, b, expected):
    division = Division.create(a, b)
    assert division.compute() == expected, f"Expected {expected}, but got {division.compute()}"


# Test for division by zero (this should raise an error)
@pytest.mark.parametrize("a, b", [
    (1, 0),   # divide by zero
    (100, 0), # divide by zero with larger numbers
])
def test_division_by_zero(a, b):
    division = Division.create(a, b)
    with pytest.raises(ZeroDivisionError):
        division.compute()

@pytest.mark.parametrize("a, b, operation", [
    ("a", 1, Addition),  # string and number for addition
    (None, 1, Subtraction),  # None and number for subtraction
    ([1, 2], 1, Multiplication),  # list and number for multiplication
    (object(), 1, Division),  # generic object and number for division
])
def test_invalid_types(a, b, operation):
    # The TypeError should be raised when trying to create the object
    with pytest.raises(TypeError):
        calculation = operation.create(a, b)
