FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.pu()
        self.goto(-280,240)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increaseLevel(self):
        self.level+=1
        self.update()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)
