#prompt for infos
age = int(input("what is your age? "))
carton_egg = int(input("How many carton of eggs do you have? "))
cookies = input("How many cookies do you have? ")
cookies =int(cookies)
number_of_people =int(input("How many people are there? "))

#mathematics operations
birthday =age + 1
total_number_eggs = carton_egg * 12
cookies_each_person_gets = float(cookies / number_of_people)

#display
print("How old are you?" + str(age))
print("On your next birthday," + "you will be" + " " + str(birthday))
print()
print("How many eggs of cartons do you have?"  +  str(carton_egg))
print("You have " +" " + str(total_number_eggs) + " " + "eggs")
print()
print("How many cookies do you have?" + str(cookies))
print("How many people are there?" + str(number_of_people))
print("Each person may have " + str(cookies_each_person_gets))

