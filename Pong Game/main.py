from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0) #Remove animations

rpaddle=Paddle((350,0))
lpaddle=Paddle((-350,0))

ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkeypress(rpaddle.goUp,"Up")
screen.onkeypress(rpaddle.goDown,"Down")
screen.onkeypress(lpaddle.goUp,"w")
screen.onkeypress(lpaddle.goDown,"s")


gameIsOn=True
while gameIsOn:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    #Wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounceY()
    #Paddle collision
    if ball.distance(rpaddle)<70 and ball.xcor()>330 or ball.distance(lpaddle)<30 and ball.xcor()>-400:
        ball.bounceX()
        time.sleep
    #paddle miss
    if ball.xcor()>370:
        ball.reset()
        scoreboard.lpoint()
    if ball.xcor()<-400:
        ball.reset()
        scoreboard.rpoint()

screen.exitonclick()