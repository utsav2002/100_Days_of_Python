from turtle import Turtle
from player import Player

player = Player()

FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.level = 1
        self.penup()
        self.update_scoreboard()

    def increase_level(self):
        self.level = self.level + 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!", align="left", font=FONT)
