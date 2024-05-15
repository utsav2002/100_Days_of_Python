import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.color("red")
        self.speed("fastest")

        self.new_food()

    def new_food(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-280, 270)

        self.goto(random_x, random_y)