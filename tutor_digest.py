import tkinter as tk


class Avatar(tk.Frame):
    def __init__(self, parent=None, width=100, height=100, ovalness=1, bg_frame_color='orange', bg_canvas_color='black'):
        super().__init__(parent, width=width, height=height, bg=bg_frame_color)
        self.grid()

        self.width = width
        self.height = height
        self.ovalness = ovalness
        self.bg_frame_color = bg_frame_color
        self.bg_canvas_color = bg_canvas_color

        # Create first canvas
        self.canvas1 = tk.Canvas(self, width=width / 2, height=height / 2,
                                 bg=bg_canvas_color, borderwidth=0)
        self.canvas1.grid(row=0, column=0, padx=0, pady=0)
        self.canvas1.grid_propagate(False)

        # Create second canvas
        self.canvas2 = tk.Canvas(self, width=width / 2, height=height / 2,
                                 bg=bg_canvas_color, borderwidth=0)
        self.canvas2.grid(row=1, column=1, padx=0, pady=0)
        self.canvas2.grid_propagate(False)

        self.draw()

    def draw(self):
        # Placeholder for drawing logic
        pass


if __name__ == '__main__':
    root = tk.Tk()
    avatar = Avatar(parent=root)
    avatar.mainloop()
