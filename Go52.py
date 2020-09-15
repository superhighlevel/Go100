class VongTron(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14

Tron = VongTron(2)
print(Tron.area())