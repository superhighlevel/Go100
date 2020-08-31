netAmount = 0
while True:
    s = input("Nhap nhat ki giao dich: ")
    if not s:
        break
    Values = s.split(" ")
    F=Values[0]
    V=int(Values[1])
    if F == "D":
        netAmount+=V
    elif F == "W":
        netAmount-=V
    else:
        pass
print(netAmount)