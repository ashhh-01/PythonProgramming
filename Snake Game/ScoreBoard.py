from tkinter import CENTER
from turtle import Turtle, update
ALIGNMENT="center"
FONT=("Arial" ,15,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)



    def gameOver(self):
        self.goto(0,0) 
        self.write("GAME OVER!",align=CENTER,font=FONT)
          

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScore()


