#temperatures
fahrenheit = int(input("what is the temperature in farenheit? "))
degree_celsius = (fahrenheit - 32) * (5/9)
degree_celsius_2 = f"{degree_celsius:.1f}"

#display
print("What is the temperature in Fahrenheit? " + str(fahrenheit))
print(f"The temperature in Celsius is {degree_celsius_2} degrees. ")