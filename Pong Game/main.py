from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game!")
screen.tracer(0)

r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

ball = Ball()

scoreboard = Scoreboard()

# Movement of both the paddles
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement_of_ball()

    # Detect collision with paddles:
    if ball.xcor() > 330 and ball.distance(r_paddle) < 60:
        ball.paddle_bounce()

    elif ball.xcor() < -330 and ball.distance(l_paddle) < 60:
        ball.paddle_bounce()

screen.exitonclick()
