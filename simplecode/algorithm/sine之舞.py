"""
最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，
必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。
　　不妨设
　　An=sin(1–sin(2+sin(3–sin(4+...sin(n))...)
　　Sn=(...(A1+n)A2+n-1)A3+...+2)An+1
　　FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。
输入格式
　　仅有一个数：N<201。
输出格式
　　请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。

"""



def get_r(n,a,t):
    if n==1:
        return a[n-1]+'+'+str(t)
    else:
        return '('+get_r(n-1,a,t+1)+')'+a[n-1]+'+'+str(t)
    


if __name__ == '__main__':
    n=int(input())
    s=[]
    a='sin(1'
    s.append(a)
    for i in range(2,n+1):
        if i%2==0:
            a+='-sin('+str(i)
        else:
            a+='+sin('+str(i)
        s.append(a+')'*(i))
    s[0]='sin(1)'
    print(get_r(n,s,1))
        
            
            
    
