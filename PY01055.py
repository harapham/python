
def kiem_tra(s):
    if len(s)%2==0: return False
    if s[0]==s[1]: return False
    k=s[0]
    for i in range(0,len(s)-1,2):
        if s[i]!=k: return False
    if s[len(s)-1]!=k: return False
    return True
t=int(input())
for i in range(t):
    s=input()
    print('YES' if kiem_tra(s)==True else 'NO')