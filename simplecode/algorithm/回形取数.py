"""

回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。
样例输入
3 3
1 2 3
4 5 6
7 8 9
样例输出
1 4 7 8 9 6 3 2 5
"""




import math


if __name__ == '__main__':
    m,n=map(int,input().split())
    s=[]

    for i in range(m):
        s.append(input().split())

    # 圈数,向上取整
    t=math.ceil(min(m,n)/2)
    results=[]
    # 输出时，右边的列号要大于左边的即n-1-1oop>loop。
    # 上边的行号要小于下边的,即loop<m-1-loop
    for loop in range(t):
        for y in range(loop,m-loop):  # first line
            results.append(s[y][loop])
        for x in range(loop+1,n-loop):  # second line
            results.append(s[m-1-loop][x])
        if n-1>2*loop:
            for u in range(m-2-loop,loop-1,-1):
                results.append(s[u][n-1-loop])
        if m-1>2*loop:
            for l in range(n-2-loop,loop,-1):
                results.append(s[loop][l])
    for i in range(len(results)):
        print(results[i],'',end='')
            
    
