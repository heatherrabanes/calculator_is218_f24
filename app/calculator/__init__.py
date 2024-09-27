# Import your operations module functions
from app.operations import addition, subtraction, multiplication, division

class Calculator:

    @staticmethod
    def create():
        return Calculator()

    def add(self, a, b):
        return addition(a, b)

    def subtract(self, a, b):
        return subtraction(a, b)

    def multiply(self, a, b):
        return multiplication(a, b)

    def divide(self, a, b):
        return division(a, b)