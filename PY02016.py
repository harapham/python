
t=int(input())
while t>0:
    t-=1
    n=int(input())
    di=dict()
    a=input().split()
    s=0
    p=''
    for i in a:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    for i in a:
        if di[i]>s:
            s=di[i]
            p=i
    
    if s>n/2: print(p)
    else : print('NO')
