
"""
问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)(具体可看样例)
 样例输入
3 10
样例输出
3=3
4=2*2
5=5
6=2*3
7=7
8=2*2*2
9=3*3
10=2*5


"""


import math

def spread_zs(temp,n):
    for i in range(2,n+1):
        if n%i==0:
            temp+=str(i)
            n=n//i
            if n==1:
                return temp
            elif n in res:
                return temp+'*'+res[n]
            else:
                temp+='*'
                return spread_zs(temp,n)


        
    
if __name__ == '__main__':
    a,b=map(int,input().split())
    res={}

    for i in range(a,b+1):
        temp=''
        res[i]=spread_zs(temp,i)
    for i in range(a,b+1):
        print(str(i)+'='+str(res[i]))
    
