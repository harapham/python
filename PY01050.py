
def ABC(s,n):
    if len(s)==n and s.count('A')>0 and s.count('A')<=s.count('B') <= s.count('C'):
        print(s)
    elif len(s)<n:
        ABC(s+'A',n)
        ABC(s+'B',n)
        ABC(s+'C',n)

n=int(input())
for i in range(3,n+1):
    ABC('',i)