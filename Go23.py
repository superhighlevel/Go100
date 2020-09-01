def Gen_Number(x):
    for i in range(1,x+1):
        if i%7==0:
            yield i
Input = int(input("Nhap vao mot so: "))
A = [x for x in Gen_Number(Input)]
print(A)