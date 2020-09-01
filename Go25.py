Input_Str= input("Nhap vao mot chuoi: ")
Str=Input_Str.split(" ")
Freq = {}
for word in Str:
    Freq[word] = Freq.get(word,0)+1
    print(Freq)
Hmm=sorted(Freq.keys())
for a in Hmm:
    print("%s:%d"%(a,Freq[a]))
