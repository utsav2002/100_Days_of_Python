import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.car_gen()
    car_manager.move_car()

    # Player crossing the finish line
    if player.hit_finish():
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Detect collision of Player and Car
    for car in car_manager.list_of_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.update()
screen.onkey(fun=player.move_player, key="Up")
