"""this program picks info from a user, 
that is his telephone number,
and the we will print it backt to him in words"""

phone_number = input("Enter your phone number: ")

#now gona make the dictionar
numbers = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
number_out = " "
for phone_number in phone_number:
    number_out += numbers.get(phone_number) + " "
print(number_out)
