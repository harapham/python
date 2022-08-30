import math

def nt(a):
    if a<2: return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0: return False
    return True

t=int(input())
for i in range(t):
    s=input()
    a=int(s[-4:])
    print('YES' if nt(a)==True else 'NO')
