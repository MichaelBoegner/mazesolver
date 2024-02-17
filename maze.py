from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Title"
        self.canvas = Canvas()
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
    def draw_line(self, line, fillcolor):
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
        self.fill_color = fill_color
        canvas.create_line(
            self.point_1.x, 
            self.point_1.y, 
            self.point_2.x, 
            self.point_2.y, 
            fill=fill_color, 
            width=2
        )
        canvas.pack()
    


def main():
    win = Window(800, 600)
    point_1 = Point(10,10)
    point_2 = Point(20,20)
    line = Line(point_1, point_2)
    point_3 = Point(10,10)
    point_4 = Point(200,570)
    line2 = Line(point_3, point_4)
    win.draw_line(line,"blue")
    win.draw_line(line2,"orange")
    win.wait_for_close()

if __name__ == "__main__":
    main()