
import math

t=int(input())
for i in range(t):
    n=int(input())
    print('1 * ',end='')
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            k=0
            while n%i==0:
                n/=i
                k+=1
            if n>1:print(f'{i}^{k} * ',end='')
            else: print(f'{i}^{k}')
    if n>1: print(f'{int(n)}^1')