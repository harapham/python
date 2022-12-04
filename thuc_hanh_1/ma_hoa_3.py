def rotate(s):
    n=0
    for i in s: n+=ord(i)-ord('A')
    k=''
    for i in s: k+=chr((ord(i)-ord('A')+n)%26+ord('A'))
    return k
t=int(input())
for x in range(t):
    s,k=input(),''
    n=len(s)//2
    a,b=s[:n],s[n:]
    a=rotate(a)
    b=rotate(b)
    for i in range(n): 
        k+=chr((ord(a[i])-2*ord('A')+ord(b[i]))%26+ord('A'))
    print(k)