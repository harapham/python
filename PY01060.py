def tinh(n):
    tong=0
    tich=1
    ok=0
    for i in range(len(n)):
        if i%2==1: tong+=int(n[i])
        else:
            if n[i]!='0':  
                tich*=int(n[i])
                ok=1
            
    if ok==0: tich=0
    print(str(tich)+' '+str(tong))

t=int(input())
while t>0:
    t-=1
    tinh(input())
