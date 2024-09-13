from turtle import *

class Printer:

    t: Turtle = Turtle()
    window: Screen = Screen()
    coord_x = 270
    coord_y = 210

    def __init__(self):
        self.window.screensize(canvwidth=1920, canvheight=1080, bg="white")
        self.window.setup(1920, 1080)
        self.window.setworldcoordinates(-1, self.window.window_height() - 1, self.window.window_width() - 1, -1)
        self.t.hideturtle()

    def showScreen(self):
        self.window.exitonclick()

    def setPositionOnCoords(self, index, line):
        self.t.penup()
        self.t.setpos(index, line)
        self.t.pendown()

    def drawArrowRight(self, index, line):
        self.setPositionOnCoords((index + 1) * self.coord_x - self.coord_x / 2, line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 30 + 20 * line)
        self.t.forward(150)
        self.t.left(90)
        self.t.forward(30)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(30)
        self.t.left(90)
        self.t.forward(150)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)

    def drawArrowLeft(self, index, line):
        self.setPositionOnCoords((index + 1) * self.coord_x + self.coord_x / 2, line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 20 * line)
        self.t.left(180)
        self.t.forward(150)
        self.t.left(90)
        self.t.forward(30)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(30)
        self.t.left(90)
        self.t.forward(150)
        self.t.right(90)
        self.t.forward(30)
        self.t.left(90)

    def drawArrowLeftRight(self, index, line):
        self.setPositionOnCoords((index + 1) * self.coord_x, line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 20 * line + 30)
        self.t.forward(50)
        self.t.left(90)
        self.t.forward(30)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(30)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(30)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(90)
        self.t.right(120)
        self.t.forward(30)
        self.t.left(90)
        self.t.forward(50)

    def drawSquare(self, index, line):
        self.setPositionOnCoords((index + 1) * self.coord_x - self.coord_x / 3, line * self.coord_y + 20 * line)
        for i in range(4):
            self.t.forward(self.coord_y)
            self.t.right(90)
    
    def drawCircle(self, index, line):
        self.setPositionOnCoords((index + 1) * self.coord_x, line * self.coord_y - self.coord_y + 20 * line)
        self.t.circle(self.coord_y / 2)

    figuresdict = {
            "->" : drawArrowRight,
            "<-" : drawArrowLeft,
            "<->" : drawArrowLeftRight,
            "()" : drawCircle,
            "[]" : drawSquare
        }

    def drawWholePicture(self, symbols):
        for symbol in symbols:
            self.figuresdict[symbol.symbol](self, symbol.index, symbol.line_num)
            