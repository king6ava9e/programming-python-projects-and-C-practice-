
#string Methods(LEN)
print("hello world!")
course = "Acheampong Kingsley"

count = len(course)
print(count)

#using the UPPER = This will orint all the data into capital letters
print(course.upper())
print(course)
#notice how the second line is different from the .upper

#Using the LOWER
print(course.lower())
print(course)
#Notice how the second line is different just like the first one too.

#using the FIND = what this does is that is 
#tries to look for the first occurence of the character
#that you will pass into the parenthenses and it will give out its index
print(course.find("m"))

#USING THE REPLACE
print(course.replace("Kingsley", "Akwasi"))
#NB: THIS REPLACE JUST LIKE THE FIND , THEY ARE CASE SENSITIVE

#CHECK THIS OUT
#A BOOLEAN CAN BE CREATED WITHOUT FIST SETTING THE VALUE EVEN TO TRUE OR FALSE
#EXAMPLE IS THE CODE BELOW
print("Kingsley" in course)
#always keep in mind that is case sensitive



#PYTHON ARITHEMETIC CALCULATIONS
#WE HAVE THE ADDITON 
#MULTIPLICATION
#SUBTRACTION
#DIVISION
#WE HAVE THE MODULUS (%) WHICH RETURNS THE REMAINDER OF A DIVISION
print(10%4)
#we also hav the exponential (**)= this gives the exponent of a number
print(23**3)
#check this out
x = 4
x+= 5
print(x)
#this will give 9 because 5 is added to the x
# however check this out 
x= 5
x=+ 3
print (x)
#this gives out three because the new value of x becomes three

#ALWAYS KEEP IN MIND MATHEMATIC PRECEDENCE(BODMAS),  THIS IS USED
#a lot in python and other mathematical operations

#MATHS FUNCTIONS
x = 2.907
round(x)
"""what the rouond will do is that it will round the 
text to its nearest whole number"""
#we also have the abs whic will return a positive number
#eg
x = (-33.44)
print(abs(x))
"""Keep in mind that whenever you wanna work with maths calculations, use the import math on the top of you code
"""

# IF STATEMENTS
"""This helps us to write codes base on certain conditions"""
#example
is_hot = False
if  is_hot:
    print("Its a hot day")

elif is_hot:
    print("What then is it?")

else:
    print("is not hot")






   
   
