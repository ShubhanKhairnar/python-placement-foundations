#non-reusable variable
birth_year = int (input ("Enter your birth year: "))
current_year = int (input ("Enter current year:"))
print(f"Your age is {current_year - birth_year}!")

#reusable variable
birth_year = int (input ("Enter your birth year: "))
current_year = int (input ("Enter current year:"))
calculated_age = current_year - birth_year
print(f"Your age is {calculated_age}!")