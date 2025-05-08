#prompts for questions
price_of_child_meal = float(input("What is the price of a child's meal? "))
price_of_adult_meal = float(input("What is the price of adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
print()
#calculation of subtotal and display
subtotal = (price_of_child_meal * number_children) + (price_of_adult_meal*number_adults)
#diplay
print(f"Subtotal: ${subtotal}")
print()
#salestax calculations
salestax = float(input("What is the sales tax rate? "))
#salestax calculations
Salestax_calculated = (subtotal) * (salestax/100)
#total_calculation
TOtal = (Salestax_calculated) + (subtotal)
print(f"Salestax : ${Salestax_calculated}")
print(f"Total : ${TOtal}")
print()
#computation of Amount to be payed and exchange
payment_amount = float(input("What is the payment amount? "))
#computation of change
change = (payment_amount) - (TOtal)
print(f"Change : ${change:2f}")