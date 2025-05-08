#this is to generate random values for a two possible dice
import random

dice = [1, 2, 3, 4, 5, 6]
#randomly select a value from the dice list
value = random.choice(dice)
value2 = random.choice(dice)
print(f"{value}, {value2}")




