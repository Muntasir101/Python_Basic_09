class car(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model


obj = car("bmw", '2012')

print(obj.name)
print(obj.model)
