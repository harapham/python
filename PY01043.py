import re

def sotn(n):
    k=0
    i='2'
    while k<n:  
        if re.fullmatch('[02468]+',i) :
            ii=i[::-1]
            k=int(i+ii)
            if k<n: print(k,end=' ')
        i=str(int(i)+2)

t=int(input())
while t>0:
    t-=1
    n=int(input())
    sotn(n)
    print()