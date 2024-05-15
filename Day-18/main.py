import random
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.shape("arrow")
# timmy.pensize(10)
timmy.speed("fastest")

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# angle_list = (90, 180, 270, 360)

#
# def shape(number_of_sides):
#     timmy.color(random.choice(color_list))
#     angle = 360 / number_of_sides
#     for n in range(number_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_sides_n in range(3, 11):
#     shape(shape_sides_n)
#
#
# for n in range(200):
#     timmy.color(random_color())
#     timmy.forward(50)
#     timmy.right(random.choice(angle_list))

for n in range(74):
    timmy.color(random_color())
    timmy.circle(150, steps=50)
    timmy.left(5)

screen.exitonclick()