t=int(input())
while t>0:
    a=input()
    k=0
    for i in range(len(a)):
        k+=int(a[i])
    if k%10==0:
        ok=1
        for i in range(len(a)-1):
            if abs(int(a[i])-int(a[i+1]))!=2:
                ok=0
                break
        print('YES' if ok==1 else 'NO')
    else: print('NO')
    t-=1