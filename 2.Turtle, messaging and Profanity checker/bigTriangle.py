""" A program that draws a big 5 layered triangle with red background """

import turtle

def draw_recursion(turtle,edge_length,remaining_recursions):
    # draw one recursion of sierpinski's triangle if remaining_recursions > 0:
    if remaining_recursions > 0:
        turtle.left(120)
        for edge_counter in range(0, 3):
            turtle.forward(edge_length/2)
            draw_recursion(turtle,edge_length/2, remaining_recursions - 1)
            turtle.forward(edge_length/2)
            if edge_counter < 2:
                turtle.right(120)
            else:
                turtle.left(120)


def draw_sierpinskis_triangle(iterations):
    # setup window and initial position:
    edge_length = 400
    start_position_y = -160

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(5)
    brad.penup()
    brad.right(90)
    brad.setposition(0, start_position_y)
    brad.left(90)
    brad.pendown()

    #draw recursive part of sierpinski's triangle:
    draw_recursion(brad, edge_length/2, iterations)

    #draw border:
    for i in range(0, 9):
        if i % 3 == 1:
            brad.left(120)
        else:
            brad.forward(edge_length/2)
    window.exitonclick()

draw_sierpinskis_triangle(5)
