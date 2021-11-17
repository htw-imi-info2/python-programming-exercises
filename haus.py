# -----------------------------------------------------------------------
# Pythagoras Tree
# -----------------------------------------------------------------------
# python has a Turtle Graphics, see
# https://docs.python.org/3.10/library/turtle.html
# for available colors see https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html


import sys
from turtle import *


def square(side_length):
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)

def start_position(side_length):
    up()
    setposition((side_length / 2), -300)
    left(90)
    down()

def haus():
    side_length = 300
    start_position(side_length)
    square(side_length)
    done()


if __name__ == '__main__':
    haus()


