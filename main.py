# Author: Lohit Sharma
# Purpose: This program makes a sinograph using turtle library
import random
from turtle import Turtle, Screen  # import appropriate packages

lavi = Turtle()  # initialize Turtle object
screen = Screen()  # initialize Screen object
screen.colormode(255)

def new_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb


def sino_graph():
    for x in range(100):
        lavi.color(new_color())
        lavi.circle(100)
        lavi.left(10)


sino_graph()
screen.exitonclick()
