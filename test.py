#
# def TongHaiSo(a, b):
#     Tong = a + b
#     return Tong
# x = TongHaiSo(3, 5)
#
# print(x)
#
# tong = 0
# dem = 0
# while (True):
#     giatri_input = input('Nhap vao mot so: ')
#     if giatri_input == 'done':
#         break
#     giatri_input = float(giatri_input)
#     tong = tong + giatri_input
#     dem = dem + 1
#     giatriTB = tong / dem
#
# print('Gia tri trung binh cong la:', giatriTB)

#Bai 4 ?


tenFile = input('Nhap vao ten File: ')
st = open(tenFile)
tuDienTu = dict()
fred = dict()
for dong in st:
    tachTuTrongMotDong = dong.split()
    for tu in tachTuTrongMotDong:
        fred[tu]=fred.get(tu,0)+1
        if tu not in tuDienTu:
            tuDienTu[tu] = 1
        else:
            tuDienTu[tu] += 1

input_str =input("Nhap vao mot tu can tim: ")
for tu in st:
    print(input_str, tu)
    if tu == input_str:
        print("Co tu")
        break
    else:
        continue

print(tuDienTu)
print(fred)
