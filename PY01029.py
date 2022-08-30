
from re import S


def nguyen_to(s,k):
    if k==0: return s
    return nguyen_to(k,s%k)

t=int(input())
for i in range(t):
    s=input()
    k=s[::-1]
    print("YES" if nguyen_to(int(s),int(k))==1 else "NO")