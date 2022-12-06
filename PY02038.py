def ToHop(k,n):
    if k==0 or k==n : return 1
    if k==1 : return n
    return ToHop(k,n-1)+ToHop(k-1,n-1)

t=int(input())
a=[]
res=0
for i in range(t):
    a.append(input())
for i in range(t):
    res+= ToHop(2,int(a[i].count('C')))
    k=0
    for j in range(t):
        if a[j][i]=='C':
            k+=1
    if k>=2 :
        res+= ToHop(2,k)
print(res)

