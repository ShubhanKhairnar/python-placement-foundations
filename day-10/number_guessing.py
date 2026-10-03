def guess_number(secret):
    guess = int(input("Guess the number: "))
    while guess != secret:
        print("Try again!")
        guess = int(input("Guess the number: "))
    return "Congratulations! You guessed the number."

secret = 7
result = guess_number(secret)
print(result)


