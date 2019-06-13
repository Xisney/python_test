"""

version:0.1
author:Jason
date: 2019-06-08
"""
from turtle import *


def main():
    def curvemove():
        for i in range(200):
            right(1)
            forward(1)
    color('violet', 'pink')
    begin_fill()
    left(140)
    forward(111.65)
    curvemove()
    left(120)
    curvemove()
    forward(111.65)
    end_fill()
    done()


if __name__ == '__main__':
    main()
