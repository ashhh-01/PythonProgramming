COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
import time
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.allCars=[]
        self.hideturtle()
        self.carSpeed=STARTING_MOVE_DISTANCE

    def createCar(self):
        randomChance=random.randint(0,2)
        if randomChance==2:
            newCar=Turtle("square")
            newCar.color(random.choice(COLORS))
            newCar.setheading(180)
            newCar.shapesize(stretch_len=2,stretch_wid=1)
            newCar.pu()
            randomY=random.randint(-250,250)
            newCar.goto(300,randomY)
            self.allCars.append(newCar)

    def move(self):
        for car in self.allCars:
            car.fd(STARTING_MOVE_DISTANCE)

    def level(self):
        self.carSpeed+=MOVE_INCREMENT