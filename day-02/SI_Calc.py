# 1. Get loan/investment inputs
principal = float(input("Enter principal amount (₹): "))
rate = float(input("Enter annual interest rate (%): "))
time_years = float(input("Enter time period (in years): "))

# 2. Intermediate variables: interest and total calculations
interest_earned = (principal * rate * time_years) / 100
total_payable = principal + interest_earned

# 3. Display formatted summary
print(f"Interest Earned: ₹{interest_earned:.2f}")
print(f"Total Amount Payable: ₹{total_payable:.2f}")