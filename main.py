from graphics import Window, Point, Line, Cell

def main():
    win = Window(500,500)
    # l = Line(Point(50,50),Point(400,400))
    # c1 = Cell(True, True, True, True, 5, 50, 5, 50, True)
    c2 = Cell(True, True, True, True, 20, 40, 100, 120, True)
    c3 = Cell(True, True, True, True, 40, 60, 120, 140, True)
    print("running")
    win.draw_cline(c2, "black")
    win.draw_cline(c3, "red")
    win.wait_for_close()

main()