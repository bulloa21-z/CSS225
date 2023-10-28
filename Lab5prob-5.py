import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Invisibility Cloak")

# Create a turtle object for the triangle
InvisibilityCloak = turtle.Turtle()
InvisibilityCloak .speed(1)  # Set drawing speed (1 is slow)

# Function to draw a triangle with a colorful border
def draw_colorful_triangle(size, color):
    InvisibilityCloak.color(color)
    InvisibilityCloak.begin_fill()
    for _ in range(3):
        InvisibilityCloak.forward(size)
        InvisibilityCloak.left(120)
    InvisibilityCloak.end_fill()

# Draw the colorful triangle
draw_colorful_triangle(100, "green")

# Close the window when clicked
screen.exitonclick()
