from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.speed("fastest")
        if self.ycor() > 300:
            self.forward(0)
        elif self.ycor() < -300:
            self.backward(0)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(30)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(30)
