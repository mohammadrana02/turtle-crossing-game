import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

# COLLISION DETECTION
# Detect when the turtle player collides with a car and stop
# the game if this happens.

# LEVEL FINISH DETECTION
# Detect when the turtle player has reached the top edge of the screen
# (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle
# to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT
# to increase the car speed. If you get stuck, check the video walkthrough
# in Step 6.



