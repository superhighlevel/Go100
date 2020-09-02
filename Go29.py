# Join Strings

def Join_Strs():
    S = []
    while True:
        Input_Str = input("nhap vao cac chuoi: ")
        if not Input_Str.strip() == "":
            S.append(Input_Str)
        else:
            break
    Str = ""
    for w in S:
        Str = Str + str(w)
    print(Str)


Join_Strs()
