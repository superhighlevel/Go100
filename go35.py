# Dict và bình phương các số

def dictpower():
    d=dict()
    for x in range(1, 21):
        d[x]=x**2
    for x in d.items():
        print(x)
dictpower()