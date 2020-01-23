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
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
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
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)
        # 添加0.3的飘落叶子
        if random() > 0.7:
            pu()
            # 飘落
            t = heading()
            an = -40 + random() * 40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random())
            forward(dis)
            setheading(t)
            # 叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 * n * 0.4)
            circle(2)
            left(90)
            pu()
            # 返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(m)


if __name__ == '__main__':
    bgcolor(0.5, 0.5, 0.5)
    ht()
    speed(1)  # 速度调节
    tracer(0, 0)
    pu()
    backward(100)
    left(90)
    pu()
    backward(300)
    tree(12, 100)  # 递归7层
    done()
