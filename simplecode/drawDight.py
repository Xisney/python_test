"""
七段数码管绘制（turtle）

version:0.1
author:Jason
date: 2019-07-24
"""
import turtle, datetime


def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDight(d):
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for i in date:
        drawDight(int(i))


def main():
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.pendown()
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
