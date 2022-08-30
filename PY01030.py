s=input().split()
n=int(s[0])
k=int(s[1])

def nguyen_to(a,b):
    if b==0: return a
    return nguyen_to(b,a%b)
d=0
for i in range(pow(10,k-1),pow(10,k)):
    if nguyen_to(n,i)==1:
        if d%10==0: 
            print()
        d+=1
        print(i,end=' ')