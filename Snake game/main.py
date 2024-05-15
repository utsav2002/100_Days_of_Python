import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

is_game_on = True

while is_game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # New food after collision
    if snake.head.distance(food) < 20:
        food.new_food()
        scoreboard.add_score()
        snake.extend()

    # Detect collision with wall
    if (snake.head.xcor() > 390) or (snake.head.xcor() < -390) or (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for each_block in snake.all_blocks[1:]:
        if (snake.head.distance(each_block)) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
