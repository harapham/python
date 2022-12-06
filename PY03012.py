import functools
class Sv:
    def __init__(self,name,ac,sub):
        self.name =name
        self.ac = ac
        self.sub = sub
def cmd(a,b):
    if a.ac<b.ac: return 1
    elif a.ac == b.ac:
        if a.sub>b.sub: return 1
        elif a.sub==b.sub:
            if a.name >b.name : return 1
            else: return -1
        else: return -1
    else: return -1

t=int(input())
a=[]
while t>0:
    t-=1
    name = input()
    ac,sub = [int(i) for i in input().split()]
    a.append(Sv(name,ac,sub))
a=sorted(a,key=functools.cmp_to_key(cmd))
for i in a:
    print(i.name+' '+str(i.ac)+' '+str(i.sub))
