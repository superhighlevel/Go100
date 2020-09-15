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