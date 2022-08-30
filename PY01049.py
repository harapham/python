import math
from operator import truediv

def nto(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def kt(s):
    if nto(len(s))==False: return False
    c=0
    for i in range(len(s)):
        if nto(int(s[i]))==True: c+=1
    if c>=len(s)-c: return True
    return False

t=int(input())
for i in range(t):
    s=input()
    print('YES' if kt(s)==True else 'NO')