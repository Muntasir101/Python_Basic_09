class Calculator():

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2


obj = Calculator(10, 20)
print(obj.sum())
print(obj.sub())

