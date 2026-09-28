bill_amt= float(input("Enter bill amount: "))
tip_percent= float(input("Enter tip percentage: "))

tip_amt= bill_amt * (tip_percent/100)
people= int(input("Enter number of people: "))

total_amt= bill_amt + tip_amt
per_person= total_amt/people 

print(f" Total bill amt: ${total_amt:.2f} and tip amt: ${tip_amt:.2f} and each person owes: ${per_person:.2f}")
