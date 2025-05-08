"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

#INPUT THE COMMAND FOR THE AGE
age = int(input("What is your age please?"))
#DO THE CALCULATIONS
difference = (220) - (age)
#DO THE CALCALATIONS FOR THE HIGHEST 
highest_percentage = (85/100)*(difference)
#DO THE CALCULATION FOR THE LOWEST 
lowest_percentage = (65/100)*(difference)
#DISPLAY
print(f"when you exercise to strengthen your heart, you should keep your heart rate between {lowest_percentage} and {highest_percentage} beats per minute.")