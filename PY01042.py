def kiem_tra(s):
    for i in range(len(s)):
        if s[i]!='0' and s[i]!='1' and s[i]!='2': 
            return False
    return True

t=int(input())
for i in range(t):
    s=input()
    print('YES' if kiem_tra(s)==True else 'NO')