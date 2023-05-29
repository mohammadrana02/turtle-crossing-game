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
car_manager = CarManager()
scoreboard = Scoreboard()

# the player moves using the up key
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True

while game_is_on:
    # the screen updates 10 times per second
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()  # adds a car to the game
    car_manager.move()  # moves the cars across the screen

    # detects if the player collides with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detects if the player completes the level
    if player.ycor() > 280:
        car_manager.next_level()
        player.next_level()
        scoreboard.next_level()

screen.exitonclick()
