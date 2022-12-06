import math

def snt(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def check(n):
    k=0
    for i in range(len(n)):
        if i%2!=int(n[i])%2: return False
        k+=int(n[i])
    if not snt(k): return False
    return True

t= int(input())
while t>0:
    t-=1
    n=input()
    print('YES' if check(n)==True else 'NO')
    