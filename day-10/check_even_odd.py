def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number to check if it's even or odd: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")