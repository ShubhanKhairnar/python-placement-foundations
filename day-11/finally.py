try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")
