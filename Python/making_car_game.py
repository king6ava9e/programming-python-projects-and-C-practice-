#This is to make a car game where the user
#is going to choose from options and then 
#see the resulting commands.

def main():
    pass
"""This is going to ask the user to type and choose from options"""
print ("Welcome to the car game!")
print ("type help to see the commands")
help = input("type help to see the commands: ").lower()
if help == "help":
    print("You can choose from the following commands:")
    print("1. start - to start the car")
    print("2. stop - to stop the car")
    print("3. quit - to exit the game")

choice = input("Enter your choice: ").lower()
if choice == "start":
    print("Car started...")
elif choice == "stop":
    print("Car stopped.")
elif choice == "quit":
    print("Game exited.")
else:
    print("Invalid command. Please try again.")


main()   