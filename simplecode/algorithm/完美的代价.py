"""
回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。
小龙龙认为回文串才是完美的。现在给你一个串，
它不一定是回文的，请你计算最少的交换次数使得该串变成一个完美的回文串。
交换的定义是：交换两个相邻的字符

输入格式
　　第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
　　第二行是一个字符串，长度为N.只包含小写字母
输出格式
　　如果可能，输出最少的交换次数。
　　否则输出Impossible

"""

def is_hw(n,s):
    temp=set()
    if n%2==0:
        for i in range(26):
            if s.count(chr(ord('a')+i))%2!=0:
                return False
    else:
        for i in range(26):
            if s.count(chr(ord('a')+i))%2!=0:
                temp.add(chr(ord('a')+i))
        if len(temp)>1:
            return False
    return True

def step(n,s,k):
    res=0
    for i in range(n//2):
        if s[i:].count(s[i])!=1:  # 保证访问元素后移
            temp=k[:n-i].index(s[i])  # 保证访问元素前移
            res+=temp
            k.pop(temp)
            s=k[::-1]  # 更新s
        else:
            res+=n//2-i
    return res




    

if __name__ == '__main__':
    n=int(input())
    s=list(input())
    k=s[::-1]
    
    if is_hw(n,s):
        print(step(n,s,k))
    else:
        print('Impossible')
    
    
            
            
    
