"""
十二亿三千四百五十六万七千零九
　　用汉语拼音表示为
　　shi er yi san qian si bai wu shi liu wan qi qian ling jiu

"""



def read_four_num(n):
    n=list(map(int,n))

    if n[0]!=0:  # 千位不为零
        res.append(s[n[0]])
        res.append('qian')
    else:
        pass  # 为零则不读
    if n[1]!=0:  # 百位不为零
        res.append(s[n[1]])
        res.append('bai')
    elif (n[0]==0 and n[1]==0) or (n[1]==0 and n[2]==0 and n[3]==0): # 千位百位都为零
        pass
    else:
        res.append(s[n[1]])
    if n[2]!=0 and n[2]!=1:
        res.append(s[n[2]])
        res.append('shi')
    elif n[2]==1 and n[0]==0 and n[1]==0:
        res.append('shi')
    elif (n[1]==0 and n[2]==0) or (n[2]==0 and n[3]==0):
        pass
    else:
        res.append(s[n[2]])
        
    if n[3]!=0:
        res.append(s[n[3]])
    else:
        pass



if __name__ == '__main__':
    s={0:'ling',1:'yi',2:'er',3:'san',4:'si',5:'wu',
       6:'liu',7:'qi',8:'ba',9:'jiu'}
    res=[]
    n=input()

    if 0<len(n)<=4:
        read_four_num(n.rjust(4,'0'))
    elif 4<len(n)<=8:
        n=n.rjust(8,'0')
        read_four_num(n[:4])
        res.append('wan')
        if n[4:]!='0000' and n[4]=='0':
            res.append('ling')
        read_four_num(n[4:])
    elif 8<len(n)<=12:
        n=n.rjust(12,'0')
        read_four_num(n[:4])
        res.append('yi')
        if n[4:8]!='0000'and n[4]=='0':
            res.append('ling')
            read_four_num(n[4:8])
            res.append('wan')
        elif n[4:8]!='0000':
            read_four_num(n[4:8])
            res.append('wan')
        elif n[4:]=='00000000':
            pass
        else:
            res.append('ling')
        read_four_num(n[8:])
    for i in res:
        print(i,end=' ')
    
            
            
    
