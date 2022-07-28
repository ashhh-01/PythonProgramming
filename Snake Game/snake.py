POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE=20
import turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        #Auto initialise
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.addSegment(position)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            newX=self.segments[seg_num-1].xcor()
            newY=self.segments[seg_num-1].ycor()
            #2nd Segments will take the first Segments coordinates and 3rd takes 2nd  
            self.segments[seg_num].goto(newX,newY)
        self.head.fd(MOVE)
    
    def addSegment(self,position):
            seg=turtle.Turtle(shape="square")
            seg.color("white")
            seg.pu()
            seg.goto(position)
            self.segments.append(seg)
    
    def extend(self):
        self.addSegment(self.segments[-1].position())


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
 