#prompt for a positive number
number = int(input("Please type a positive number."))

while not number >= 0:
    print("Sorry, that is negative, please enter a positive number.")
    number = int(input("Please type a positive number."))

print(f"The number is {number}")