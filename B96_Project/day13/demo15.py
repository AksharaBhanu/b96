bill_amount = int(input("Enter the bill amount: "))
if bill_amount >= 6000:
    discount_rate = 0.20  # 20% discount
elif bill_amount >= 4000:
    discount_rate = 0.15  # 15% discount
elif bill_amount >= 2000:
    discount_rate = 0.10  # 10% discount
else:
    discount_rate = 0.0  # No discount

discount_amount = bill_amount * discount_rate
balance_to_pay = bill_amount - discount_amount

print("Discount amount:", discount_amount)
print("Balance to be paid:", balance_to_pay)
