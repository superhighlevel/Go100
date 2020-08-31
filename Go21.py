import re
Pass = []
Input_Pass = [x for x in input("Nhap mat khau: ").split(",")]
for p in Input_Pass:
    if (len(p)<6) or (len(p)>12):
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    Pass.append(p)
print(",".join(Pass))
