class People(object):
    name = "Yuuto"
    def __init__(self, name = None):
        self.name = name

Yuuto = People("Yuuto")
print("%s name is %s" %(People.name, Yuuto.name))

Nani = People()
Nani.name = "Nani"
print("%s name is %s" %(People.name, Nani.name))
