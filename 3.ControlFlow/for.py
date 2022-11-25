"""
for i in range()
20*1=20
20*2=40
...
20*10=200
"""

num = int(input("Enter a number: "))
if 0 <= num <= 10:
    for i in range(1, 11):
        print(num, "*", i, "= ", num * i)
else:
    for i in range(1, 11):
        print(20, "*", i, "= ", 20 * i)



