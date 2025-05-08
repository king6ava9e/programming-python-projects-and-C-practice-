def main ():
    # This program converts pounds to kilograms and vice versa.
    weight = float(input("Enter weight: "))
    unit = input("Enter unit (kg or lb): ").strip().lower()

    if unit == "kg":
        converted_weight = weight * 2.20462
        print(f"{weight} kg is equal to {converted_weight:.2f} lb")
    elif unit == "lb":
        converted_weight = weight / 2.20462
        print(f"{weight} lb is equal to {converted_weight:.2f} kg")

main()