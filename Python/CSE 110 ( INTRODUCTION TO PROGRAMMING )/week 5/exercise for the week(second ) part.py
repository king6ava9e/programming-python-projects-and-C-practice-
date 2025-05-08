#creating lists
shopping_lists = []
question = ""

#creating loops
while question != "quite":
    question = input("Please enter the items of the shopping list (type : quite to finish)")
    if question != "quite":
        shopping_lists.append(question)

for i in range(len(shopping_lists)):
    needed = shopping_lists[i]
    print(f" {i}.{needed} ")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_lists[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_lists)):
    item = shopping_lists[i]
    print(f"{i}. {item}")
    