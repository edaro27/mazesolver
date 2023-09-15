from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Eduardo's maze solver")
        self.__canvas = Canvas(self.__root, width = width, height = height, bg = "white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_cline(self, cell, fill_color):
        cell.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2
        )
        canvas.pack()

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _x1, _x2, _y1, _y2, _win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            canvas.create_line(
                self._x1, self._y1, self._x1, self._y2, fill = fill_color, width = 2
            )
            canvas.pack()
        if self.has_right_wall:
            canvas.create_line(
                self._x2, self._y1, self._x2, self._y2, fill = fill_color, width = 2
            )
            canvas.pack()
        if self.has_top_wall:
            canvas.create_line(
                self._x1, self._y1, self._x2, self._y1, fill = fill_color, width = 2
            )
            canvas.pack()
        if self.has_bottom_wall:
            canvas.create_line(
                self._x1, self._y2, self._x2, self._y2, fill = fill_color, width = 2
            )
            canvas.pack()
    