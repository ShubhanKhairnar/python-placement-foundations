#Power function
def calculate_power(number, power):
    return number ** power

# Get user input
number = float(input("Enter a no:  "))
power = float(input("Enter the power:  "))

# Calculate the power
result = calculate_power(number, power) 
print(f"{number} raised to the power of {power} is: {result}")


#Kilometers to Miles Converter
def kilometers_to_miles(Kilometers):
    return Kilometers * 0.621371

# Get user input
Kilometers = float(input("Enter distance in kilometers: "))
# Convert to miles
miles = kilometers_to_miles(Kilometers)
print(f"{Kilometers} kilometers is equal to {miles:.2f} miles.")



#Bill per person Calculator
def bill_per_person(Total_bill, number_of_people, tip_percentage):
    tip_amount = Total_bill * (tip_percentage/100)
    total_amount = Total_bill + tip_amount
    return total_amount / number_of_people

# Get user input
Total_bill = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the bill per person
bill_per_Person = bill_per_person(Total_bill, number_of_people, tip_percentage)
print(f"Each person owes: ${bill_per_Person:.2f}")
