"""
try
except
"""

a = 10
print(type(a))


def divide(a, b):
    a = int(input("First number : "))
    b = int(input("Second number : "))
    return a / b


try:
    print(divide(10, 0))
except Exception as error:
    print(error)

print("Hello, world!")
