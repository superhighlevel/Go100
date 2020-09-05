def tupletan():
    t=(1,2,3,4,5,6,7,8,9,10)
    l=list()
    for i in t:
        l.append(t[i-1]) if int(t[i-1])%2==0 else 0
    print(l)
tupletan()
