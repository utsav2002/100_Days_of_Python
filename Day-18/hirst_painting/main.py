import turtle

import colorgram
from turtle import Turtle,  Screen
import random

timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()


# Initial position
timmy.penup()
timmy.backward(230)
timmy.right(90)
timmy.forward(250)
timmy.left(90)


no_of_dots = 100

# Find the best colours and make a list
colors = colorgram.extract('image.jpg', 50)
color_list = []

for items in colors:
    r = items.rgb.r
    g = items.rgb.g
    b = items.rgb.b
    each_color = (r, g, b)

    color_list.append(each_color)

# Create the chart
for _ in range(int(no_of_dots/10)):
    for n in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)

screen.exitonclick()