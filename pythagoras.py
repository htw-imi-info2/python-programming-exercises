#-----------------------------------------------------------------------
# Pythagoras Tree
#-----------------------------------------------------------------------
# python has a Turtle Graphics, see
# https://docs.python.org/3.7/library/turtle.html


import sys
from turtle import *


def square(side_length,n):
    forward(side_length)
    if (n > 0):
        pyth(side_length,n-1)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)


def pyth(side_length,n):
    len_right = side_length/5*4
    right(36.87)
    square(len_right,n-1)
    left(90)
    forward(len_right)

    len_left = side_length/5*3
    square(len_left,n-1)
    left(90)
    forward(len_left)
    left(36.87+90)
    forward(side_length)
    left(90)




def pythagoras_tree(side_length,n):
    square(side_length,n)

def startposition(len):
    up()
    setposition((len/2),-300)
    left(90)
    down()



def main(n):
    color('green', 'pink')
    begin_fill()
    len = 100
    startposition(len)
    pythagoras_tree(len,n)

    end_fill()
    done()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(int(sys.argv[1]))
  else:
    print("usage: pythagoras.py <n>")
