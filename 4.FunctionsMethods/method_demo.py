"""
Function is A group of statement which can perform some specific task.
Methods are reusable and can be called multiple times when needed.
"""

"""
def sum_demo():
    number1 = 10
    number2 = 5
    result = number1 + number2
    print(result)


sum_demo()


def sub_demo():
    number1 = int(input("Enter Number 1: "))
    number2 = int(input("Enter Number 2: "))
    result = number1 - number2
    print(result)


sub_demo()

final_result = sum_demo() + sub_demo()
print(final_result)


# Return
def sum_demo2(number1, number2):
    return number1 + number2


print(sum_demo2(20, 10))


def sub_demo2(number1, number2):
    return number1 - number2


sub_demo2(20, 10)

final_result = sum_demo2(30, 20) + sub_demo2(10, 5)
print(final_result)


# Positional arguments
def sum_demo3(number1=5, number2=10):
    return number1 + number2


print(sum_demo3())

"""

"""
# variable Scope
a = 10


def test_case_1():
    b = 20
    print("Value of global a : " + str(a))
    print("Value of local b : " + str(b))


def test_case_2():
    c = 30
    print("Value of global a : " + str(a))
    print("Value of local c : " + str(c))


test_case_1()
test_case_2()
"""

# built-in function
# max()

print(max(20, 10, 12, 22, 30, 50))
print(min(20, 10, 12, 22, 30, 50))
print(round(12.93))

