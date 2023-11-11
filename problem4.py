# Bryan Ulloa
# 11/06/2023

# Print that value as well as the value of math.pi from the math module
import math

def approximate_pi(iterations):
    approximated_pi = 0
    for i in range(iterations):
        approximated_pi += (-1) ** i / (2 * i + 1)
    approximated_pi *= 4
    return approximated_pi

iterations = 1000000

approximated_pi_value = approximate_pi(iterations)
math_pi_value = math.pi

print(f"Approximated Pi: {approximated_pi_value}")
print(f"Math Module Pi: {math_pi_value}")


