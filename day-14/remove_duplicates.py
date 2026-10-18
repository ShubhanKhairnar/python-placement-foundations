numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Your numbers:", numbers)

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print (unique_numbers)

