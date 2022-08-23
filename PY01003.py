t=int(input())
while t>0:
    sa=input()
    a=list(sa)
    i=len(sa)-1
    while i>0:
        if int(a[i])>=5:
            a[i-1]=str(int(a[i-1])+1)
        a[i]='0'
        i-=1
    for i in range(len(sa)):
        print(a[i],end='')
    print()
    t-=1