try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator! Please enter one of +, -, *, /.")
        result = None

    if result is not None:
        print(f"The result of {num1} {operator} {num2} is {result}")

except ValueError:
    print("Invalid input! Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Calculator finished.")