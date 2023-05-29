from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("white")
        self.shape("turtle")
        self.setheading(90)

    def up(self):
        """The turtle moves forward"""
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        """The turtle goes back to the starting position"""
        self.goto(STARTING_POSITION)
