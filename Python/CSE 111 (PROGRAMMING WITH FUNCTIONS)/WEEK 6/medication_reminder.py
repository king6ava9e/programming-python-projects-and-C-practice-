import csv
import os  # THIS WILL HELP ME TO INTERACT WITH MY OPERATING SYSTEM
import time
import datetime

def create_csv_file(filename='medications.csv'):
    """Creates a file called medications.csv
    Adds the header row: Name, Dosage, Time, Date, Notes"""
    if not os.path.exists(filename):
        headers = ['Name', 'Dosage', 'Time', 'Date', 'Notes']
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"CSV file '{filename}' created with headers.")
    else:
        print(f"CSV file '{filename}' already exists.")

def add_medication(filename='medication_data.csv'):
    """Ensures that every time the user enters new information, it is added to the CSV file."""
    name = input("Enter medication name: ")
    dosage = input("Enter dosage: ")
    time = input("Enter time to take the medication (HH:MM AM/PM): ")
    date = input("Enter the date to take the medication (YYYY-MM-DD): ")
    notes = input("Enter any notes (optional): ")

    medication_data = [name, dosage, time, date, notes]

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(medication_data)

    print(f"Medication '{name}' added successfully.")

def view_medications(filename='medication_data.csv'):
    """Displays the list of medications and their details."""
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            print("\nList of Medications:")
            for row in reader:
                print(f"Name: {row[0]}, Dosage: {row[1]}, Time: {row[2]}, Date: {row[3]}, Notes: {row[4]}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

def set_reminder(filename='medication_data.csv'):
    """Sets a reminder for the user on a specific medication."""
    medication_name = input("Enter the medication name for reminder: ")

    found = False
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].lower() == medication_name.lower():
                medication_time = row[2]  # Get the time column for the medication
                found = True
                break

    if not found:
        print(f"Medication '{medication_name}' not found in the records.")
        return

    reminder_time = datetime.datetime.strptime(medication_time, "%I:%M %p").time()
    current_time = datetime.datetime.now().time()

    if reminder_time > current_time:
        print(f"Reminder set for {medication_name} at {medication_time}.")
    else:
        print(f"The time for {medication_name} has already passed today. Please set it for tomorrow.")

    while datetime.datetime.now().time() < reminder_time:
        time.sleep(30)  # Sleep for 30 seconds

    print(f"Reminder: Time to take your medication '{medication_name}'!")

def send_reminder(reminder_time):
    """This function will check the current time and send a reminder when it's time."""
    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
            print("Reminder: It's time to take your medication!")
            break
        time.sleep(60)  # Sleep for 60 seconds before checking again

def main():
    """Main function to run the Medication Reminder System."""
    create_csv_file()  # Ensure the CSV file exists before running the program

    while True:
        print("\n--- Medication Reminder System ---")
        print("1. Add Medication")
        print("2. View Medications")
        print("3. Set Reminder")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_medication()  
        elif choice == '2':
            view_medications()  
        elif choice == '3':
            set_reminder()  
        elif choice == '4':
            print("Exiting Medication Reminder System. Goodbye!")
            break  
        else:
            print("Invalid option, please choose between 1 and 4.")

# Run the main function to start the program
if __name__ == "__main__":
    main()