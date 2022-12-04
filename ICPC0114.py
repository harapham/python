import math

def snt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def test(n):
    nn=n[::-1]
    k=ok=0
    for i in range(len(n)):
        k+=int(n[i])
        if not snt(int(n[i])): ok=1
    if snt(int(n)) and snt(int(nn)) and snt(k) and not ok:
        return True
    return False

t=int(input())
while t>0:
    t-=1

    print('Yes' if test(input()) else 'No')

        
