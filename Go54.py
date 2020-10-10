class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0

class square(object):
    def __init__(self, l):
        self.length = l
    def area(self):
        return self.length*self.length

aSquare = square(12)
print(aSquare.area())
ax = Shape()
print(ax.area())

class Shape(object):
    def __init__(self):
        pass
    def Area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.l = length

    def Area(self):
        return self.l**2

ASquare = Square(5)
print(ASquare.Area())