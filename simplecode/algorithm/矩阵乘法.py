"""
给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2
　　3 4
　　A的2次幂
　　7 10
　　15 22
输入格式
　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
输出格式
　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开
  
 样例输入
2 2
1 2
3 4
样例输出
7 10
15 22

"""



def compute(s,t,n):
    temp=0
    h=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp+=s[i][k]*t[k][j]
            h[i][j]=temp
            temp=0
    return h

    
if __name__ == '__main__':
    n,m=map(int,input().split())
    s=[]
    if m==0:
        for i in range(n):
            for j in range(n):
                if i==j:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print()
    else:
        for i in range(n):
            s.append(list(map(int,input().split())))
        if m==1:
            for i in s:
                for j in i:
                    print(j,end=' ')
                print()
        else:
            t=s
            for i in range(1,m):
                s=compute(s,t,n)
            for i in s:
                for j in i:
                    print(j,end=' ')
                print()

