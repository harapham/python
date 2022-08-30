a,k,n=[int(i) for i in input().split()]
du=k-a%k
ok=0
while du<=n-a:
    print(du,end=' ')
    ok=1
    du+=k
if ok==0: print(-1)