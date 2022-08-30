t=int(input())
for i in range(t):
    n,x,m=[float(i) for i in input().split()]
    a=0
    while n<m:
        n=n+n*x/100
        a+=1
    print(a)