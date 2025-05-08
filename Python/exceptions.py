while True:
    try:
        age = int(input("Enter your age: "))
        income = 2000
        risk = income / age
        print(f"Your age is {age}.")
        print(f"Your risk is {risk}.")
        break
    except ZeroDivisionError:
            print("Age cannot be zero. Please enter a valid age.")
            continue  # Skip to the next iteration of the loop
        
           
    except ValueError:
        print("Invalid input. Please enter a valid age.")
# This code will keep asking for a valid age until the user provides one.

    
   