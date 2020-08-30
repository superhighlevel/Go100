Input_Str = input("Nhap vao mot chuoi: ")
Values = {"Char": 0, "Number": 0}
for s in Input_Str:
    if s.isalpha():
        Values["Char"] += 1
    if s.isnumeric():
        Values["Number"] += 1
print("So chu cai la: %d So chu so la: %d" % (Values["Char"], Values["Number"]))
