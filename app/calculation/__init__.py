from abc import ABC, abstractmethod

# The Calculation class is now an abstract base class (ABC).
# An abstract class cannot be instantiated directly and is meant to be inherited by subclasses.
# It defines a common interface (abstract methods) that subclasses must implement.
class Calculation(ABC):

    # Class method that acts like a factory to create instances of the class.
    # It can be inherited by subclasses, and in this case, it ensures that the method 
    # is available to any class inheriting from Calculation.
    @classmethod
    def create(cls, a, b):
        return cls(a, b)

    # An abstract method that must be implemented by any subclass.
    # This ensures that every subclass provides its own version of this method.
    @abstractmethod
    def compute(self):
        pass  # No implementation here, subclasses will provide it.


# This class represents a specific type of calculation: Addition.
# It inherits from the Calculation class and must implement the abstract method 'compute'.
class Addition(Calculation):

    # The constructor (initializer) method initializes the object with 'a' and 'b'.
    def __init__(self, a, b) -> None:
        self.a = a  # Store 'a' as an instance variable
        self.b = b  # Store 'b' as an instance variable

    # Implementation of the abstract 'compute' method.
    # This method adds 'a' and 'b' together and returns the result.
    def compute(self):
        return self.a + self.b