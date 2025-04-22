import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="orange")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Simple")
        self.pack(fill=tk.BOTH, expand=True)


def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
