from turtle import Turtle

FONT = ("Courier", 24, "normal")


# SCOREBOARD BEHAVIOUR
# Create a scoreboard that keeps track of which level
# the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car,
# GAME OVER should be displayed in the centre.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.level = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()
