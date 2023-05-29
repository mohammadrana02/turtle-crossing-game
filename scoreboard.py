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
        self.level = -1
        self.hideturtle()
        self.next_level()

    def next_level(self):
        """Updates the scoreboard by 1 point"""
        self.level += 1
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def game_over(self):
        """Shows the game over screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
