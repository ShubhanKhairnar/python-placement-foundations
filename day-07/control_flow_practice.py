#Budget Status Checker
def check_budget_status (budget, total_spent):
    if total_spent > budget:
        over_budget = total_spent - budget
        print(f"You are over budget by ${over_budget:.2f}.")
    elif total_spent == budget:
        print("You are exactly on budget.")
    else:
        under_budget = budget - total_spent
        print(f"You are under budget by ${under_budget:.2f}.")  

budget = float(input("Enter your monthly budget: "))
total_spent = float(input("Enter your total monthly expenses: "))

check_budget_status(budget, total_spent)



