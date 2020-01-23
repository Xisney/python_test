"""
python相关
飘落的樱花与樱花树
date: 2020-1-10
author: xys
version: 1.0
"""

from turtle import *
from random import *
from math import *


# 定义绘图函数
def tree(n, m):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(m)  # 绘制树枝
    if n > 0:
        b = random() * 15 + 10  # 右分支偏转角度
        c = random() * 15 + 10  # 左分支偏转角度
        d = m * (random() * 0.25 + 0.7)  # 下一个分支的长度
        # 绘制右分支
        right(b)
        tree(n - 1, d)
        # 绘制左分支
        left(b + c)  # 向左转c角度
        tree(n - 1, d)
        # 回归正确位置
        right(c)
    else:
        # 绘制叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5  # heading用于返回当前角度
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(m)


if __name__ == '__main__':
    bgcolor(0.5, 0.5, 0.5)
    ht()
    speed(1)  # 速度调节
    tracer(0, 0)  # 什么功能？
    pu()
    backward(100)
    left(90)
    pu()
    backward(300)
    tree(12, 100)  # 递归7层
    done()
