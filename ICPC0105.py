import re
t = int(input())
for i in range(t):
    x = [int(j) for j in re.findall("\d+",input())]
    print(max(x))