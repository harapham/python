
s=input().split()
n=int(s[0])
m=int(s[1])

a=[[]]*n
ln=0
nn=1e5+1
for i in range(n):
    a[i]=[int(x) for x in input().split()]
    if ln<max(a[i]): ln=max(a[i])
    if nn>min(a[i]): nn=min(a[i])
k=ln-nn
ok=0

for i in range(n):
    for j in range(m):
        if a[i][j]==k: 
            if(ok==0): print(int(k))
            ok=1
            print(f'Vi tri [{i}][{j}]')
if(ok==0): print('NOT FOUND')
