# Simple Calculator with Python

def calculator():
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
