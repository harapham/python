t=int(input())
for i in range(t):
    n=int(input())
    k=0
    for j in range(n,0,-2):
        k+=1/j
    print('%.6f' %k)
