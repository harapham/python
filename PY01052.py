import math

def nguyen_to(s):
    if s<2: return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0: return False
    return True
t=int(input())
for i in range(t):
    s=input()
    kq=0
    for j in range(len(s)):
        kq+=int(s[j])
    print('YES' if nguyen_to(kq) else 'NO')