
"""
问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。
输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。
输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。


"""





def exchange(x1,y1,x2,y2):
    sx1=min(x1,x2)
    sy1=min(y1,y2)
    sx2=max(x1,x2)
    sy2=max(y1,y2)
    return sx1,sy1,sx2,sy2

    

if __name__ == '__main__':
    x1,y1,x2,y2=map(float,input().split(' '))
    x1,y1,x2,y2=exchange(x1,y1,x2,y2)
    x3,y3,x4,y4=map(float,input().split(' '))
    x3,y3,x4,y4=exchange(x3,y3,x4,y4)
    area=0

    tx1=max(x1,x3)
    ty1=max(y1,y3)
    tx2=min(x2,x4)
    ty2=min(y2,y4)

    if tx2-tx1<=0 or ty2-ty1<=0:
        area=0
    else:
        area=(tx2-tx1)*(ty2-ty1)
    print("%.2f" % area)
            
    
