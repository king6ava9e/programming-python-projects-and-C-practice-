#ask user for the subtotal
import datetime
subtotal = float(input("what is the subtotal please?"))
current_day = datetime.datetime.today().strftime('%A')

# Default values to prevent undefined variable errors
discount_amount = 0
subtotal_correct = subtotal  # No discount means subtotal stays the same
sales_tax = subtotal_correct * 0.06
amount_due = subtotal_correct + sales_tax

if (current_day == "Tuesday" or current_day == "Wednesday") and subtotal >= 50:
    discount_amount = (subtotal) * 0.10
    subtotal_correct = (subtotal) - (discount_amount)
    sales_tax = (subtotal) * (0.06)
    amount_due = (subtotal_correct) + (sales_tax)

print(f"the subtotal is {subtotal}")
print(f"the discount amount is {discount_amount}")
print(f"the sales tax {sales_tax}")
print(f"the total amount due {amount_due}")



#do the calculations for discount, subtotal, tax and all
#print the sales tax , discount, and total amount due