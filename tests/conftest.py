# Fixture to create a Calculator instance
import pytest

from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator.create()