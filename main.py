from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root, width = self.width, height = self.height, bg = "white")
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

    def draw_line(self, x1, y1, x2, y2, fill_color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill_color = fill_color
        line = Line(self.x1, self.y1, self.x2, self.y2)
        line.draw(self.__canvas, self.fill_color)

class Point:
    x = 0
    y = 0

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas, fill_color):
        print(self.x1, self.y1, self.x2, self.y2)
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill = fill_color, width = 5
        )
        canvas.pack()

def main():
    win = Window(500,500)
    print("running")
    win.draw_line(2,2,400,400, "white")
    win.draw_line(52,35,188,399, "white")
    win.wait_for_close()

main()