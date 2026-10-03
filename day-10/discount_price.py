def calculate_discount():
    if price >= 5000:
        discount = price * 0.20
    elif price >= 3000:
        discount = price * 0.10
    elif price >= 1000:
        discount = price * 0.05
    else:
        discount = 0
    final_price = price - discount
    return final_price

price = float(input("Enter the purchase amount: "))
final_price = calculate_discount(price)
print(f"Final amount to be paid after discount: ${final_price:.2f}")