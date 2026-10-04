n = int(input("Enter a positive number: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print(f"The count of even numbers from 1 to {n} is {count}")

