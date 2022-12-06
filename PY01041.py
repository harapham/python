def check(n):
    if len(n)<3: return False
    i=0
    while i<len(n)-1 and n[i]<n[i+1]: i+=1
    if i<len(n)-1:
        while i<len(n)-1 and n[i]>n[i+1]: i+=1
    if i==len(n)-1: return True
    return False

t=int(input())
while t>0:
    t-=1

    n=input()
    print('YES' if check(n) else 'NO')

