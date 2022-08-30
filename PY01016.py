t=int(input())
for i in range(t):
    a=input()
    for j in range(0,len(a),2):
        for k in range(int(a[j+1])):
            print(a[j],end='')
    print()