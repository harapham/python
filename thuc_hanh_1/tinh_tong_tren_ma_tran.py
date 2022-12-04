import numpy as np
s=input().split()
n,m,k=int(s[0]),int(s[1]),int(s[2])
a=np.zeros((n,m))
for i in range(n):
    for j in range(m):
        a[i][j]=int((j+1)+m*i)
for i in range(k):
    s=input().split()
    e,x,y=s[0],int(s[1]),int(s[2])
    if e=='R':
        for j in range(m): a[x-1][j]=(a[x-1][j]*y)%(1e9+7)
    if e=='S':
        for j in range(n): a[j][x-1]=(a[j][x-1]*y)%(1e9+7)
kq=0
for i in range(n):
    for j in range(m):
        kq=(kq+a[i][j])%(1e9+7)
print(int(kq))

   