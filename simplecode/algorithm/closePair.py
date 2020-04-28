import math
import random

"""
分治法求解最近点对
"""


# 计算欧几里得距离
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# 分治法求解最近点对的函数
def close_pair(x, y, n):
    if n <= 3:
        res = math.inf
        for i in range(n):
            for j in range(i + 1, n):  # 不计算与它本身的距离
                temp = distance(x[i], x[j])
                if res > temp:
                    res = temp
                    min_one = i
                    min_two = j
    else:
        # 将点对进行分组
        x1 = x[:math.ceil(n / 2)]
        y1 = y[:math.ceil(n / 2)]
        x2 = x[math.floor(n / 2):]
        y2 = y[math.floor(n / 2):]

        d1, min_one, min_two = close_pair(x1, y1, len(x1))
        d2, min_one, min_two = close_pair(x2, y2, len(x2))
        d = min(d1, d2)

        m = x[math.ceil(n / 2) - 1][0]  # 得到中位线

        s = []
        # 将x在m周围d距离以内的点，加入
        for i in y:
            if abs(m - i[0]) < d:
                s.append(i)

        res = d

        # 判断是否最小距离在不同区域
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                res = min(distance(s[i], s[j]), res)

    return res, min_one, min_two


if __name__ == '__main__':
    n = int(input())
    x = []  # 用于存放点对

    for i in range(n):  # 随机生成n组点对
        h = random.randint(-10, 10)
        s = random.randint(-10, 10)
        x.append([h, s])

    y = x.copy()  # 获得点集的深拷贝

    x.sort(key=lambda x: x[0])  # 按照x轴升序排列
    y.sort(key=lambda x: x[1])  # 按照y轴升序排列

    print("生成的点对按x排序为：")
    print(x)
    print("生成的点对按y排序为：")
    print(y)

    res, min_one, min_two = close_pair(x, y, n)
    print("最近距离为:%.2f" % res)
    print("两点分别为：")
    print(x[min_one], x[min_two])
