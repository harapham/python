import math

s=[int(i) for i in input().split()]

for i in range(s[0],s[1]-1):
    l,r=i+1,i+2
    while l<s[1] and l<s[1]:
        if math.gcd(i,l)==1 and math.gcd(i,r)==1 and math.gcd(l,r)==1:
            print('('+str(i)+', '+str(l)+', '+str(r)+')')
        r+=1
        if r>s[1] :
            l+=1
            r=l+1

    
    