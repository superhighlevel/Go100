Values = []
for x in range(10000, 30010):
    a = str(x)
    flag = False
    for i in range(len(a)):
        if int(a[i]) % 2:
            flag = False
            break
        else:
            flag = True
    if flag:
        Values.append(a)
print(",".join(Values))
