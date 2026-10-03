# countdown program using while loop

number = int(input("Enter number to countdown from: "))

while number > 0:
    print(number)
    number -= 1 # decrease the number by 1 each time
print("Countdown finished!")