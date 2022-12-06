t = int(input())
while t>0:
    t-=1

    n = input()
    nn='0'
    i=0
    while i<1000:
        i+=1
        k = int(nn)+int(n)
        if k%7==0:
            print(k)
            break
        n=str(k)
        nn =n[::-1]
    if i==1000 and int(n)%7!=0:
        print(-1)
