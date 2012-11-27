"""
Program file: ccurve.py
Author: Ken

This program prompts the user for the level of
a c-curve and draws a c-curve of that level.
"""

from turtlegraphics import Turtle

def cCurve(turtle, x1, y1, x2, y2, level):
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints."""
      turtle.up()
      turtle.move(x1, y1)
      turtle.down()
      turtle.move(x2, y2)
      
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) / 2
      ym = (x2 + y1 + y2 - x1) / 2
      cCurve(turtle, x1, y1, xm, ym, level - 1)
      cCurve(turtle, xm, ym, x2, y2, level - 1)

def main():
   level = input("Enter the level (0 or greater): ")
   turtle = Turtle(400, 500)
   turtle.setWidth(1)
   cCurve(turtle, 50, -100, 50, 100, level)

#main()

def testCurves():
   """Display first 7 curves and also level 10."""
   for level in range(0, 7):
      turtle = Turtle()
      turtle.setColor(0, 0, 0)
      cCurve(turtle, 50, -50, 50, 50, level)

testCurves()
   
