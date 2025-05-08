# Ask the user for the temperature
temperature = float(input("What is the temperature? "))

# Ask if the temperature is in Fahrenheit or Celsius
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# Convert Celsius to Fahrenheit if needed
if unit == "C":
    temperature = (temperature * 9/5) + 32  # Convert to Fahrenheit

# Loop through wind speeds from 5 to 60 mph (incrementing by 5)
wind_speed = 5
while wind_speed <= 60:
    # Calculate wind chill using the formula
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
    
    # Print the result rounded to 2 decimal places
    print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")
    
    # Increase wind speed by 5 for the next calculation
    wind_speed += 5