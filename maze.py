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

def main():
    win = Window(800, 600)
    print("THIS IS WIN", win)
    win.wait_for_close()

if __name__ == "__main__":
    main()