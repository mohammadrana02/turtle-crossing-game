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
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move()

    # if player.ycor() > 250:
    #     car.next_level()

screen.exitonclick()

# COLLISION DETECTION
# Detect when the turtle player collides with a car and stop
# the game if this happens.





