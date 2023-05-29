from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        """adds a car to the game"""
        random_chance = random.randint(1, 6)  # a car has a 1/6 chance of being generated per loop of the program so
        # the screen doesn't get filled up with cars
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(x=300, y=random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        """The cars moves across the screen"""
        for car in self.all_cars:
            car.forward(self.speed)

    def next_level(self):
        """The speed of the cars increases"""
        self.speed += MOVE_INCREMENT


