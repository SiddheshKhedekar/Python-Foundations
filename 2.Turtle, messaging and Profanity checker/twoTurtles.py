""" The program that allows user to make two separate turtles draw at the same time. """

import turtle

background = turtle.Screen()

meow=turtle.Turtle()
meow.shape("turtle")
meow.color("red")

woof = turtle.Turtle()
woof.shape("turtle")
woof.color("blue")

meow.speed(1)
meow.right(90)
meow.forward(200)
woof.speed(1)
woof.forward(100)
woof.left(90)

meow.right(90)
meow.forward(200)
woof.forward(100)
woof.left(90)

meow.right(90)
meow.forward(200)
woof.forward(100)
woof.left(90)

meow.right(90)
meow.forward(200)
meow.right(90)
woof.forward(100)
woof.left(90)

background.exitonclick()
