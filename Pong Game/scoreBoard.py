from turtle import Turtle
ALIGNMENT="center"
FONT=("courier",80,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(self.rscore,align=ALIGNMENT,font=FONT)


    def lpoint(self):
        self.lscore+=1
        self.update()
    
    def rpoint(self):
        self.rscore+=1
        self.update()