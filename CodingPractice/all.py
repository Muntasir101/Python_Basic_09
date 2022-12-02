# Problem 1
"""
UserName = 'Eric'
print('Hello '+UserName+','+'Would you like like to learn some Python today?')
"""
"""
# Problem 2
UserName1 = 'Bob are you ready for sqa'
Lower_case = UserName1.lower()
Upper_case = UserName1.upper()
Tite_case = UserName1.title()
print(Lower_case,'\n',Upper_case,'\n', Tite_case)
"""
"""
# Problem 3
Quote = "“A person who never made a mistake never tried anything new.”"
print('Albert Einstein once said, '+ Quote)
"""
"""
# Problem 4
print('The result is Addition is: ',5+3)
print('The result is Subtraction is: ',10-2)
print('The result is Multiplication is: ',4*2)
print('The result is Division is: ',32/4)

"""
"""
# Problem 5
FavNum = '7'
msg = "My favourite numbers is "+ FavNum
print(msg)
"""
"""
# Problem 6
UserCar = input('What kind of rental car would like: ')
print('“Let me see if I can find you a '+ UserCar+ " “")
"""
"""
# Problem 7
Client = int(input('How many people are in their dinner group: '))
if Client>=8:
    print('They’ll have to wait for a table.')
else:
    print('That  table is ready.')
"""
"""
# Problem 8
UserInput = int(input('Enter Your Number: '))

if UserInput%10==0:
    print('Your entered number are multiple by 10 ','\n',UserInput ,'are  mutiple by 10')
else:
    print('Your entered number are not multiple by 10 ''\n',UserInput ,'are not mutiple by 10')
"""

# Problem 9
UserInput = input('Enter your desire choice: ')
while True:
    if UserInput=='Quit':
        print('Select one: ')
        break
    else:
        print('Again')
        break
"""
"""
# Problem 10
Age = int(input('Enter your age: '))

if 3 > Age:
    print('Your ticket is free')
elif 3<= Age<= 12:
    print('Your ticket price is 10$')
else:
    print('Your ticket price is 15$')
