from turtle import Turtle
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def movement_of_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

        # Detect collision with walls
        if self.ycor() > 280 or self.ycor() < -280:
            self.wall_bounce()

        # Detect ball miss:
        if self.xcor() > 399:
            self.goto(0, 0)
            self.move_speed = 0.1
            time.sleep(0.5)
            scoreboard.l_point()
            self.paddle_bounce()

        elif self.xcor() < -399:
            self.goto(0, 0)
            self.move_speed = 0.1
            time.sleep(0.5)
            scoreboard.r_point()
            self.paddle_bounce()

    def wall_bounce(self):
        self.y_move = self.y_move * -1

    def paddle_bounce(self):
        self.x_move = self.x_move * -1
        self.move_speed = self.move_speed * 0.7