""" A program that draws a small blue flower using function. """

import turtle

def draw_diamond(some_turtle):
    some_turtle.left(30)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(120)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(150)

def draw_art():
    # Instantiate a Screen object, window. Then customize window.
    window = turtle.Screen()
    window.bgcolor("white")     # set background color

    # Instantiate a Turtle object, brad. Then customize brad.
    brad = turtle.Turtle()
    brad.shape("turtle")      # see Turtle doc
    brad.color("blue")      # see Turtle doc
    brad.speed(0)             # 1 (slowest) to 10 (fastest). 0 means no animation.

    # Draw a circle with 36 diamonds. We rotate each diamond by 10 degrees at a time.
    for i in range (0, 36):
        draw_diamond(brad)
        brad.right(10)

    # Draw a between middle of circle and the floor
    brad.right(90)
    brad.forward(200)

    # How to exit?
    window.exitonclick()      # click on the window to exit


# Invoke the procedure!
draw_art()
