t = int(input())

s = []

for i in [int(j) for j in input().split()]:
    if len(s) and (not (s[len(s)-1]+i)%2 ):
        s.pop()
    else:
        s.append(i)
print(len(s))

