# Version 1 (Variables): Stores calculated results in memory so they can be reused
# later in the code.
# Program 1: Basic Calculator
# 1. Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Perform raw math directly inline
add_res = num1 + num2
sub_res = num1 - num2
mul_res = num1 * num2
div_res = num1 / num2

# 3. Print results using f-strings
print(f"{num1} + {num2} = {add_res}")
print(f"{num1} - {num2} = {sub_res}")
print(f"{num1} * {num2} = {mul_res}")
print(f"{num1} / {num2} = {div_res:.2f}")

# Version 2 (Inline): Calculates values on the fly directly inside the f-string
# without saving them in memory.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\n--- Results ---")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")