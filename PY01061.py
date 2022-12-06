import math

def nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t= int(input())
while t>0:
    t-=1
    n=input()
    d=int(n[:3])
    c=int(n[len(n)-3:])
    
    print('YES' if nt(d)==nt(c)==True else 'NO')
