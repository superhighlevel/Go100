Input_Str = input("Nhap vao mot chuoi: ")
Str = [s for s in Input_Str.split(" ")]
print(" ".join(sorted(list(set(Str)))))