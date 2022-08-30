import math
from operator import truediv
def nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
t=int(input())
while t>0:
    n=int(input())
    k=0
    for i in range(n):
        if math.gcd(i,n)==1: k+=1
    print('YES' if nt(k)==True else 'NO')
    t-=1