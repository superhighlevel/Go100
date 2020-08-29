class IPString(object):
    def __init__(self):
        self.s =""

    def getString(self):
        self.s = input("Nhap vao mot chuoi: ")

    def Output(self):
        print(self.s.upper())

StrOj = IPString()
StrOj.getString()
StrOj.Output()