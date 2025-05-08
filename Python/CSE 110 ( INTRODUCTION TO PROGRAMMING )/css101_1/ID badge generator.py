print("please enter the following details")
#this line leaves a blank space
print()


first_name =input("first name")
last_name = input("last name")
email = input("email")
phone = input("phone number")
job_title = input("job title")
id_number = input("id number")
hair_colour = input("hair")
eye_colour = input("eye")
month_started = input("month")
training = input("training")
response_start = 10


#goimg to use a \n to make a seperation
print("\n the ID  card is :")
print("---------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair :{hair_colour.capitalize():<{response_start}}  Eye:{eye_colour.capitalize():<{response_start}}")
print(f"Month :{month_started.capitalize():<{response_start}}  Training:{training.capitalize():<{response_start}}")

print("-----------------------------------")