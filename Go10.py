# Input_XY=input("Nhap vao X,Y: ")
# XY=[int(x) for x in Input_XY.split(',')]
# Dx = XY[0]
# Dy = XY[1]
# Mlt = [[0 for col in range(Dy)] for row in range(Dx)]
# for row in range(Dx):
#     for col in range(Dy):
#         Mlt[row][col]=row*col
# print(Mlt)


Input_AB=input("Nhap vao A,B: ")
AB=[int(x) for x in Input_AB.split(',')]
A=AB[0]
B=AB[1]
Values = [[0 for col in range(B)] for row in range(A)]
for row in range(A):
    for col in range(B):
        Values[row][col]=row*col
print(Values)