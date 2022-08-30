import math
def nt(k):
    if k<2: return False
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def kiem_tra(n,m):
    k=math.gcd(n,m)
    t=0
    while k>0:
        t+=k%10
        k=k//10
    if nt(t)==True: return True
    return False

t=int(input())
for i in range(t):
    s=input().split()
    n=int(s[0])
    m=int(s[1])
    print('YES' if kiem_tra(n,m)==True else 'NO')