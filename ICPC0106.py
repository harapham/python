
t=int(input())

for i in range(t):
    b = int(input())
    k = input()
    if b==2 : b=1
    elif b==4 : b=2
    elif b==8 : b=3
    elif b==16 : b=4
    if len(k)%b !=0:
        for j in range(b-len(k)%b):
            k='0'+k
    
    res=''
    token = 0
    
    for i in range(len(k)):
        token+=int(k[i])*2**(b-1-i%b)
        if (i+1)%b==0:
            if token==10: res+='A'
            elif token==11: res+='B'
            elif token == 12 : res+='C'
            elif token == 13 : res+='D'
            elif token == 14 : res+='E'
            elif token == 15 : res+='F'
            else : res+=str(token)
            token = 0
    print(res)

