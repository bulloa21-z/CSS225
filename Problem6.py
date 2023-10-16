# Bryan Ulloa
# 10/12/23

# This program converts degrees Fahrenheit to degree Celsius

# Enter the temperature in degrees Fahrenheit
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))

# Converting Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Print the answer
print(f"{fahrenheit} Fahrenheit is equal to {celsius: 2f} Celsius")