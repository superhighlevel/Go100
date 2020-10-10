def Cal():
    return 5/0.1

try:
    Cal()
    # a = c
    a =  1
except ZeroDivisionError:
    print("Error! Không thể chia với 0")
except Exception as E:
    print("Có lỗi", E)
else:
    print("Có lỗi chi à ? ")
