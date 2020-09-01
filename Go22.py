from operator import itemgetter, attrgetter
A =[]
while True:
    s = input()
    if not s:
        break
    A.append(tuple(s.split(",")))
print(sorted(A))
print(sorted(A, key=itemgetter(0,1,2)))