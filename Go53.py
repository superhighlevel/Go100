class Hinhchunhat(object):
    def __init__(self, d, r):
        self.dai = d
        self.rong = r
    def DienTich(self):
        return self.dai*self.rong
ex = Hinhchunhat(10,2)
print(ex.DienTich())