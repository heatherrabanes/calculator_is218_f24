# Importing calculation classes (Addition, Subtraction, Multiplication, Division)
# These classes are assumed to be defined in the 'app.calculation' module. Each class likely
# represents a distinct arithmetic operation and implements a `compute` method to perform that operation.
from app.calculation import Addition, Subtraction, Multiplication, Division

# Importing necessary typing utilities.
# `Dict` and `Type` are used here for type hinting to indicate that the dictionary `operations_map`
# will have keys of type `str` and values that are calculation class types.
from typing import Dict, Type

# Mapping operations (as strings) to their respective calculation classes.
# This map follows the Strategy Design Pattern, where each operation is encapsulated
# within its own class. This pattern helps organize the logic by separating each
# operation into its own class, adhering to the "Single Responsibility Principle" of OOP.
# - Key: String representing the operation (e.g., 'add').
# - Value: Corresponding class (e.g., Addition class) that performs the operation.
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

# Main function where the REPL (Read-Eval-Print Loop) is implemented.
# REPL allows the program to interact with users in a loop: reading inputs, processing them, and showing outputs.
def main():
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    # Infinite loop that keeps the REPL running until the user types 'exit' or 'quit'.
    while True:
        # Prompt the user for input and strip any extra whitespace.
        command = input(">>> ").strip()

        # Check if the user wants to exit the REPL.
        # `in` is used to check if the command is any variation of 'exit' or 'quit'.
        if command.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break  # Exit the loop and thus end the program.

        # If the user asks for help, print a list of available commands.
        elif command.lower() == 'help':
            print("""
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  exit           - Exits the REPL
  help           - Shows this help message
""")

        # For all other inputs, attempt to process them as a calculation command.
        else:
            # Split the user's command into parts (should be 3 parts: operation, a, and b).
            parts = command.split()

            # If the input doesn't have exactly 3 parts (operation, number1, number2), show an error message.
            # LBYL (Look Before You Leap) approach is used here to ensure the input is well-formed before processing it.
            if len(parts) != 3:
                print("Invalid command format. Type 'help' for instructions.")
                continue  # Skip the rest of the loop and prompt for the next command.

            # Unpack the split command into the operation and the two arguments (a_str and b_str).
            operation, a_str, b_str = parts

            try:
                # Try to convert the input strings (a_str, b_str) to floats.
                # If this fails, a ValueError will be raised, and the code will jump to the except block.
                a = float(a_str)
                b = float(b_str)

                # Check if the operation is in the `operations_map`. This ensures we handle only valid operations.
                # This uses the LBYL (Look Before You Leap) approach by checking if the operation exists before proceeding.
                if operation not in operations_map:
                    print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
                    continue  # Skip the rest of the loop and ask for the next command.

                # Instantiate the appropriate calculation class from the `operations_map`.
                # This leverages the Strategy Pattern to dynamically decide which calculation to perform
                # based on the user's input (e.g., Addition, Subtraction, etc.).
                calculation = operations_map[operation].create(a, b)

                # Call the `compute` method to perform the calculation and store the result.
                result = calculation.compute()

                # Print the result of the calculation.
                print("Result:", result)

            # Handle the case where the input values cannot be converted to floats.
            except ValueError:
                print("Invalid numbers. Please enter valid numeric values.")

            # Handle division by zero specifically since it's a common error.
            # This is an example of EAFP (Easier to Ask for Forgiveness than Permission), where
            # we perform the operation and handle specific exceptions afterward.
            except ZeroDivisionError:
                print("Error: Division by zero.")

            # Catch any other unforeseen exceptions that may occur and display a generic error message.
            except Exception as e:
                print(f"An error occurred: {e}")

# Check if this script is being run as the main program (and not imported as a module).
if __name__ == '__main__':
    main()