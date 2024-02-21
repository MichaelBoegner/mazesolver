from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Title"
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
    def close(self):
        self.running = False
    def draw_line(self, line, fillcolor="black"):
        line.draw(self.canvas, fillcolor)

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
class Line:
    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1.x, 
            self.point_1.y, 
            self.point_2.x, 
            self.point_2.y, 
            fill=fill_color, 
            width=2
        )
        canvas.pack()
    
class Cell:
    def __init__(self, window):
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window

    def draw_line(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
            
    def draw_move(self, to_cell, undo=False):
        if undo: 
            fillcolor = "red"
        else:
            fillcolor = "black"
        line = Line(Point(self._x2*.75,self._y2*.75), Point(to_cell._x2*.75, to_cell._y2*.85))
        self._window.draw_line(line, fillcolor)



def main():
    window = Window(800, 800)
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell1.has_left_wall = True
    cell1.has_top_wall = True
    cell1.has_right_wall = True
    cell1.has_bottom_wall = True
    cell1.draw_line(100,100,200,200)

    cell2.has_left_wall = True
    cell2.has_top_wall = True
    cell2.has_right_wall = True
    cell2.has_bottom_wall = True
    cell2.draw_line(100,200,200,300)

    cell1.draw_move(cell2, True)

    window.wait_for_close()

if __name__ == "__main__":
    main()