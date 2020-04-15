"""
给定一个n*n的棋盘，棋盘中有一些位置不能放皇后。
现在要向棋盘中放入n个黑皇后和n个白皇后，
使任意的两个黑皇后都不在同一行、同一列或同一条对角线上，任意的两个白皇后都不在同一行、同一列或同一条对角线上。
问总共有多少种放法？n小于等于8。
"""



n=int(input())
s=[]  # 存放初始位置
result=0  # 存放结果
for i in range(n):
    s.append(input().split())

# 存放皇后的位置，index表示row,value表示column    
white=[None for _ in range(n)]
black=[None for _ in range(n)]

# 检验白皇后当前位置是否合法
def check_white(white,row):
    if s[row][white[row]] == '1':
        for i in range(row):  # 行列距离相等判断对角线
            if white[i]==white[row] or abs(white[i]-white[row])==abs(i-row):
                return False
        return True
    return False

# 检验黑皇后位置是否合法
def check_black(black,white,row):
    if s[row][black[row]]=='1' and white[row]!=black[row]:
        for i in range(row):  # 判断是否共线(列与对角线)
            if black[i]==black[row] or abs(black[row]-black[i])==abs(row-i):
                return False
        return True
    return False

# 放置白皇后于当前行
def put_white(white,row):
    if row==n:  # 放置完白皇后，开始放置黑皇后
        put_black(black,0)
    else:
        for j in range(n):
            white[row]=j
            if check_white(white,row):  # 该位置可行则向下一层寻找
                put_white(white,row+1)

def put_black(black,row):
    if row==n:
        global result
        result+=1
        return
    else:
        for j in range(n):
            black[row]=j
            if check_black(black,white,row):
                put_black(black,row+1)
                

    
if __name__ == '__main__':
    put_white(white,0)
    print(result)
    

    
