# Bryan Ulloa
# 10/14/2023

# This code will compute the area of a circle

import math

# The user enters the radius
radius = float(input("Enter the radius of the circle: "))


# Compute the area of the circle
area = math.pi + (radius ** 2)

# User will print the answer
print(f"The area of a circle with radius {radius} is {area: 2.f}")
