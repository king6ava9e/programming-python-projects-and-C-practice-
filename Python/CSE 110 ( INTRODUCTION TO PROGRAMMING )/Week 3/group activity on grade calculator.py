#prompt for grade percentage
grade_percentage = float(input("What is your grade percentage? "))
#if statements
print()
if grade_percentage >= 90:
    print("A")
elif grade_percentage >= 80:
    print("B")
elif grade_percentage >= 70:
    print("C")
elif grade_percentage >= 60:
    print("D")
elif grade_percentage < 60:
    print("F")
#If user passd the exams
if grade_percentage >= 90:
    print("Congratulations, you passed the exams")
elif grade_percentage >= 80:
    print("Congratulations, you passed the exmas.")
elif grade_percentage >= 70:
    print("Congratulations, You passed the exams")
elif grade_percentage <= 69:
    print("You failed the test, You could do better next time.")