'''Calculation tests'''
from decimal import Decimal
from datetime import datetime
import pytest
from app.calculation import Calculation
from app.exceptions import OperationError

def test_addition():
    '''Test for addition calculation operation'''
    calc = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    assert calc.result == Decimal("5")

def test_subtraction():
    '''Test for subtraction calculation operation'''
    calc = Calculation(operation="Subtraction", operand1=Decimal("5"), operand2=Decimal("3"))
    assert calc.result == Decimal("2")

def test_multiplication():
    '''Test for multiplication calculation operation'''
    calc = Calculation(operation="Multiplication", operand1=Decimal("4"), operand2=Decimal("2"))
    assert calc.result == Decimal("8")

def test_division():
    '''Test for division calculation operation'''
    calc = Calculation(operation="Division", operand1=Decimal("8"), operand2=Decimal("2"))
    assert calc.result == Decimal("4")

def test_division_by_zero():
    '''Test for division by zero'''
    with pytest.raises(OperationError, match="Division by zero is not allowed"):
        Calculation(operation="Division", operand1=Decimal("8"), operand2=Decimal("0"))

def test_power():
    '''Test for power calculation operation'''
    calc = Calculation(operation="Power", operand1=Decimal("2"), operand2=Decimal("3"))
    assert calc.result == Decimal("8")

def test_negative_power():
    '''Test for negative power calculation operation'''
    with pytest.raises(OperationError, match="Negative exponents are not supported"):
        Calculation(operation="Power", operand1=Decimal("2"), operand2=Decimal("-3"))

def test_root():
    '''Test for root calculation operation'''
    calc = Calculation(operation="Root", operand1=Decimal("16"), operand2=Decimal("2"))
    assert calc.result == Decimal("4")

def test_invalid_root():
    '''Test for invalid root'''
    with pytest.raises(OperationError, match="Cannot calculate root of negative number"):
        Calculation(operation="Root", operand1=Decimal("-16"), operand2=Decimal("2"))

def test_unknown_operation():
    '''Test for unknown calculation operation'''
    with pytest.raises(OperationError, match="Unknown operation"):
        Calculation(operation="Unknown", operand1=Decimal("5"), operand2=Decimal("3"))

def test_to_dict():
    '''Test for recording calculations to history'''
    calc = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    result_dict = calc.to_dict()
    assert result_dict == {
        "operation": "Addition",
        "operand1": "2",
        "operand2": "3",
        "result": "5",
        "timestamp": calc.timestamp.isoformat()
    }

def test_from_dict():
    '''Test for taking calculation from history'''
    data = {
        "operation": "Addition",
        "operand1": "2",
        "operand2": "3",
        "result": "5",
        "timestamp": datetime.now().isoformat()
    }
    calc = Calculation.from_dict(data)
    assert calc.operation == "Addition"
    assert calc.operand1 == Decimal("2")
    assert calc.operand2 == Decimal("3")
    assert calc.result == Decimal("5")

def test_invalid_from_dict():
    '''Test for invalid calculation from history'''
    data = {
        "operation": "Addition",
        "operand1": "invalid",
        "operand2": "3",
        "result": "5",
        "timestamp": datetime.now().isoformat()
    }
    with pytest.raises(OperationError, match="Invalid calculation data"):
        Calculation.from_dict(data)

def test_format_result():
    '''Test for formatting calculation operation result'''
    calc = Calculation(operation="Division", operand1=Decimal("1"), operand2=Decimal("3"))
    assert calc.format_result(precision=2) == "0.33"
    assert calc.format_result(precision=10) == "0.3333333333"

def test_equality():
    '''Test for calculation operation equality'''
    calc1 = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    calc2 = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    calc3 = Calculation(operation="Subtraction", operand1=Decimal("5"), operand2=Decimal("3"))
    assert calc1 == calc2
    assert calc1 != calc3
