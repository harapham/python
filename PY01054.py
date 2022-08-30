t=int(input())
for i in range(t):
    s=input()
    kq=1
    for j in s:
        if j!='0': kq*=int(j)
    print(kq)