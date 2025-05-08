#creating lists
names = ["Johm", "King"]
question = ""
#creatin loops
while question != "end":
    question =input("what is your friends name? ")
    if question != "end":
        names.append(question)

print("The names are: ")
for i in names:
    print(f"{i}")

   
