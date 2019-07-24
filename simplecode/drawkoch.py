"""
暑期python学习
科赫曲线的绘制

version:0.1
author:Jason
date: 2019-07-24
"""
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 4
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
