import re

t= int(input())
for i in range(t):
    s=input()
    n=[int(k) for k in re.findall("\d+",s)]
    print(min(n))