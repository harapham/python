import re
t= int(input())
while t>0:
    t-=1

    n= int(input())
    i=2
    num = str(i)+str(i)[::-1]
    while int(num)<n:
        if re.fullmatch('[02468]+',str(i)):
            print(num, end=' ')
        i+=2
        num = str(i)+str(i)[::-1]
    print()