def kiem_tra(n):
    n=str(n)
    k=n[::-1]
    if k==n and len(n)>1: return True
    return False

t=int(input())
for i in range(t):
    s=input()
    kq=0
    for j in range(len(s)):
        kq+=int(s[j])
    print('YES' if kiem_tra(kq)==True else 'NO')