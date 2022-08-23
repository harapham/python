t=int(input())
for i in range(t):
    a=input()
    ok=0
    for j in range(len(a)):
        if a[j]!='4' and a[j]!='7':
            print('NO')
            ok=1
            break
    if ok==0: print('YES')