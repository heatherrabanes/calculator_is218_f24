from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division, Number

# The Calculation class is now an abstract base class (ABC).
# An abstract class cannot be instantiated directly and is meant to be inherited by subclasses.
class Calculation(ABC):

    # The constructor (initializer) method initializes the object with 'a' and 'b'.
    def __init__(self, a: Number, b: Number) -> None:
        # Type checking to ensure a and b are either int or float
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be numbers (int or float)")
        self.a = a
        self.b = b

    # Class method that acts like a factory to create instances of the class.
    # It can be inherited by subclasses, and in this case, it ensures that the method 
    # is available to any class inheriting from Calculation.
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Calculation':
        return cls(a, b)

    # An abstract method that must be implemented by any subclass.
    # This ensures that every subclass provides its own version of this method.
    @abstractmethod
    def compute(self) -> Number:
        pass  # No implementation here, subclasses will provide it.


# This class represents a specific type of calculation: Addition.
# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Addition(Calculation):

    # Implementation of the abstract 'compute' method.
    # This method adds 'a' and 'b' together and returns the result.
    def compute(self) -> Number:
        return addition(self.a, self.b)


# This class represents a specific type of calculation: Subtraction.
class Subtraction(Calculation):

    # Implementation of the abstract 'compute' method.
    # This method subtracts 'b' from 'a' and returns the result.
    def compute(self) -> Number:
        return subtraction(self.a, self.b)


# This class represents a specific type of calculation: Multiplication.
class Multiplication(Calculation):

    # Implementation of the abstract 'compute' method.
    # This method multiplies 'a' and 'b' together and returns the result.
    def compute(self) -> Number:
        return multiplication(self.a, self.b)


# This class represents a specific type of calculation: Division.
class Division(Calculation):

    # Implementation of the abstract 'compute' method.
    # This method divides 'a' by 'b' and returns the result.
    def compute(self) -> Number:
        if self.b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return division(self.a, self.b)