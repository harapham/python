
def giaiThua(n):
    s=1
    for i in range(n):
        s*=i+1
    return s

t=int(input())
while t>0:
    t-=1
    ok=0
    s=input()
    tmp=0
    for i in range(len(s)):
        tmp+=giaiThua(int(s[i]))
        if tmp==int(s): ok=1
        elif tmp>int(s):
            break
    print('Yes' if ok==1 else 'No')
