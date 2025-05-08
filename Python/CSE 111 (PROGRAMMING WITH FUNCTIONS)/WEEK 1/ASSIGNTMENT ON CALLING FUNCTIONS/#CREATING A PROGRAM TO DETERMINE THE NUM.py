#CREATING A PROGRAM TO DETERMINE THE NUMBER OF BOXES NEEDED FOR THE ITEMS
#IMPORTING , MATHS
import math
#ASK FOR THE NUMBER OF MANUFACTURED ITEMS
items_manufactured = int(input("what is the number of items manufactured? "))
#ASK FOR THE NUMBER OF ITEMS THE USER WILL NEED PER BOX
items_to_be_packed_per_box = int(input("how many items will you pack per box?"))
#DO THE CALCULATIONS
items_per_box = (items_manufactured/items_to_be_packed_per_box)
items_per_box_correct = math.ceil(items_per_box)
#DISPLAY
print(f"for {items_manufactured}, packing {items_to_be_packed_per_box} in each box, you will need {items_per_box_correct} boxes")