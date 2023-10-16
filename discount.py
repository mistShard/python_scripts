from datetime import datetime

current_date = (datetime.now())
today = current_date.weekday()
subtotal = float(input("Please enter the Subtotal: "))

if subtotal >= 50 and (today == 1 or today == 2):
    discount = .10 * subtotal
    subtotal = subtotal - discount
    sales_tax = .06 * subtotal
    total = subtotal + sales_tax
    print(f"Discount amount: {discount:.2f}")
else:
    sales_tax = .06 * subtotal
    total = subtotal + sales_tax

print(f"""Sales tax amount: {sales_tax:.2f}
Total: {total:.2f}""")

