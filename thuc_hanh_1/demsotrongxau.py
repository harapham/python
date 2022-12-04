t=int(input())
while t>0:
    s=input()
    n=input()
    print(len(s.split(n))-1)
    t-=1