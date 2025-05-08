#Prompts for the integers
first_integer = input("What is the first integer?  ")
second_integer = input("What is the second integer? ")
#If conditioning 1
if first_integer > second_integer:
    print("The first number is greater")
else:
    print("The first number is not greater")
#If conditioning 2
if first_integer == second_integer:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
#If conditioning 3
if second_integer > first_integer:
    print("The second number is greater")
else:
    print("The second number is not greater")
print()
#Comparing strings practice(Prompt for favorite animal)
animal = input("What is your favorite animal? ")
FavoriteAnimal = ("Vixen.lower()")
#Conditional answering on if statements
if animal == FavoriteAnimal :
    print("That's my favorite animal too! ")
else:
    print("It is not my favorite animal ")


