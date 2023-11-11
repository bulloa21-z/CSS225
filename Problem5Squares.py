# Bryan Ulloa
# 11/09/23

# Producing an image below

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare(alex,100)
wn.exitonclick()