
import math

def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int(input())

while t>0:
    t-=1

    n = int(input())
    se = []
    for i in range(n):
        if snt(i) and se.count(i)==0:
            ii = str(i)[::-1]
            if int(ii)!=i and snt(int(ii)) and int(ii)<n:
                se.append(i)
                se.append(int(ii))
    for i in range(len(se)):
        print(se[i],end=' ')
    print()