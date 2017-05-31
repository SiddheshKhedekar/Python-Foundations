""" The program that allows user to make a small circle out of small squares using a function. """

import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)        # move forward 100 units
        some_turtle.right(90)           # turn right 90 degrees

def draw_art():
    # Instantiate a Screen object, window. Then customize window.
    window = turtle.Screen()
    window.bgcolor("red")     # set background color

    # Instantiate a Turtle object, brad. Then customize brad.
    brad = turtle.Turtle()
    brad.shape("turtle")      # see Turtle doc
    brad.color("yellow")      # see Turtle doc
    brad.speed(6)             # 1 (slowest) to 10 (fastest). 0 means no animation.

    # Draw a circle with 36 squares. We rotate each square by 10 degrees at a time.
    for i in range (0, 36):
        draw_square(brad)
        brad.right(10)

    # How to exit?
    window.exitonclick()      # click on the window to exit

# Invoke the procedure!
draw_art()
