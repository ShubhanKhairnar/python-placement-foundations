try:
    age = int (input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
    