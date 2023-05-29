from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("white")
        self.shape("turtle")
        self.setheading(90)

    def up(self):
        """The car moves forward"""
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)

