import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player=Player()
carManager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkeypress(player.move,"Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.createCar()
    carManager.move()
    #Car collison
    for car in carManager.allCars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.gameOver()
    #Reached Finished Line
    if player.reachedFinishedLine():
        player.goTostart()
        carManager.level()
        scoreboard.increaseLevel()

screen.exitonclick()