bill=300
tip=0.15
people=4
total=bill + (bill*tip)
per_person = total/people
#Unformatted
print(f" Each person owes: ${per_person}")
#Formatted
print(f" Each person owes: ${per_person:.2f}")
