import pytest
from app.calculation import Addition  # Assuming your class is saved in a module named 'calculation_module'

# Test the Addition class for different sets of input using pytest's parametrize
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),     # simple addition
    (0, 0, 0),     # edge case with zeros
    (-1, -1, -2),  # adding two negative numbers
    (100, 200, 300),  # larger positive numbers
    (-10, 20, 10),  # one negative, one positive
    (0.5, 1.5, 2.0),  # floating point addition
    (-0.5, 1.5, 1.0), # negative floating point and positive floating point
])
def test_addition_compute(a, b, expected):
    # Create an Addition object using the inputs 'a' and 'b'
    addition = Addition.create(a, b)
    
    # Assert that the compute method returns the expected value
    assert addition.compute() == expected, f"Expected {expected}, but got {addition.compute()}"
    
# Test for error scenarios (invalid types)
@pytest.mark.parametrize("a, b", [
    ("a", 1),  # string and number
    (None, 1), # None and number
    ([1, 2], 1),  # list and number
    (object(), 1),  # generic object and number
])
def test_addition_invalid_types(a, b):
    # Expecting a TypeError when invalid types are passed
    with pytest.raises(TypeError):
        addition = Addition(a, b)
        addition.compute()