t=int(input())
for i in range(t):
    s=input()
    k=0
    for j in range(len(s)):
        k+=int(s[j])
    print('YES' if k%3==0 else 'NO')