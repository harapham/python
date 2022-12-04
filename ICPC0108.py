t = int(input())
while t>0:
    t-=1
    n=int(input())
    a=sorted([int(i) for i in input().split()])
    res=0
    for i in range(n-2):
        l,r =i+1,n-1
        while l<r:
            if a[l]+a[i]+a[r]==0:
                res+=1
                l+=1
            elif a[l]+a[i]+a[r]<0:
                l+=1
            else : r-=1
    print(res)
    