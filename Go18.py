a = input("Nhap vao so a: ")
# n1 = int("%s"%a)
# n2 = int("%s%s"%(a,a))
# n3 = int("%s%s%s"%(a,a,a))
# n4 = int("%s%s%s%s"%(a,a,a,a))
# print("Tong can tinh: ",n1+n2+n3+n4)
n = input("Nhap vao so lan muon cong a: ")
values = 0
for i in range(1,int(n)+1):
    x= 0
    for j in range(i):
        x = int(a)+(int(a)*j*100)
    print(x)
    values += x
print(values)
