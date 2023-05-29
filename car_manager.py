from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# LEVEL FINISH DETECTION
# Detect when the turtle player has reached the top edge of the screen
# (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle
# to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT
# to increase the car speed. If you get stuck, check the video walkthrough
# in Step 6.

# CAR BEHAVIOUR
# Create cars that are 20px high by 40px wide that are randomly
# generated along the y-axis and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.

class CarManager:
    def __init__(self):
        self.cars = []
        self.start_cars()
        self.speed = STARTING_MOVE_DISTANCE

    def start_cars(self):
        for i in range(20):
            self.add_car()

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setposition(x=random.randint(320, 350), y=random.randint(-250, 250))
        new_car.setheading(180)
        new_car.forward(5)
        self.cars.append(new_car)

    def move(self):
        for car_num in range(len(self.cars) - 1, 0, -1):
            self.cars[car_num].forward(20)

    def next_level(self):
        for car in self.cars:
            pass
