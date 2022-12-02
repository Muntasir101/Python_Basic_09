class Calculator():

    def sum(self, number1, number2):
        return number1 + number2

    def sub(self, number1, number2):
        return number1 - number2


obj = Calculator()
print(obj.sum(20, 30))
print(obj.sub(50, 20))
