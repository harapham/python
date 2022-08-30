t=int(input())
for i in range(t):
    a=input()
    ok=0
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            print('NO')
            ok=1
            break
    if ok==0: print('YES')