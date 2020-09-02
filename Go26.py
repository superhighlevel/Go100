# Calculate sum of 2 numbers
def sum():
    A = [x for x in input("Nhap vao 2 so x, y: ").split(" ")]
    print("x + y = ", int(A[0])+int(A[1]))
sum()