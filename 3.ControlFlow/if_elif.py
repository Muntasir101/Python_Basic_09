"""
age 0 to 10 : chocolate
age 10 to 20 : cake
age 20 to 30 : Burger
rest are water
"""

age = input("Your age : ")

if 0 <= int(age) <= 10:
    print("Chocolate")
elif 10 < int(age) <= 20:
    print("Cake")
elif 20 < int(age) <= 30:
    print("Burger")
else:
    print("Water")