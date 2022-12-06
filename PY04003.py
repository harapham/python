import math

class PS:
    def __init__(self,tu,mau):
        x = math.gcd(tu,mau)
        self.tu = int(tu/x)
        self.mau = int(mau/x)

    def __str__(self):
        return (str(self.tu)+'/'+str(self.mau))

tu,mau = [int(i) for i in input().split()]
a = PS(tu,mau)
print(a)