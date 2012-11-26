# -*- coding: cp1252 -*-
import os
import sys
import Tkinter

class Main:
     def __init__(self, root):
         self.Root = root
         Btn = Tkinter.Button(self.Root, text = "My Button")
         Btn.grid(column = 0, row = 0)

if __name__ == '__main__':
     root = Tkinter.Tk()
     root.title("My First GUI")

     Main(root)

     root.mainloop()

