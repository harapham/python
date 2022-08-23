t=int(input())
for i in range(t):
    a=input()
    print('YES' if a[0:2]==a[len(a)-2:] else 'NO')