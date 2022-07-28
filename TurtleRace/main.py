from turtle import Turtle,Screen
import random
import turtle
screen=Screen()
screen.setup(width=500,height=400)
allTurtle=[]

raceOn=False
user=screen.textinput(title="Make your bet!",prompt="Which colored (blue/orange/green/yellow/black) turtle is going to win?").lower()
color=["red","blue","orange","green","yellow","black"]
ylist=[-70,-40,-10,20,50,80]

for index in range(0,6):
    newTurtle=Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.goto(x=-230,y=ylist[index])
    newTurtle.color(color[index])
    allTurtle.append(newTurtle)

if user:
    raceOn=True
while raceOn:
    for turtles in allTurtle:
        #Half the width of 40*40 turtle is 20 so 250-20 
        if turtles.xcor()>230:
            raceOn=False
            winningColor=turtles.pencolor()
            if winningColor==user:
                print(f"You won!The {winningColor} turtle is the winner!")
            else:
                print(f"You lost!The {winningColor} turtle is the winner!")
        distance=random.randint(0,10)
        turtles.fd(distance)


screen.exitonclick()