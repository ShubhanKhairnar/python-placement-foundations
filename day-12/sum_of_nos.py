n = int(input("Enter number till which you want to find sum: "))
sum = 0
for i in range (1,n+1):
    sum += i
print(f"The sum of numbers from 1 to {n} is {sum}")
