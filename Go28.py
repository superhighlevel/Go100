# Sum list of integers
def SumInt():
    A = [x for x in input("Nhap vao cac so nguyen cach nhau boi khoang trong").split(" ")]
    sum=0
    for value in A:
        sum+=int(value)
    print("Tong cac so nguyen trong list la: ", sum)

SumInt()