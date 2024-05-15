from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.all_blocks = []
        self.starting_snake()
        self.head = self.all_blocks[0]

    def starting_snake(self):
        for position in START_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.all_blocks.append(new_block)

    def reset(self):
        for blocks in self.all_blocks:
            blocks.goto(1000, 1000)

        self.all_blocks.clear()
        self.starting_snake()
        self.head = self.all_blocks[0]

    def extend(self):
        self.add_block(self.all_blocks[-1].position())

    def move(self):
        for block in range(len(self.all_blocks) - 1, 0, -1):
            # Find the co-ordinates of previous block
            new_x = self.all_blocks[block - 1].xcor()
            new_y = self.all_blocks[block - 1].ycor()

            # Ask the next block to go to front block's co-ordinates
            self.all_blocks[block].goto(new_x, new_y)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.all_blocks[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.all_blocks[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.all_blocks[0].setheading(LEFT)
