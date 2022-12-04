t = int(input())
while t>0:
    t-=1

    x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    for i in range(x[1],x[0]):
        print(a[i], end=" ")
    for i in range(x[1]):
        print(a[i],end=" ")
    print()
    