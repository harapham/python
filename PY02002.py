
a=[0,1]
for i in range(2,93):
    a.append(a[i-1]+a[i-2])
t=int(input())
while t>0:
    t-=1
    l,r = [int(i) for i in input().split()]
    for i in range(l,r+1):
        print(a[i],end=' ')
    print()