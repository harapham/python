import math
def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

a=[[]]
n,m = [int(i) for i in input().split()]
for i in range(n):
    x=[int(k) for k in input().split()]
    for j in range(m):
        if snt(x[j]): print(1, end=' ')
        else : print(0, end=' ')
    print()

