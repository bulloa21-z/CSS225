# Bryan Ulloa
# 11/06/2023

# This program will use a for statement to calculate the factorial of a user input value

import math

n = int(input("Enter a non-negative integer to calculate its factorial: "))

# Calculate factorial using a for loop
factorial = 1
for i in range(1, n + 1):
    factorial *= i
# Calculate the math
math_factorial = math.factorial(n)

print(f"Calculated Factorial: {factorial}")
print(f"Factorial (Using math.factorial): {math_factorial}")
