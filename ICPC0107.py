import re

t= int(input())
while t>0:
    t-=1
    x = input().split()
    s = input().split()
    if len(s)==1:
        s1=s[0]
        s2=input()
    else:    
        s1,s2=s[0],s[1]
    sx1 = re.sub(x[0],x[1],s1)
    sx2 = re.sub(x[0],x[1],s2)
    sy1 = re.sub(x[1],x[0],s1)
    sy2 = re.sub(x[1],x[0],s2)

    m1=str(int(sx1)+int(sx2))
    m2=str(int(sy1)+int(sy2))
    print(m1+" "+m2 if m1<m2 else m2+" "+m1 )
