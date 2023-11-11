# Bryan Ulloa
# 11/09/2023

# writing a function areaOfCircle(r) which returns the area of a circle of radius r.

import math

def area_of_circle(r):
    try:
        return math.pi * float(r)**2
    except ValueError:
        return " Sorry, Please enter a valid number for the radius."


radius = input("Please enter the radius of the circle: ")
result = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {result}")
