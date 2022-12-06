import math

def nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t= int(input())
def check(n):
    for i in range(len(n)):
        if nt(i)!=nt(int(n[i])): return False
    return True
while t>0:
    t-=1
    print('YES' if check(input())==True else 'NO')
