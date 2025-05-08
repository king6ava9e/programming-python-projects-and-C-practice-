people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

main_parts = []
last_two = []
for names in people:
    print(names)

index = 0
while index < len(people):
    full_string = people[index]
    main_part = full_string[:-2]
    last_twos = full_string[-2:]

    main_parts.append(main_part)
    last_two.append(last_twos)

    index +=1

    #display
print(f"main parts; {main_parts}")    
print(f"last two : {last_two}")

#displaying the max and min
youngest_age = min(last_two)
print(f"The youngest is : {youngest_age} ")

#finding the corresponding digits
young_index = last_two.index(youngest_age)

#finding the main parts
young_person = main_parts[young_index]

print(f"The youngest person is : {young_person} and he is : {youngest_age}")