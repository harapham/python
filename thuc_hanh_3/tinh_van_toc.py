class CuaRo :
    def __init__(self, ten, donVi, thoiGian) :
        a = [i[0] for i in ten.split()]
        b = [i[0] for i in donVi.split()]
        self.id = ''.join(b) + ''.join(a)
        self.ten = ten
        self.donVi = donVi
        c = thoiGian.split(':')
        self.vanToc = 120 / (int(c[0]) - 6 + int(c[1]) / 60)

    def __str__(self) :
        return f"{self.id} {self.ten} {self.donVi} {round(self.vanToc)} Km/h"

n = int(input())
cuaRo = []
for i in range(n) :
    cuaRo.append(CuaRo(input(), input(), input()))
cuaRo = sorted(cuaRo, key = lambda x : -x.vanToc)
print(*cuaRo, sep = '\n')
