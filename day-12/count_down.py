num = int(input("Enter a number whose countdown you want to print: "))
for i in range(num, 0, -1):
    print(i)
print("Countdown finished!")

#same using while loop
number = int(input("Enter number to countdown from: "))
while number > 0:
    print(number)
    number -= 1 # decrease the number by 1 each time
print("Countdown finished!")
