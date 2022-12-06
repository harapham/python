global d ,n, k
d=[]

def hoanvi(s,i):
    if i==n:
        print(s)
    elif i<n:
        for j in range(n):
            if d[j]==0:
                d[j]=1
                hoanvi(s+k[j],i+1)
                d[j]=0

k=input()
n=len(k)
for i in range(n): d.append(0)
hoanvi('',0)