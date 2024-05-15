from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.score = 0
        with open("data.txt", mode= 'r') as read_high_score:
            self.high_score = int(read_high_score.read())
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
