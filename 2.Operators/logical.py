"""
python ahs 3 logical operators
1. and
2. or
3. not

To check multiple conditions and returns Boolean value True or False
"""

age = 20

# print(age > 10 and age <20)
print(10 < age < 20)

print(age > 10 or age < 20)

print(not age > 10)

print(10 == 10 or 10 > 10 and 10 >= 20 or 10 <= 30 and 10 > 30 or 10 == 10)
"""
True or False and False or True and False or True 
True or False or False or True
True or True
True
"""
print(10 == 10 or 10 > 10 and 10 >= 20 or 10 <= 30 and 10 > 10 and 10 == 20 and 20 < 20 or 30 <= 4 and not False)
"""
True or False and False or True and False and False and False or False and not False
True or False or False and False or False and not False
True or False or False or False
True or False
True
"""
