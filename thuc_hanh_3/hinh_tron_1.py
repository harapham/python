class point:
    def __init__(self, x,y):
        self.x =int(x)
        self.y =int(y)

t=int(input())
for c in range(t):
    n= int(input())
    k= int(input())
    a=[0,1,2,3]
    ok=1
    kq=0
    points=[]
    for i in range(n):
        li=input().split()
        points.append(point(li[0],li[1]))

    while ok==1:
        ax = points[a[1]-1].x
        ay = points[a[1]-1].y
        bx = points[a[2]-1].x
        by = points[a[2]-1].y
        cx = points[a[3]-1].x
        cy = points[a[3]-1].y
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if d> 0:
            ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
            uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
            khoangcach= (ax-ux)*(ax-ux)+(ay-uy)*(ay-uy)
            count=0
            for j in points:
                if (j.x-ux)*(j.x-ux)+(j.y-uy)*(j.y-uy)<khoangcach: count+=1
            if count ==k :
                print('YES')
                kq=1
                break
        
        i =3 
        while i>0 and a[i]==n-3+i : i-=1
        if i>0 :
            a[i]=a[i]+1
            for j in range(i+1,4):
                a[j] =a[i]-i+j
        else : ok=0
        
    if kq==0: print('NO')    