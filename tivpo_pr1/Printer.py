from turtle import *

class Printer:

    t: Turtle = Turtle()
    window: Screen = Screen()

    def __init__(self):
        self.window.screensize(canvwidth=1920, canvheight=1080, bg="white")
        self.t.hideturtle()

    def showScreen(self):
        self.window.exitonclick()

    def drawArrowRight(self):
        forward(150)
        left(90)
        forward(30)
        right(120)
        forward(90)
        right(120)
        forward(90)
        right(120)
        forward(30)
        left(90)
        forward(150)
        right(90)
        forward(30)

    def drawArrowLeft(self):
        left(180)
        self.drawArrowRight()

    def drawArrowLeftRight(self):
        forward(75)
        left(90)
        forward(30)
        right(120)
        forward(90)
        right(120)
        forward(90)
        right(120)
        forward(30)
        left(90)
        forward(150)
        left(90)
        forward(30)
        right(120)
        forward(90)
        right(120)
        forward(90)
        right(120)
        forward(30)
        left(90)
        forward(75)

    def drawSquare(self):
        for i in range(4):
            forward(210)
            right(90)
    
    def drawCircle(self):
        self.t.circle(105)