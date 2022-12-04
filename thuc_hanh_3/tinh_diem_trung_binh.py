from decimal import *
class sinhVien :
    def __init__(self, ma, name, d1, d2, d3) :
        self.ma = 'SV{:02d}'.format(ma)
        temp=name.strip().split()
        name= ' '.join(temp)
        self.ten = name.title()
        self.diem = ( Decimal(d1)*3+Decimal(d2)*3+Decimal(d3)*2)/8
        self.xh=0
    

n=int(input())
a=[]
for i in range(n):
    a.append(sinhVien(i+1,input(),int(input()),int(input()),int(input())))
a= sorted(a, key = lambda x : -x.diem)
a[0].xh =1
for i in range(1,n):
    if a[i].diem == a[i-1].diem :
        a[i].xh = a[i-1].xh
    else :
        a[i].xh=i+1

for i in a:
    print(i.ma, i.ten, i.diem.quantize(Decimal('1.00'), ROUND_HALF_UP), i.xh)
