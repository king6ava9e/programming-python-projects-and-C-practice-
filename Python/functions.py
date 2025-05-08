def greet(name):
    print(f"Hello, {name}!")

def main():
    # This is where you handle input
    user_name = input("Enter your name: ")
    
    # Pass input to a reusable function
    greet(user_name)

# Start the program
main()
