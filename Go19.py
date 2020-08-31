Input_number = [x for x in input("Nhap vao cac so: ").split(",") if int(x) % 2 != 0]
print(",".join(Input_number))
