# 'a' and 'b' are PARAMETERS
def add_numbers(a, b):
    result = a + b
    return result  # RETURN VALUE

# 5 and 10 are ARGUMENTS
sum = add_numbers(5, 10)

# PRINT THE RESULT TO THE TERMINAL
print(sum)

# Remove the hardcoding of the numbers and instead get them from the user
def add_numbers(a,b):
    result=a+b
    return result

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = add_numbers(num1,num2)

print(f"Sum is {sum}")
