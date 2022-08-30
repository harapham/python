
import math

def ktra(s):
    d=s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(d[i])-ord(d[i-1])): 
            return False
    return True

t=int(input())
for i in range(t):
    s=input()
    print('YES' if ktra(s)==True else 'NO')