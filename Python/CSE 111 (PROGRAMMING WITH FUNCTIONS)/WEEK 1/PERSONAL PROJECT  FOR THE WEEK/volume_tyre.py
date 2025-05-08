from datetime import datetime

# Get user input for tire dimensions
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the approximate volume of the tire
volume = (3.14159 * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Round the volume to two decimal places
volume = round(volume, 2)

# Display the calculated volume
print(f"The approximate volume is {volume} liters")

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Open the file volumes.txt and append the data
with open("volumes.txt", "at") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

# Ask the user if they want to buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy_tires == "yes":
    phone_number = input("Enter your phone number: ").strip()
    with open("volumes.txt", "at") as file:
        file.write(f"Phone: {phone_number}\n")
    print("Your information has been saved. A representative will contact you.")

print("Thank you for using the tire volume calculator!")