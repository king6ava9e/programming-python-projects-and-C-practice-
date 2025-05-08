import random
class Dice:
    def __init__(self, sides=6):
       pass

    def roll(self):
        value1 = random.randint(1, 6)
        value2 = random.randint(1, 6)
        return value1, value2
    
d1 = Dice()
print(d1.roll())
        