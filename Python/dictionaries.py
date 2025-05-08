"""this program is to help create a dictionary of words and their meanings."""
# #creating a dictionary
dictionary = {
    "apple" : "A fruit that is typically red, green, or yellow.",
    "banana" : "A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.",
    "cherry" : "A small round fruit that is typically red or black and has a pit in the center.",
}
#accessing dictionary values
#print("Welcome to the dictionary program!")
#print(dictionary["apple"])

#accesing a value using a key and the get method
#print(dictionary.get("banana"))

#adding a new key-value pair to the dictionary with the get method
#print(dictionary.get("grape", "A small round fruit that is typically purple or green."))

#adding a new key-value pair to the dictionary
dictionary["pineaple"] = "A tropical fruit with a spiky exterior and sweet, juicy interior."
#print(dictionary)

#creating a dictionary containing another dictionary
dictionary2 = {
    "fruits" : {
        "apple" : "A fruit that is typically red, green, or yellow.",
        "banana" : "A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.",
        "cherry" : "A small round fruit that is typically red or black and has a pit in the center.",
    },
    "dairy" : {
        "milk" : "A white liquid produced by mammals that is often consumed as a beverage or used in cooking.",
        "cheese" : "A dairy product made from curdled milk that is often used in cooking or eaten as a snack.",
        "yogurt" : "A dairy product made by fermenting milk with bacteria, often eaten as a snack or used in cooking.",
    },

    "vegetables" : {
        "carrot" : "A long orange vegetable that is typically eaten raw or cooked.",
        "broccoli" : "A green vegetable that resembles a small tree and is often eaten steamed or stir-fried.",
        "spinach" : "A leafy green vegetable that is often used in salads or cooked dishes.",
    }   
}

#print(dictionary2)

#accessing a value in the nested dictionary
#print(dictionary2["fruits"]["apple"])
#print(dictionary2.get("fruits"))

#adding a new key-value pair to the nested dictionary
dictionary2["fats"] = {
    "butter" : "A dairy product made by churning cream, often used in cooking or as a spread.",
    "olive oil" : "A liquid fat obtained from olives, often used in cooking or as a salad dressing.",
    "avocado" : "A green fruit with a creamy texture that is often used in salads or spreads.",
}
#print(dictionary2)

#print(dictionary2.keys())

#print(dictionary2.values())
#print(dictionary2.items())

for x,obj in dictionary2.items():
    print(x, ":", obj)
    for y, obj2 in obj.items():
        print(y, ":", obj2)
       