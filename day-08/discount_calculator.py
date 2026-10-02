purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 5000:
    discount = purchase_amount * 0.20
elif purchase_amount >= 3000 :
    discount = purchase_amount * 0.10
elif purchase_amount >= 1000 :
    discount = purchase_amount * 0.05
else:
    discount = 0

final_amount = purchase_amount - discount
print(f"Discount: ${discount:.2f} Final amount to be paid: ${final_amount:.2f}")


    