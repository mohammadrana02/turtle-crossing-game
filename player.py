from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# PLAYER BEHAVIOUR:
# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, - 250)
        self.color("white")
        self.shape("turtle")
        self.setheading(90)

    def up(self):
        self.forward(10)