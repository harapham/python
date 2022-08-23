a=input()
v_th=0
for i in range(len(a)):
    if 'a'<=a[i]<='z':
        v_th+=1
print(a.upper() if len(a)>2*v_th else a.lower())