#This is going to help me how to use class in python
class Trial:
    def __init__(self,name, age, height):
        self.name = name
        self.age = age
        self.height = height
       

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def informations(self):
        info =self.name, self.age, self.height
        
        message = ("This is a class that contains information about a person."
                   "It includes their name, age, and height."
                   "You can create an instance of this class to store and display this information."
                   "You can also add methods to perform operations on the data stored in the class."
                   f"Example: {self.name} is {self.age} years old and {self.height} cm tall.")
        return message
       


t1 = Trial("John", 25, 175)

print(t1.__str__())
print(t1.informations())
# This code defines a class called "Trial" that represents a person with attributes for name, age, and height.

    
        