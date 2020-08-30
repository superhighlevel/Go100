X = []
Bit = [x for x in input("Nhap cac so nhi phan").split(",")]
for p in Bit:
    Bp = int(p, 2)
    if not Bp%5:
        X.append(p)
print(",".join(X))
