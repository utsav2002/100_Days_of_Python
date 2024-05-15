import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.list_of_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_gen(self):
        random_chance = random.randint(1 ,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")

            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()

            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.list_of_cars.append(new_car)

    def move_car(self):
        for cars in self.list_of_cars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT
