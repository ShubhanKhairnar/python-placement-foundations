def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
n = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(n)
print(f"The factorial of {n} is {result}.")