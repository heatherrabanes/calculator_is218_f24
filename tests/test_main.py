'''My Calculator Test'''
import pytest
from app.main import addition, subtraction, multiplication, division

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''Multiplication function'''
    assert multiplication(1,2) == 2

def test_positive_division():
    '''Positive Division test'''
    assert division(1,1) == 1

def test_negative_division():
    '''Negative Division test'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
