t=int(input())
while t>0:
    a=input()
    a=a+'/'
    dem=1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            dem+=1
        else:
            print(str(dem)+a[i],end='')
            dem=1
    print()
    t-=1