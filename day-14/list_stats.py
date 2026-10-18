
numbers = [12, 5, 20, 8]

if len(numbers) == 0:
    print("Empty List.")
else:
    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

        total = total + number

    average = total / len(numbers)

    print("Maximum: ", largest)
    print("Minimum: ", smallest)
    print("Average: ", average)
    

