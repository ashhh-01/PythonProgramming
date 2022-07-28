from turtle import Screen
import time
from snake import Snake
from food import Food
from ScoreBoard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreBoard=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



gameOn=True

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Food Collison
    #distance fn btw coordinate(x,y) or a turtle instance
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreBoard.increaseScore()
        

    #Detect wall collison
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 :
        gameOn=False
        scoreBoard.gameOver()

    #Detect Tail collison
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            gameOn=False
            scoreBoard.gameOver()

    
screen.exitonclick()