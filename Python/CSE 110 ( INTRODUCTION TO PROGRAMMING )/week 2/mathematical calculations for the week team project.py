#prompts

square_length =int(input("What is the lenghth of a side of the square? "))
rectanglular_lenghth = int(input("What is the lenghth of the rectangle? "))
rectangular_width = int(input("What is the width of the rectangle? "))
circular_radius = int(input("What is the radius of the circle? "))

#computationL mathematics
import math
area_of_the_square = (square_length)**2
area_of_rectangle = (rectanglular_lenghth) * (rectangular_width)
area_of_the_circle = (math.pi) * (circular_radius)**2

#display
print(f"What is the length of a side of the square? " + str(square_length))
print(f"The area of the square is : {area_of_the_square}")
print(f"What is the length of the rectangle? {rectanglular_lenghth}")
print(f"What is the width of the rectangle? {rectangular_width}")
print(f"The area of the rectangle is : {area_of_rectangle}")
print(f"What is the radius of the circle ? {circular_radius}")
print(f"The area of the circle is : {area_of_the_circle}")


