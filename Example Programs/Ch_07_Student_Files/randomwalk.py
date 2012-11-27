"""
File: randomwalk.py

A turtle takes a random walk.
"""

from turtlegraphics import Turtle
import random

def randomWalk(turtle, turns, distance = 20):
    turtle.setWidth(1)
    for x in xrange(turns):
        turtle.turn(random.randint(0, 360))
        turtle.move(distance)

randomWalk(Turtle(), 30)
