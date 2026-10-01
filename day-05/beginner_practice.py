#BMI Calculator
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

BMI = weight / (height ** 2)

print(f"Your BMI is {BMI:.2f}")



#Mins to Hs and Mins
total_mins = int(input("Enter total minutes: "))
hours = total_mins // 60
minutes = total_mins % 60

print(f"{total_mins} minutes is equal to {hours} hours and {minutes} minutes.")



#SI Calculator
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_intrest = calculate_simple_interest(principal, rate, time)

print(f"The simple interest is: {simple_intrest:.2f}")


#String Formatting
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
language = input("Enter your favorite programming language: ")

# Convert cases
formatted_first = first_name.title()
formatted_last = last_name.title()
formatted_lang = language.upper()

print(f"Hello {formatted_first} {formatted_last}, your favorite language is {formatted_lang}!")

#Word Length Checker
sentence = input("Enter a sentence: ")

# Calculate length and uppercase string
char_count = len(sentence)
upper_sentence = sentence.upper()

print(f"Original: {sentence}")
print(f"Character Count (including spaces): {char_count}")
print(f"Uppercase: {upper_sentence}")