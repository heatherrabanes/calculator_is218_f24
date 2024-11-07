'''Validators tests'''
from decimal import Decimal
import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError
from app.input_validators import InputValidator  # adjust as per your file structure

# Sample configuration with a max input value of 1 million for testing purposes
config = CalculatorConfig(max_input_value=Decimal('1000000'))

# Test cases for InputValidator.validate_number

def test_validate_number_positive_integer():
    '''Test to validate positive integer'''
    assert InputValidator.validate_number(123, config) == Decimal('123')

def test_validate_number_positive_decimal():
    '''Test to validate positive decimal'''
    assert InputValidator.validate_number(123.456, config) == Decimal('123.456').normalize()

def test_validate_number_positive_string_integer():
    '''Test to validate positive string integer'''
    assert InputValidator.validate_number("123", config) == Decimal('123')

def test_validate_number_positive_string_decimal():
    '''Test to validate positive string decimal'''
    assert InputValidator.validate_number("123.456", config) == Decimal('123.456').normalize()

def test_validate_number_negative_integer():
    '''Test to validate negative integer'''
    assert InputValidator.validate_number(-789, config) == Decimal('-789')

def test_validate_number_negative_decimal():
    '''Test to validate negative decimal'''
    assert InputValidator.validate_number(-789.123, config) == Decimal('-789.123').normalize()

def test_validate_number_negative_string_integer():
    '''Test to validate negative string integer'''
    assert InputValidator.validate_number("-789", config) == Decimal('-789')

def test_validate_number_negative_string_decimal():
    '''Test to validate negative string decimal'''
    assert InputValidator.validate_number("-789.123", config) == Decimal('-789.123').normalize()

def test_validate_number_zero():
    '''Test to validate zero'''
    assert InputValidator.validate_number(0, config) == Decimal('0')

def test_validate_number_trimmed_string():
    '''Test to validate trimmed string'''
    assert InputValidator.validate_number("  456  ", config) == Decimal('456')

# Negative test cases
def test_validate_number_invalid_string():
    '''Test to validate invalid string'''
    with pytest.raises(ValidationError, match="Invalid number format: abc"):
        InputValidator.validate_number("abc", config)

def test_validate_number_exceeds_max_value():
    '''Test to validate number exceeding max value'''
    with pytest.raises(ValidationError, match="Value exceeds maximum allowed"):
        InputValidator.validate_number(Decimal('1000001'), config)

def test_validate_number_exceeds_max_value_string():
    '''Test to validate string exceeding max value'''
    with pytest.raises(ValidationError, match="Value exceeds maximum allowed"):
        InputValidator.validate_number("1000001", config)

def test_validate_number_exceeds_negative_max_value():
    '''Test to validate negative number exceeding max value'''
    with pytest.raises(ValidationError, match="Value exceeds maximum allowed"):
        InputValidator.validate_number(-Decimal('1000001'), config)

def test_validate_number_empty_string():
    '''Test to validate empty string'''
    with pytest.raises(ValidationError, match="Invalid number format: "):
        InputValidator.validate_number("", config)

def test_validate_number_whitespace_string():
    '''Test to validate whitespace string'''
    with pytest.raises(ValidationError, match="Invalid number format: "):
        InputValidator.validate_number("   ", config)

def test_validate_number_none_value():
    '''Test to validate no value'''
    with pytest.raises(ValidationError, match="Invalid number format: None"):
        InputValidator.validate_number(None, config)

def test_validate_number_non_numeric_type():
    '''Test to validate non numeric number type'''
    with pytest.raises(ValidationError, match="Invalid number format: "):
        InputValidator.validate_number([], config)
