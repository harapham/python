t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    Min=min(a)
    Max=max(a)
    dem=0
    for s in range(Min,Max):
        if not(s in a): dem+=1
    print(dem)