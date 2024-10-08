# main.py

from app.calculator import Calculator  # Adjust the import path as necessary

def main():
    calc = Calculator.create()
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
                if operation == 'add':
                    result = calc.add(a, b)
                elif operation == 'subtract':
                    result = calc.subtract(a, b)
                elif operation == 'multiply':
                    result = calc.multiply(a, b)
                elif operation == 'divide':
                    try:
                        result = calc.divide(a, b)
                    except ZeroDivisionError:
                        print("Error: Division by zero.")
                        continue
                else:
                    print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
                    continue
                print("Result:", result)
            except ValueError:
                print("Invalid numbers. Please enter valid numeric values.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()