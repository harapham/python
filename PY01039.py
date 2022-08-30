t=int(input())
for i in range(t):
    s=input()
    k=s[0:2]
    if len(s)%2==0: k=k*(len(s)//2)
    else: k=k*(len(s)//2)+s[0]
    print("YES" if s==k else "NO")