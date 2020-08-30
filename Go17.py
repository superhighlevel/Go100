Input_Str = input("Nhap vao mot chuoi: ")
Values = {"Upper": 0, "Lower": 0}
for s in Input_Str:
    if s.isupper():
        Values["Upper"] += 1
    if s.islower():
        Values["Lower"] += 1
print("So chu hoa: %d\nSo chu thuong: %d"%(Values["Upper"],Values["Lower"]))