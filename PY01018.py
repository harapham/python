P= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    t=input().split(' ')
    k=t[0]
    if k=='0': break
    s=t[1]
    kq=''
    for i in range(len(s)):
        kq=kq+P[(P.find(s[i])+int(k))%28]
    print(kq[::-1])


