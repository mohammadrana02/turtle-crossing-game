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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.add_car()

    car.move()

    # detects if the player collides with the car
    for car_num in range(len(car.cars) - 1, 0, -1):
        if player.distance(car.cars[car_num]) < 20:
            player.next_level()

    if player.ycor() > 280:
        car.next_level()
        player.next_level()
        scoreboard.next_level()

screen.exitonclick()

# COLLISION DETECTION DONE
# Detect when the turtle player collides with a car and stop
# the game if this happens.
