from turtle import Turtle, Screen


class Printer:
    t: Turtle = Turtle()
    window: Screen = Screen()

    screen_x = 1820
    screen_y = 1000

    coord_x = (
        270  # координаты, отображающие размер фигуры, и ячейки, в которую входит фигура
    )
    coord_y = (
        210  # при желании можно оформить всё в скейлинг, но это ещё час работы (больше)
    )

    def __init__(self):
        self.window.screensize(
            canvwidth=self.screen_x, canvheight=self.screen_y, bg="white"
        )  # размер холста в пикселях
        self.window.setup(self.screen_x, self.screen_y)  # размер окна
        self.window.setworldcoordinates(
            -1, self.window.window_height() - 1, self.window.window_width() - 1, -1
        )  # измерения координат, конкретно сейчас оно означает-->
        self.t.hideturtle()  # --> 0, 0 координат находятся в верхнем левом углу
        self.t.speed(100)

    def show_screen(self):
        self.window.exitonclick()

    def set_position_on_coords(
        self, index, line
    ):  # позиционирование под координаты фигуры
        self.t.penup()  # поднять карандаш (не рисовать)
        self.t.setpos(index, line)  # установка позиции
        self.t.pendown()  # опустить карандаш (рисовать)

    def draw_arrow_right(self, index, line):
        self.set_position_on_coords(
            (index + 1) * self.coord_x - self.coord_x / 2,
            line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 30 + 20 * line,
        )
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

    def draw_arrow_left(self, index, line):
        self.set_position_on_coords(
            (index + 1) * self.coord_x + self.coord_x / 2,
            line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 20 * line,
        )
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

    def draw_arrow_left_right(self, index, line):
        self.set_position_on_coords(
            (index + 1) * self.coord_x,
            line * self.coord_y / 2 + self.coord_y / 2 * (line - 1) + 20 * line + 30,
        )
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

    def draw_square(self, index, line):
        self.set_position_on_coords(
            (index + 1) * self.coord_x - self.coord_x / 3,
            line * self.coord_y + 20 * line,
        )
        for i in range(4):
            self.t.forward(self.coord_y)
            self.t.right(90)

    def draw_circle(self, index, line):
        self.set_position_on_coords(
            (index + 1) * self.coord_x, line * self.coord_y - self.coord_y + 20 * line
        )
        self.t.speed(1)
        self.t.circle(self.coord_y / 2)
        self.t.speed(100)

    figuresdict = {
        "->": draw_arrow_right,
        "<-": draw_arrow_left,
        "<->": draw_arrow_left_right,
        "()": draw_circle,
        "[]": draw_square,
    }

    def draw_whole_picture(self, symbols):
        for symbol in symbols:
            self.figuresdict[symbol.symbol](self, symbol.index, symbol.line_num)
