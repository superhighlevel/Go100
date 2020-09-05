#Tuple và số chẵn

def tuplechan():
    t = (1,2,3,4,5,6,7,8,9,10)
    l = list()
    for i in t:
        l.append(t[i-1]) if int(t[i-1])%2==0 else 0
    t2=tuple(l)
    print(t2)

tuplechan()

# def tuplechan():
#     t = (1,2,3,4,5,6,7,8,9,10)
#     l = list()
#     for i in t:
#         print(t[i-1]) if int(t[i-1])%2==0 else 0
#
# tuplechan()