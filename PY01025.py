s=input()
kq=''
k=-2
for i in range(len(s)):
    kq=s[-i-1]+kq
    if k%3==0: kq=','+kq
    k+=1
print(kq.strip(','))
