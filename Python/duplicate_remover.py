"""This program is designed to remove duplicate elements from a list.
numbe"""
#list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,   2, 3, 4, 5, 6, 7, 8, 9, 10]
uniques_numbers = []

for number in numbers:
    if number not in uniques_numbers:
        uniques_numbers.append(number)
 
print(uniques_numbers)   
              