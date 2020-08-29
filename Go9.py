import math
c = 50
h = 30
data = [x for x in input("Nhap vao gia tri cho d: ").split(',')]
v = []
for d in data:
    v.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
print(','.join(v))
