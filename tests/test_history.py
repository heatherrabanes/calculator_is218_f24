'''History tests'''
from unittest.mock import Mock, patch
import pytest
from app.calculation import Calculation
from app.history import LoggingObserver, AutoSaveObserver
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig

# Sample setup for mock calculation
calculation_mock = Mock(spec=Calculation)
calculation_mock.operation = "addition"
calculation_mock.operand1 = 5
calculation_mock.operand2 = 3
calculation_mock.result = 8

# Test cases for LoggingObserver

@patch('logging.info')
def test_logging_observer_logs_calculation(logging_info_mock):
    '''Test for observer calculation logging'''
    observer = LoggingObserver()
    observer.update(calculation_mock)
    logging_info_mock.assert_called_once_with(
        "Calculation performed: addition (5, 3) = 8"
    )

def test_logging_observer_no_calculation():
    '''Test for observer logging no calculation'''
    observer = LoggingObserver()
    with pytest.raises(AttributeError):
        observer.update(None)  # Passing None should raise an exception as there's no calculation

# Test cases for AutoSaveObserver

def test_autosave_observer_triggers_save():
    '''Test for observer autosave trigger'''
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)

    observer.update(calculation_mock)
    calculator_mock.save_history.assert_called_once()

@patch('logging.info')
def test_autosave_observer_logs_autosave(logging_info_mock):
    '''Test for observer autosave logging'''
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)

    observer.update(calculation_mock)
    logging_info_mock.assert_called_once_with("History auto-saved")

def test_autosave_observer_does_not_save_when_disabled():
    '''Test that autosave observer does not trigger save when disabled'''
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = False
    observer = AutoSaveObserver(calculator_mock)

    observer.update(calculation_mock)
    calculator_mock.save_history.assert_not_called()

# Additional negative test cases for AutoSaveObserver

def test_autosave_observer_invalid_calculator():
    '''Test for autosave observer when invalid'''
    with pytest.raises(TypeError):
        AutoSaveObserver(None)  # Passing None should raise a TypeError

def test_autosave_observer_no_calculation():
    '''Test for autosave observer when no calculation'''
    calculator_mock = Mock(spec=Calculator)
    calculator_mock.config = Mock(spec=CalculatorConfig)
    calculator_mock.config.auto_save = True
    observer = AutoSaveObserver(calculator_mock)

    with pytest.raises(AttributeError):
        observer.update(None)  # Passing None should raise an exception
