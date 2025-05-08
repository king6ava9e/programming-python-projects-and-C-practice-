#creating the menu list
choice = ""
cart = []
prices = []

while True:
    print("....\n The options in the menu cart include:....")
    print("1. Add a new Item")
    print("2. Display the contents of the shopping cart ")
    print("3. Remove the item")
    print("4. Compute the total")
    print("5. Quit")

    #choice of user
    choice = input("Please choose an option (1-5)")

    if choice == "1":
        item = input("Please Enter the name of the item")
        price = float(input(f"What is the price of '{item}'? "))
        cart.append(item)
        prices.append(price)
        print(f"{item} has been added to the cart.")

    elif choice == "2":
        if len(cart) > 0 :
            print(f"  The contents of your shopping cart are: {cart} ")    
            for i in range(len(cart)):
                print(f"{i + 1} . {cart[i]} - - ${prices[i]:.2f}")
        else:
            print("Your shopping cart is empty")

    elif choice == "3":
        if len(cart) > 0 :
            print("The content of your shopping card are :")
            for i in range(len(cart)):
                print(f"{i + 1} . {cart[i]} - - ${prices[i]:.2f}")

                print()

            try:
                remove_index = int(input("Enter the number of the item to be removed: "))
                if 1 <= remove_index < len(cart):
                    remove_item = cart.pop(remove_index)
                    removed_price = prices.pop(remove_index)
                    print(f"'{remove_item}' with price ${removed_price} has been removed from the cart.")
                else:
                    print("Sorry, that's not a valid item number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Your shopping cart is empty.")

    elif choice == "4":
         if len(cart) > 0:
            total = sum(prices)  # Add up all the prices in the list
            print(f"The total price of the items in your cart is: ${total:.2f}")
         else:
            print("Your shopping cart is empty.")  

    elif choice == "5":
           print("Thank you for using the shopping cart. Goodbye!")
           break  # Exit the loop and end the program
    

    else:
        print("Invalid option. Please try again.")  

