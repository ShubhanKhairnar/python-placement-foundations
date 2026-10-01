def calculate_expenses(rent, food, transport, budget):
    total_expenses = rent + food + transport
    remaining_budget = budget - total_expenses

    rent_percentage = (rent / budget) * 100
    food_percentage = (food / budget) * 100
    transport_percentage = (transport / budget) * 100

    return total_expenses, remaining_budget, rent_percentage, food_percentage, transport_percentage

# Get user input
rent = float(input("Enter monthly rent amount: "))
food = float(input("Enter monthly food expenses: "))
transport = float(input("Enter monthly transport expenses: "))
budget = float(input("Enter your monthly budget: "))

# Calculate expenses and percentages    
expenses_calculated = calculate_expenses(rent, food, transport, budget)

# Unpack the returned values
total_expenses, remaining_budget, rent_percentage, food_percentage, transport_percentage = expenses_calculated  

# Print the results
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
print(f"Rent: {rent_percentage:.2f}% of budget")
print(f"Food: {food_percentage:.2f}% of budget")
print(f"Transport: {transport_percentage:.2f}% of budget")
