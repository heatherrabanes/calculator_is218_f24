from app.calculation import Addition, Subtraction, Multiplication, Division
from typing import Dict, Type

# A mapping of operation strings to their corresponding calculation classes
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

def main():
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        command = input(">>> ").strip()
        if command.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
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
        else:
            parts = command.split()
            if len(parts) != 3:
                print("Invalid command format. Type 'help' for instructions.")
                continue
            
            operation, a_str, b_str = parts
            try:
                a = float(a_str)
                b = float(b_str)
                
                # Look up the appropriate calculation class from the operations_map
                if operation not in operations_map:
                    print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
                    continue
                
                # Instantiate the correct Calculation subclass and perform the operation
                calculation = operations_map[operation](a, b)
                result = calculation.compute()
                print("Result:", result)
                
            except ValueError:
                print("Invalid numbers. Please enter valid numeric values.")
            except ZeroDivisionError:
                print("Error: Division by zero.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()