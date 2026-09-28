def calculate_age_next_year(current_age):
    return current_age + 1

name = input("Enter your name: ")
current_age = int(input("Enter your current age: "))

next_year_age = calculate_age_next_year(current_age)
print(f"Hello {name}, next year you will be {next_year_age} years old.")