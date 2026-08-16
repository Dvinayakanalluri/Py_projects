
unit = input("Enter the unit to convert from (C for Celsius, F for Fahrenheit): ").strip().upper()
temp = float(input("Enter the temperature value to convert: "))

if unit == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
elif unit == "F":
    converted_temp = round((temp - 32) * 5/9, 1)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print(f"{unit} is an invalid unit. Please enter either 'C' or 'F'.")