import math
def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int(input())
while t>0:
    t-=1

    n=int(input())
    count = 0
    for i in range(2,n-6):
        if snt(i) and snt(i+2) and snt(i+6): count+=1
        elif snt(i) and snt(i+4) and snt(i+6): count+=1
    print(count)
