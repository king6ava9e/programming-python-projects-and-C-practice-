"""This is my first python exercise
that I am embarking on after relearning some
basic concepts
AUTHOR = Acheampong Kingsley
Date = 8th January 2025"""

"""Problem statement
THE PRICE OF A HOUSE IS $1M.
IF A BUYER HAS GOOD CREDIT, 
THEY NEED TO PUT DOWN 10% 
OTHERWISE, THEY NEED TO PUT 
DOWN 20%, WRITE DOWN A PROGRAM WITH THE FOLLOWING RULES
AND DISPLAY THE DOWN PAYMENT REQUIRED FOR THE BUYER WITH GOOD CREDITS
PRINT DOWN THE DOWN PAYMENT"""

def main():
    house_price = 1000000
    has_good_price = False

    if has_good_price:
        down_payment= (0.2)*house_price
    else:
        down_payment = (0.1)*house_price
        print (f"the buyer got a good price and his down payment is ${down_payment:.2f}")


main()